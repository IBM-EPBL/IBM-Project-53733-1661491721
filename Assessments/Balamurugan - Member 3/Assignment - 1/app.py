from flask import Flask , render_template

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("homepage.html")

@app.route("/about me")
def about_page():
    return render_template("about me.html")

@app.route("/contact us")
def contact_page():
    return render_template("contact us.html")

@app.route("/signin page")
def signin_page():
    return render_template("signin page.html")

@app.route("/signup")
def signup_page():
    return render_template("signup.html")
