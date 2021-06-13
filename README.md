# prose
Prose is the simple twitter clone build with Flask
In prose you can keep your blog, see other people's blog,chat with other peoples

## Running localy
    $ pip3 install -r requirements.txt
    $ export FLASK_APP=prose.py
    $ flask run

## Dockerfile
    $ docker build -t prose .
    $ docker run -p 8000:5000 prose
    
## Running on the production server
    $ gunicorn prose:app 
  
## Prose hosted on heroku:
https://first-prose.herokuapp.com/
