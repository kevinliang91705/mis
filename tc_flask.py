from flask import Flask,render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
	homepage = "<h1>410917504 資管二B 梁實翔</h1>"
    homepage += "<a href=/mis>MIS工作</a><br>"
    return homepage

@app.route("/mis")
def course():
	return render_template("KEVIN.html")



if __name__ == "__main__":
    app.run()
