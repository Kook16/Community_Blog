from flask import Flask, render_template, redirect, url_for, flash
from .forms import RegistrationForm, LoginForm, AddPost
from app import app, db, login_manager
from app.models import Post, User
from flask_login import current_user, logout_user, login_user, login_required


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_required
@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
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
        user = User(username=form.username.data, email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        if user and form.password.data == user.password:
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        flash('Unsuccessful Login, Please Check email and password and try again!', 'danger')
        return redirect(url_for('login'))
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
