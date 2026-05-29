from flask import Flask, render_template
app = Flask(__name__)

# 👈 將原本的 "Index Page" 修改為 "Hello, World!" 以符合 Exercise 44 要求
@app.route("/")
def hello():
    return "Hello, World!" 

@app.route("/exercise42")
def show_variables():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return render_template("page.html", user_info=x)
