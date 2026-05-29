from flask import Flask, render_template
from markupsafe import escape # 👈 照教材第 16 頁引進安全防護
app = Flask(__name__)

# 房間 1：Exercise 44 的首頁 (你目前截圖的畫面)
@app.route("/")
def hello():
    return "Hello, World!"

# 房間 2：Exercise 42 的變數顯示網頁
@app.route("/exercise42")
def show_variables():
    x = {"name": "John", "age": 30, "city": "New York"}
    return render_template("page.html", user_info=x)

# 房間 3：【全新加入】Exercise 45 的網址代入名稱功能
@app.route("/user/<username>")
def show_user_profile(username):
    # 當瀏覽器輸入 /user/Jenny，畫面就會動態跑出 User Jenny
    return f"User {escape(username)}"
