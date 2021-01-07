from flask import Blueprint, render_template as HTML
import app.helpers.utils as Utils

# This is the Blueprint for the whole Resume page
# All links are related to ://url/resume
resume = Blueprint(
    "resume", __name__, static_folder="static", template_folder="templates"
)

################################################
################## Home Route ##################
################################################


@resume.route("/")
def index():
    return HTML("index.html", age=Utils.get_age())


#################################################
################ Porfolio Routes ################
#################################################


@resume.route("/ansible-automation")
def ansible_automation():
    return HTML("ansible.html")


@resume.route("/checkpoint-automation")
def checkpoint_automation():
    return HTML("checkpoint.html")


@resume.route("/locky")
def locky():
    return HTML("locky.html")


@resume.route("/mes")
def mes():
    return HTML("mes.html")


@resume.route("/mesg")
def mesg():
    return HTML("mesg.html")


@resume.route("/fortweet")
def fortweet():
    return HTML("fortweet.html")


@resume.route("/th3pl4gu3")
def th3pl4gu3():
    return HTML("th3pl4gu3.html")


@resume.route("/prometheus")
def prometheus():
    return HTML("prometheus.html")
