from flask import Flask, render_template
app = Flask(__name__)

@app.route("/exercise42")
def show_variables():
    # 教材第 32 頁指定的 Python 物件
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    
    # 使用 render_template，並把物件 x 當作參數傳給網頁（取名為 user_info）
    return render_template("page.html", user_info=x)