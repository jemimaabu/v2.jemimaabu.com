import os
import requests
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_mail import Mail, Message
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer

app = Flask(__name__)

# app.config['MAIL_SERVER'] = 'smtp.mailgun.org'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_DEBUG'] = True
# app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_SUPPRESS_SEND'] = False
# app.config['MAIL_USERNAME'] = 'postmaster@sandbox212ba39fba0f4cd99214a881a5db6bcd.mailgun.org'
# app.config['MAIL_PASSWORD'] = 'aaa434a86fff147674fe4f2a8e07d509-1b65790d-a2ba2bff'
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SECRET_KEY'] = "secret"

apikey="4758595800fe577e1f9608e15917716d-1b65790d-7c8d4065"
url="https://api.mailgun.net/v3/sandbox212ba39fba0f4cd99214a881a5db6bcd.mailgun.org"

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
    form = MyForm()

    if form.validate_on_submit():
        requests.post(url,
                      auth=("api", apikey),
                      data={"from": "testing@test.com",
                            "to": ["jemimaabu@gmail.com"],
                            "subject": "New Contact Entry",
                            "text": "Test"}
                      )
        # requests.post(url,
        #   auth=("api", api),
        #   data={"from": (form.name.data, form.email.data),
        #         "to": "jemimaabu@gmail.com",
        #         "subject": form.subject.data,
        #         "text": form.message.data}
        #   )
        return redirect('')

    return render_template('index.html', form=form)


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

