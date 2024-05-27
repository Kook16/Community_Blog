from flask import Flask, render_template, redirect, url_for, flash, request
from flask_mail import Message
from .forms import RegistrationForm, LoginForm, AddPost, ResetPasswordRequestForm, ResetPassword, ResetConfirmationLink
from app import app, db, login_manager, mail, bcrypt
from app.models import Post, User
from app.utils import generate_confirmation_token, confirm_token
from flask_login import current_user, logout_user, login_user, login_required
from itsdangerous import SignatureExpired, BadTimeSignature, URLSafeTimedSerializer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_required
@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    if current_user.is_anonymous:
        return redirect(url_for('landingpage'))
    form = AddPost()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data,
                    user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    posts = Post.query.all()
    return render_template('home.html', title='Home', posts=posts, form=form)

@login_required
@app.route('/about/<username>')
def about(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.timestamp.desc()).all()
    return render_template('about.html', title='About', posts=posts, user=user)


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data,
                    password=password_hash)
        db.session.add(user)
        db.session.commit()
        token = generate_confirmation_token(user.email)
        confirm_url = url_for('confirm_email', token=token, _external=True)
        html = render_template('activate.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_email(user.email, subject, html)
        flash('A confirmation email has been sent via email.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=app.config['MAIL_USERNAME']
    )
    mail.send(msg)

@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = confirm_token(token)
        if not email or not isinstance(email, str):
            raise ValueError("Invalid email")
    except SignatureExpired:
        flash('The confirmation link has expired.', 'danger')
        return redirect(url_for('resend_confirmation'))
    except BadTimeSignature:
        flash('The confirmation link is invalid.', 'danger')
        return redirect(url_for('resend_confirmation'))
    except Exception as e:
        flash('The confirmation link is invalid or has expired.', 'danger')
        return redirect(url_for('login'))

    user = User.query.filter_by(email=email).first_or_404()
    if user.is_active:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.is_active = True
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('login'))

@app.route('/resend_confirmation', methods=['GET', 'POST'])
def resend_confirmation():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = ResetConfirmationLink()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()

        if user is None:
            flash('Email address not found.', 'danger')
            return redirect(url_for('resend_confirmation'))
        
        if user.is_active:
            flash('Account already confirmed. Please login.', 'success')
            return redirect(url_for('login'))
        
    # generate new confirmation token
        token = generate_confirmation_token(user.email)
        confrim_url = url_for('confirm_email', token=token, _external=True)
        subject = 'Please confrim your email'
        html = render_template('confirm.html', confrim_url=confrim_url)

        #send confirmation email
        send_email(user.email, subject, html)
        flash('A new confirmation email has been sent.', 'success')
        return  redirect(url_for('login'))
    
    return render_template('resend_confirmation.html', title='Resend Confirmation', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            if user.is_active:
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('home'))
            else:
                flash('Please activate your account first.', 'warning')
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@login_required
@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/follow/<username>')
def follow(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        flash('User {} not found'.format(username), 'danger')
        return redirect(url_for('home'))
    if user == current_user:
        flash('You cannot follow yourself!', 'danger')
        return redirect(url_for('about', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are now following {}'.format(username), 'success')
    return redirect(url_for('about', username=username))


@app.route('/unfollow/<username>')
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        flash('User {} not found'.format(username), 'danger')
        return redirect(url_for('home'))
    if user == current_user:
        flash('You cannot unfollow yourself!', 'danger')
        return redirect(url_for('about', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You have unfollowed {}'.format(username), 'success')
    return redirect(url_for('about', username=username))

@app.route('/landingpage')
def landingpage():
    return render_template('landingpage.html')

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password_request():
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()

        if user:
            token = generate_confirmation_token(user.email)
            reset_url = url_for('reset_password', token=token, _external=True)
            subject = "Password Reset Requested"
            html = render_template('reset_password_email.html', reset_url=reset_url)
            send_email(user.email, subject, html)
            flash('A password reset email has been sent to you.', 'info')
        else:
            flash('Email address not found.', 'danger')     
            return redirect(url_for('login'))
    return render_template('reset_password_request.html', form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    try:
        email = confirm_token(token)
    except:
        flash('The password reset link is invalid or has expired.', 'danger')
        return redirect(url_for('reset_password_request'))
    form = ResetPassword()

    if form.validate_on_submit():
        password = form.password.data
        user = User.query.filter_by(email=email).first_or_404()
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = password_hash
        db.session.commit()
        flash('Your password has been updated!', 'success')
        return redirect(url_for('login'))
    
    return render_template('reset_password.html', form=form)