# from crypt import methods
from datetime import datetime
from email import contentmanager
from email.policy import default
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from matplotlib.pyplot import title



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return 'Blog post ' + str(self.id)

# def __init__(self, title, content, author,created_at):
#    self.title = title
#    self.content = content
#    self.author = author
#    self.created_at = created_at


@app.route('/')
@app.route('/home')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('posts'))
    else:
        all_posts = BlogPost.query.order_by(BlogPost.created_at).all()
        return render_template('posts.html', posts=all_posts)

@app.route('/home/users/<string:name>/posts/<int:id>')

def hello(name, id):
    return "Hello, " + name + " your id is: "+ str(id)

@app.route('/onlyget', methods=['GET'])
def get_req():
    return "Only GET this"

@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')

@app.route('/posts/edit/<int:id>', methods=('GET','POST'))
def edit(id):
    post = BlogPost.query.get_or_404(id)
    if request.method == 'POST':
        post.post_title = request.form['title']
        post.post_content = request.form['content']
        post.post_author = request.form['author']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html',post=post)

@app.route('/posts/new', methods=('GET','POST'))
def new_post():
    if request.method == 'POST':
        post.post_title = request.form['title']
        post.post_content = request.form['content']
        post.post_author = request.form['author']
        new_post= BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else: 
        return render_template('new_post.html')

if __name__ == "__main__":
    app.run(debug=True)




