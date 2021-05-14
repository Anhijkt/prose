from flask import jsonify
from . import api
from ..models import User, Post

@api.route("/posts/")
def all_post_route() :
	posts = [post.to_json() for post in Post.query.all()]
	return jsonify({"posts" : posts})
@api.route("/users/")
def all_user_route() :
	users = [user.to_json() for user in User.query.all()]
	return jsonify({"users" : users})
@api.route("/posts/<post_id>")
def post_route(post_id) :
	return Post.query.get(post_id).to_json()
@api.route("/users/<post_id>")
def user_route(post_id) :
	return User.query.get(post_id).to_json()
