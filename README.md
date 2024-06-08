Community Blog App
Welcome to the Community Blog App, a platform for users to share their thoughts and ideas through blog posts. This application allows users to register, log in, create posts, edit them, and view posts by other users.

Table of Contents
Features
Installation
Prerequisites
Setup
Usage
Routes
Technologies Used
Contributing
License
Contact
Features
User authentication (register, login, logout)
Create, edit, and delete blog posts
View posts from all users
Pagination for posts
User profiles with bio and image
Responsive design for mobile and desktop
Installation
Prerequisites
Python 3.8 or higher
Virtual environment tool (venv or virtualenv)
SQLite (comes bundled with Python)
Setup
Clone the repository:


git clone https://github.com/yourusername/community_blog_app.git
cd community_blog_app
Create a virtual environment and activate it:


python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required packages:


pip install -r requirements.txt
Usage
Open your web browser and navigate to http://127.0.0.1:5000.
Register a new account.
Log in with your new account.
Create, edit, and view blog posts.
Routes
/: Home page displaying blog posts
/register: User registration
/login: User login
/logout: User logout
/account: User account management
/post/new: Create a new post
/post/<int:post_id>: View a specific post
/post/<int:post_id>/edit: Edit a specific post
/post/<int:post_id>/delete: Delete a specific post
Technologies Used
Backend:
Python
Flask
Flask-SQLAlchemy
Flask-Migrate
Flask-Login
Flask-WTF
Frontend:
Jinja2
Bootstrap (for styling)
Database:
SQLite
Contributing
We welcome contributions from the community. Please follow these steps to contribute:

Fork the repository:
Click the "Fork" button at the top right of this page to create your own copy of the repository.

Clone your fork:


git clone git@github.com:Kook16/Community_Blog.git
cd community_blog_app
Create a new branch:


git checkout -b feature/your-feature-name
Make your changes:
Implement your feature or bug fix.

Commit your changes:


git commit -m "Description of your changes"
Push to your fork:


git push origin feature/your-feature-name
Create a pull request:
Go to the original repository and click the "New pull request" button. Provide a detailed description of your changes and submit the pull request.


Contact
For any questions or feedback, please contact:

Your Name: calvin51416@gmail.com
GitHub: kook16
Thank you for using the Community Blog App! We hope you enjoy it.
