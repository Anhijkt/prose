# prose
Prose is the simple twitter clone build with Flask

## Running localy
1) Installing dependencies
    $ pip3 install -r requirements.txt
2) Running on local server
    $ export FLASK_APP=prose.py
    $ flask run 

## Dockerfile
1) Building docker image
    $ docker build -t prose .
2) Running image in container
    $ docker run -p 8000:5000 prose
    
## Running on the production server
    $ gunicorn prose:app 
https://first-prose.herokuapp.com/
