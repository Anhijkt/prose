from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class FindForm(FlaskForm) :
	nickname = StringField(validators=[DataRequired()]) 
	submit = SubmitField("Find")
class RegForm(FlaskForm) :
	username = StringField("Username: ")
	nickname = StringField("Nickname: ", validators=[DataRequired()])
	password = PasswordField("Password: ", validators=[DataRequired()])
	submit = SubmitField("Submit")
class PostForm(FlaskForm) :
	text = StringField("Text: ", widget=TextArea(), validators=[DataRequired()])
	submit = SubmitField("Post")
