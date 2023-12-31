from flask import Blueprint, render_template

app_projects = Blueprint('projects', __name__,
                url_prefix='/projects',
                template_folder='templates/bp_projects/')

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/AWSDeployment/')
def portfolio():
    return render_template("aws.html")

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")

@app_projects.route('/walruses/')
def walruses():
    return render_template("walruses.html")

@app_projects.route('/apis/')
def hawkers():
    return render_template("apis.html")