from app import create_app
from app.models import db, User, Post

app = create_app("production")

@app.shell_context_processor
def make_context() :
	return dict(db=db, Post=Post, User=User)