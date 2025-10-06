from flask import Flask, render_template, request, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import os
from dotenv import load_dotenv
import smtplib


class Form(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    subject = StringField('subject', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email()])
    message = StringField('message', validators=[DataRequired(), Length(max=500)])


app = Flask(__name__)

load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')


@app.route('/', methods=['GET', 'POST'])
def home():
    contact_form = Form()
    if contact_form.validate_on_submit():
        name = contact_form.name.data
        email = contact_form.email.data
        subject = contact_form.subject.data
        message = contact_form.message.data
        user = os.getenv("FROM_EMAIL")
        password = os.getenv("FROM_EMAIL_PASSWORD")
        to_adr = os.getenv("TO_EMAIL")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=user, password=password)
            connection.sendmail(from_addr=user, to_addrs=to_adr, msg=f"Subject:{subject}\n\n{message}\n"
                                                                     f"This massage is from user:{name} with email of:"
                                                                     f"{email}")
            flash("Your message have sent successfully!")
            return redirect('/#contact')

    elif request.method == 'POST':
        flash("Please fill the form Correctly")
        return redirect('/#contact')
    else:
        return render_template('index.html', form=contact_form)



@app.route('/starter')
def starter():
    return render_template("starter-page.html")


@app.route('/portfolio')
def portfolio():
    return render_template("portfolio-details.html")


if __name__ == "__main__":
    app.run(debug=True)
