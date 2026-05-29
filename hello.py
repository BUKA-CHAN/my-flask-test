from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

# =============================================================
# 【核心修改：把 Exercise 48 直接搬到首頁！】
# 網址後面什麼都不用加，直接進根目錄 "/"
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    
    # 當使用者輸入數字並按下 Submit（POST 請求）
    if request.method == "POST":
        # 抓取表單數值並翻倍計算
        input_number = int(request.form["x"])
        result = input_number * 2
        
    # 直接渲染 index.html，不論是初次進入還是顯示結果
    return render_template("index.html", result=result)
# =============================================================


# 【其餘房間保持不變，想參觀再加路徑即可】
# Exercise 45 的房間
@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {escape(username)}"

# Exercise 46 的房間
@app.route("/home")
def home_page():
    return render_template("home.html")

# Exercise 47 的房間
@app.route("/page/app")
def show_variables():
    x = {"name": "John", "age": 30, "city": "New York"}
    return render_template("page.html", user_info=x)
