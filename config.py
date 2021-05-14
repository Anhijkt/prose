import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config :
	SECRET_KEY = "ANOTHER SECRET KEY"
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "data.sqlite")

	@staticmethod
	def init_app(app) :
		pass
class DevelopmentConfig(Config) :
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "dev-data.sqlite")
class ProductionConfig(Config) :
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "data.sqlite")

config = {"default": Config,
		  "development": DevelopmentConfig,
		  "production": ProductionConfig}