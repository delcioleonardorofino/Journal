from flask import Flask, render_template, abort, request
from .utils import load_posts, all_posts

app = Flask(__name__)

@app.errorhandler(404)
def error(e):
    return render_template('erro-404.html'), 404

@app.get('/')
def home():
    return render_template('index.html')

@app.get('/posts')
def get_posts():
    return render_template('posts.html', posts=all_posts)


@app.get('/healthcheck')
def keep_alive():
    return 'Keeping server alive!'

@app.get('/posts/<int:id>')
def get_post(id):
    
    posts = all_posts
    post = load_posts(id)

    if post is None:
        abort (404)

    if "HX-Request" in request.headers:
        return render_template('partial_post.html', posts=posts, post = post)
    
    return render_template('post.html', posts=posts, post=post)