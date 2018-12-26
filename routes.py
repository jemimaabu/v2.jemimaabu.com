from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(dict(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME="jemimaabu@gmail.com",
    MAIL_PASSWORD="potatoez",
    MAIL_DEBUG=True,
    MAIL_SUPPRESS_SEND=False
))

mail = Mail(app)

app.secret_key = 'development key'


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