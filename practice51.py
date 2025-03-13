from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField()
    phone = IntegerField()
    name = StringField()
    address = StringField()
    index = IntegerField()
    comment = StringField()


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data
        name, index = form.name.data, form.index.data
        if not email:
            return "Invalid email", 400
        if not phone:
            return f"Invalid phone", 400
        if not name:
            return f"Invalid name", 400
        if not index:
            return f"Invalid index", 400
        return f"Successfully registered user {email} with phone +7{phone}"


    return f"Invalid input, {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
