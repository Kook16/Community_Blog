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
        "content": "Being a software engineer involves solving complex problems, coding, and continuously learning nTech Debt is Expensiv  The main argument to justify that Tech Debt is bad is the price. So I tried to get a sense of this cost. But unlike a loan where the interest rate is written on the contract, tech debt is hard to measure. I attempted to look at the velocity of the team by story point. I noticed the velocity of the team working on the monolith was slower than the one working on the micro-service architecture. After a few months, I realised that tech debt wasn’t the issue. It was just the amount of features to maintain. Once we reached 3 microservices, the second team became slower than the monolith, despite everyone telling me the micro-service code ou couldn’t afford one upfront payment. Leveraging debt allows you to achieve a goal. Starting a company requires initial funding. Enfinancial debt that was raised thanks to the technical debt.."
    },
    {
        "author": "Charlie",
        "title": "The Benefits of Morning Exercise",
        "time_created": "2024-05-17 06:45:00",
        "content": "Starting your day with a morning workout can boost your energy levels, improve your mood, and set a positive tone for the rest of the daylonger it remains unresolved, the more work will be required to fix it later. It was a good way to explain how business teams prioritize maintenance work over new features. It became something terrible in the ecosystem. But is debt a problem? To buy a house, you get a mortgage and pay monthly iired developer complained that the first mobile app was built using React Native, instead of a native technology like Swift for iOS. I had to remind this person that before being a scale-up with 100+ engineers and 6 dedicated mobile developers, the initial mobile app was built by the only front-end engineer. He didn’t know any native language, so he used what he knew and released an MVP in less than a month. Thanks to this quick MVP, the company acquired thousands of clients. This sales traction allowed us to raise a series B, and with this money, we hired a dedicated mobile developer to build a native app. His salary was literally paid by financial debt that was raised thanks to the technical debt."
    },
    {
        "author": "Dana",
        "title": "Exploring the Local Cuisine",
        "time_created": "2024-05-18 13:20:00",
        "content": "I recently had the chance to explore our local cuisine. The variety of flavors and the richness of the dishes were truly amazing. I highly recommend trying the street food. d, “DynamoDB was released in 2012, this project started in 2009” I’ve learned to assume good intentions. The team before you had different constraints but knew what they were doing. If you don’t understand a choice, ask about the context of the decision. It could have been the only valid choice at the time. Is Tech Debt that bad? Tech Debt started as a metaphor inspired by the finance industry, just like financial debt, technical debt accumulates interest, meaning that the ."
    },
    {
        "author": "Eli",
        "title": "Tips for a Successful Garden",
        "time_created": "2024-05-19 08:00:00",
        "content": "Gardening requires patience and care. Some tips for success include choosing the right plants for your climate, watering regularly, and keeping an eye out for pests d, “DynamoDB was released in 2012, this project started in 2009” I’ve learned to assume good intentions. The tthe better, but they are just borrowing money from investors expecting returns. Debt allows them to achieve a goal. Like a tool, it’s not a bad thing. That’s how the economy works. It’s the same for software development. I joined an early startup in 2019, with a team of 8 developers. Two years later, a freshly hired developer complained that the first mobile app was built using React Native, instead of a native technology like .."
    }
    ]
    return render_template('home.html', title='Home', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/Contact')
def contact():
    return render_template('contact.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')
