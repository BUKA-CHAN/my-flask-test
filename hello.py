from flask import Flask, render_template
from markupsafe import escape  # 👈 引入安全防護，避免網址惡意腳本攻擊

app = Flask(__name__)

# 【Exercise 44 的房間】首頁依舊在原地，顯示 Hello, World!
@app.route("/")
def hello():
    return "Hello, World!"

# 【Exercise 45 的全新房間】動態網址功能
# <username> 代表這是一個會變動的變數
@app.route("/user/<username>")
def show_user_profile(username):
    # 網址輸入什麼名字，username 就會帶入什麼名字
    return f"User {escape(username)}"

# 【預留先前的房間】Exercise 42 的變數顯示網頁
@app.route("/exercise42")
def show_variables():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return render_template("page.html", user_info=x)
