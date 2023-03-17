from flask import Blueprint, render_template, flash, url_for, redirect
from itp.form import Register, Login


views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html")

@views.route("/Signup", methods=['GET', 'POST'])
def Signup():
    form = Register() 
    if form.validate_on_submit():
        flash("You Successfully Register!", "success")
        return redirect(url_for("views.login"))
    return render_template("Signup.html", form=form)

@views.route("/login", methods=['GET', 'POST'])
def login():
    form = Login()

    if form.validate_on_submit():
        if form.email_add.data == "mike@gmail.com" and form.password.data == "123456":
            flash("You Successfully Login!", "success")
            return redirect(url_for("views.home"))
        else:
            flash("Wrong email or password please check!", "danger")
    else:
        print("...")
    return render_template("login.html", form=form)

