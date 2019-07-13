import os
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_mail import Mail, Message
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
BLOG_DIR = 'blog'


flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)


mail = Mail(app)


class MyForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")


@app.route('/', methods=['GET', 'POST'])
def root():
    return render_template('index.html')


@app.route("/blog")
def blog():
    blog = [p for p in flatpages if p.path.startswith(BLOG_DIR)]
    blog.sort(key=lambda item: item['date'], reverse=False)
    return render_template('blog.html', blog=blog)


@app.route('/blog/<name>/')
def post(name):
    path = '{}/{}'.format(BLOG_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)

