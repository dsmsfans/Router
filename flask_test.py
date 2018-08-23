from flask import Flask

# 初始化 Flask 類別成為 instance
app = Flask(__name__)
# 路由和處理函式配對
@app.route('/')
def index():
    return 'Hello World!'
@app.route('/home')
def home():
    return 'Home'
# 判斷自己執行非被當做引入的模組，因為 __name__ 這變數若被當做模組引入使用就不會是 __main__
if __name__ == '__main__':
    app.run()

