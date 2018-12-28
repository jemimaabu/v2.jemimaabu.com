import os
import settings
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_USERNAME'] = settings.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = settings.MAIL_PASSWORD
app.config['SECRET_KEY'] = settings.SECRET_KEY


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
        msg = Message(
            'Sending file',
            sender=(form.name.data, form.email.data),
            recipients=["jemimaabu@gmail.com"])
        msg.body = "Email: " + form.email.data + "\nMessage: " + form.message.data
        msg.subject = form.subject.data
        mail.send(msg)
        return redirect('')

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)