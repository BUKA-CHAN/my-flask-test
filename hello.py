from flask import Flask, render_template
app = Flask(__name__)

# 👈 補上這個根目錄路由，首頁就不會再跳 404 Not Found 了！
@app.route("/")
def index():
    return "Index Page" 

# 這是先前 Exercise 42 的變數傳遞路由
@app.route("/exercise42")
def show_variables():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return render_template("page.html", user_info=x)
