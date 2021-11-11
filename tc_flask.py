from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
	homepage = "<h1>410917504 資管二B 梁實翔</h1>"
    homepage += "<a href=/aboutme>MIS工作</a><br>"
    return homepage

@app.route("/aboutme")
def mis2b():
	return render_template("aboutme.html")

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/current")
def current():
    now = datetime.now()
    return render_template("current.html", datetime = str(now))

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)

@app.route('/hi')
def hi():
    # 載入原始檔案
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # 計數加1
    count += 1

    # 覆寫檔案
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()
    return ("本網站總拜訪人次："+str(count))

if __name__ == "__main__":
    app.run()