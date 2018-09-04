from flask import Flask, request
import datetime
from threading import Lock
# pip install flask-WTF
from flask_wtf import FlaskForm
from wtforms import StringField, validators


class ContactForm(FlaskForm):
    def valid_date(self, field):
        a = datetime.datetime.now()
        l = field.data.split('.')
        t = []
        for x in l:
            t.append(int(x))
        if a.month != t[1]:
            raise ValueError('enter now date')
    name = StringField(label='Name', validators=[
        validators.Length(min=4, max=25)
    ])
    email = StringField(label='E-mail', validators=[
        validators.Length(min=6, max=35),
        validators.Email()
    ])
    job = StringField(label='JOB', validators=[
        validators.Length(min=1, max=35),
        validators.AnyOf(['IT','Bank', 'HR'])])
    date = StringField(label='date', validators=[
        validators.Length(min=8, max=8),
        valid_date
        ])


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate():
            return ('valid', 200)
        else:
            return ('invalid', 400)

    if request.method == 'GET':
        return 'hello world!', 200


if __name__ == '__main__':
    app.run()
