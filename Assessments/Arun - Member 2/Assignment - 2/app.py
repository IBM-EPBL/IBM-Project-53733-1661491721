from flask import Flask , render_template

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("homepage.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/signin")
def signin_page():
    return render_template("signin.html")

@app.route("/signup")
def signup_page():
    return render_template("signup.html")