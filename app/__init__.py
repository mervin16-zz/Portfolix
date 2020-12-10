from flask import Flask, render_template as HTML, redirect, request, url_for
from flask_mail import Mail, Message
import app.helpers.utils as Utils
import app.resume as resume_bprint
import os

# The Flask App
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
    instance_relative_config=True,
)

# Register Blueprints
app.register_blueprint(resume_bprint.resume, url_prefix="/resume")

# SMTP Settings
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USERNAME"] = os.environ["MAIL_USERNAME"]
app.config["MAIL_PASSWORD"] = os.environ["MAIL_PASSWORD"]
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False

# Create a mail object
mail = Mail(app)

# Error 404 Handler
@app.errorhandler(404)
def page_not_found(e):
    return HTML("404.html")


# Redirect to the correct resume page
@app.route("/")
def resume():
    return redirect(url_for("resume.index"))


# Send mail from contact form
@app.route("/send-email", methods=["POST"])
def send_email():

    try:
        sender_email = request.form["email"]

        # Email validity check
        if not Utils.validate_email(sender_email):
            return (
                "Please enter a valid email",
                200,
            )

        msg = Message(
            request.form["message"],
            sender=sender_email,
            recipients=os.environ["MAIL_RECIPIENTS"].split(","),
        )
        msg.body = request.form["message"]
        msg.subject = f"{request.form['name']} :: {request.form['subject']}"
        mail.send(msg)
    except Exception as e:
        return (
            'Unfortunately, your message couldn\'t be submitted right now. Please contact me directly on <a href="mailto:mervinhemaraju16@gmail.com">mervinhemaraju16@gmail.com</a>.',
            200,
        )

    # Returns a no content status code
    # because the user doesn't need to get away
    # from current page
    return "OK", 200

