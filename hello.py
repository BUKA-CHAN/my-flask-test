from flask import Flask, render_template, request  # 👈 注意這裡引入了 request
from markupsafe import escape

app = Flask(__name__)

# 【Ex 44 房間】首頁依舊在原地
@app.route("/")
def hello():
    return "Hello, World!"

# 【Ex 45 房間】動態網址功能
@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {escape(username)}"

# 【Ex 46 房間】載入獨立 HTML 範本
@app.route("/home")
def home_page():
    return render_template("home.html")

# 【Ex 47 房間】變數顯示網頁
@app.route("/page/app")
def show_variables():
    x = {"name": "John", "age": 30, "city": "New York"}
    return render_template("page.html", user_info=x)

# -------------------------------------------------------------
# 【全新加入：Exercise 48 的綜合房間】
# 允許 GET（單純進網頁看輸入框）與 POST（按下按鈕把數字送給 Python）
@app.route("/predict", methods=["GET", "POST"])
def predict():
    result = None
    
    # 如果使用者是按下了 Submit 按鈕（POST 請求）
    if request.method == "POST":
        # 1. 從網頁表單中抓取名為 "x" 的輸入框數值，並強制轉換成整數 (int)
        input_number = int(request.form["x"])
        
        # 2. 進行題目要求的「翻倍」計算
        result = input_number * 2
        
    # 3. 渲染 index.html，並把計算結果（如果是 GET 進來就是 None）傳給前端
    return render_template("index.html", result=result)
