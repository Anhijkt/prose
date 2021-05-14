from flask import render_template, redirect
from flask_login import login_user, logout_user, login_required
from . import auth
from .. import db
from ..forms import RegForm
from ..models import User

@auth.route("/login", methods=["POST", "GET"])
def login() :
	form = RegForm()
	if form.validate_on_submit() :
		user = User.query.filter_by(nickname=form.nickname.data).first()
		if user and user.verify_password(form.password.data) :
			login_user(user)
			return redirect("/")
	return render_template("login.html", action="login", form=form)
@auth.route("/registrate", methods=["POST", "GET"])
def registrate() :
	form = RegForm()
	if form.validate_on_submit() :
		if not User.query.filter_by(nickname=form.nickname.data).first() and "@" in form.nickname.data :
			new_user = User(username=form.username.data, nickname=form.nickname.data, password=form.password.data)
			db.session.add(new_user)
			db.session.commit()
			login_user(new_user)
			return redirect("/")		
	return render_template("login.html", action="registrate", form=form)

@auth.route("/logout")
@login_required
def logout() :
	logout_user()
	return redirect("/")