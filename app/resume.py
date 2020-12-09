from flask import Blueprint, render_template as HTML

# This is the Blueprint for the whole Resume page
# All links are related to ://url/resume
resume = Blueprint(
    "resume", __name__, static_folder="static", template_folder="templates"
)

############################################
################## Routes ##################
############################################


@resume.route("/")
def index():
    return HTML("index.html")


@resume.route("/portfolio")
def portfolio():
    return HTML("portfolio.html")
