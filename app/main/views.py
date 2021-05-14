from random import randint
from flask import render_template, redirect
from flask_login import current_user, login_required
from . import main
from .. import db
from ..forms import FindForm, PostForm
from ..models import User, Post

@main.route("/", methods=["POST", "GET"])
def index() :
	form = FindForm()
	if current_user.is_authenticated :
		reg_user = current_user
	else :
		reg_user = None
	if form.validate_on_submit() :
		user = User.query.filter_by(nickname=form.nickname.data).first()
		if user :
			return redirect("/user/{}".format(user.id))
	return render_template("index.html", form=form, reg_user=reg_user)

@main.route("/user/<user_id>", methods=["POST", "GET"])
@login_required
def user_route(user_id) :
	user = User.query.get(int(user_id))
	posts = Post.query.filter_by(creator=user, is_op=True)
	form = PostForm()
	if current_user.id == user.id :
		is_user_post = True
		if form.validate_on_submit() :
			new_id = randint(0,10000)
			while Post.query.filter_by(post_id=new_id).first() :
				new_id = randint(0,10000)
			new_post = Post(text=form.text.data, creator=current_user, is_op=True, post_id=new_id)
			db.session.add(new_post)
			db.session.commit()
	else :
		is_user_post = False
	return render_template("user_page.html", user=user, posts=posts, is_user_post=is_user_post, form=form)

@main.route("/post/<post_id>", methods=["POST", "GET"])
@login_required
def post_route(post_id) :
	form = PostForm()
	posts = Post.query.filter_by(post_id=post_id)
	if form.validate_on_submit() :
		new_post = Post(text=form.text.data, is_op=False, creator=current_user, post_id=post_id)
		db.session.add(new_post)
		db.session.commit()
	return render_template("post.html", form=form, posts=posts, post_id=post_id)	