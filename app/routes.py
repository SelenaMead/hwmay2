from app import app 

@app.route('/')
def home():
    return '<h1>Home Page</h1>'
@app.route('/about')
def about():
    return '<h1>About</h1>'
@app.route('/contact')
def contact():
    return '<h1>Contact</h1>'