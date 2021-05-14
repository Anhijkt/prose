from datetime import datetime
from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id) :
	return User.query.get(int(user_id))

class User(db.Model, UserMixin) :
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), nullable=False)
	nickname = db.Column(db.String(80), nullable=False, unique=True)
	password_hash = db.Column(db.String(80), nullable=False)
	posts = db.relationship("Post", backref="creator")

	@property
	def password(self):
		raise AttributError("password is not readeble")
	@password.setter
	def password(self, password) :
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password) :
		return check_password_hash(self.password_hash, password)
	def to_json(self) :
		json = {"username" : self.username,
				"nickname" : self.nickname,
				"posts_id" : [post.id for post in self.posts]}
		return json
	def __repr__(self) :
		return "<User {}>".format(self.id)

class Post(db.Model) :
	__tablename__ = "posts"
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.Text, nullable=False)
	is_op = db.Column(db.Boolean, nullable=False)
	post_id = db.Column(db.Integer, nullable=False)
	creator_id = db.Column(db.Integer, db.ForeignKey("users.id"))
	creation_date = db.Column(db.DateTime(), default=datetime.utcnow)

	def to_json(self) :
		json = {"text" : self.text,
				"is_op" : self.is_op,
				"post_id" : self.post_id,
				"creator_id" : self.creator_id,
				"creation_date" : self.creation_date.ctime()}
		return json
	def __repr__(self) :
		return "<Post {}>".format(self.id)