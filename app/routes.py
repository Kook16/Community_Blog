from flask import render_template
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
        "content": "Being a software engineer involves solving complex problems, coding, and continuously learning new technologies. It's challenging but rewarding."
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

