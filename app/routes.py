from flask import Flask, render_template, redirect, url_for, flash
from .forms import RegistrationForm, LoginForm
from app import app

@app.route('/')
@app.route('/home')
def home():
    posts = [
        {
            "author": "Alice",
            "title": "My Journey to the Mountains",
            "time_created": "2024-05-15 10:30:00",
            "content": "Last weekend, I visited the mountains and it was a breathtaking experience. The fresh air and the scenic views were unforgettable."
        },
        {
            "author": "Bob",
            "title": "A Day in the Life of a Software Engineer",
            "time_created": "2024-05-16 09:15:00",
            "content": "Being a software engineer involves solving complex problems, coding, and continuously learning new technologies. It’s a dynamic and rewarding career."
        },
        {
            "author": "Charlie",
            "title": "The Benefits of Morning Exercise",
            "time_created": "2024-05-17 06:45:00",
            "content": "Starting your day with a morning workout can boost your energy levels, improve your mood, and set a positive tone for the rest of the day."
        },
        {
            "author": "Dana",
            "title": "Exploring the Local Cuisine",
            "time_created": "2024-05-18 13:20:00",
            "content": "I recently had the chance to explore our local cuisine. The variety of flavors and the richness of the dishes were truly amazing. I highly recommend trying the street food."
        },
        {
            "author": "Eli",
            "title": "Tips for a Successful Garden",
            "time_created": "2024-05-19 08:00:00",
            "content": "Gardening requires patience and care. Some tips for success include choosing the right plants for your climate, watering regularly, and keeping an eye out for pests."
        }
    ]
    return render_template('home.html', title='Home', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print("form submitted")
    if form.validate_on_submit():
        if form.email.data == 'hello@gmail.com' and form.password.data == 'password':
            flash('Logged in successfully!', 'success')
            print("Redirecting to home")
        else:
            flash('Unsuccessful Login, Please Check email and password and try again!', 'danger')
            print("unsuccessful login")
    return render_template('/home.html', title='Login', form=form)


@app.route('/logout')
def logout():
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))