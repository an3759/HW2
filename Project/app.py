from flask import Flask
from controller import hello_bp

# 初始化網頁伺服器實體
app = Flask(__name__)

# 註冊路由控制器
app.register_blueprint(hello_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)