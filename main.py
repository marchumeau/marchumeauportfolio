import data

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", data=data.setup())

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/project1')
def project1():
    return render_template("project1.html", data=data.proj1())

@app.route('/github')
def github():
    return render_template("github.html")

@app.route('/jinja')
def jinja():
    posts=[{'title':'New Species of Bird Found in Africa', 'author':'Marc Humeau'},
           {'title':'New Source of Renewable Energy Found','author':'Marc Humeau'}]
    return render_template("jinja.html", hot=False, name="Marc Humeau", posts = posts)
                        #conditional statement in jinja

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)