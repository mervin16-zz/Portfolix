from flask import Flask, render_template as HTML
import app.resume as resume_bprint

# The Flask App
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
    instance_relative_config=True,
)

# Register Blueprints
app.register_blueprint(resume_bprint.resume, url_prefix="/resume")


# Error 404 Handler
@app.errorhandler(404)
def page_not_found(e):
    return HTML("404.html")
