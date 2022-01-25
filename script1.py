from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/weather/')
def weather():
    return render_template("project.html")

@app.route('/foliummap/')
def foliummap():
    return render_template("mapkathmandu.html")

if __name__=="__main__":
    app.run(debug=True)
