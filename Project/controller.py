from flask import Blueprint, jsonify
from datetime import datetime
from greeting import Greeting  # 引入定義的資料結構

# 建立一個藍圖，名稱叫 'hello'
hello_bp = Blueprint('hello_controller', __name__)

@hello_bp.route('/hello', methods=['GET'])
def hello():
    # 1. 產生資料物件
    greeting_object = Greeting(
        message="Hello, GitHub Actions! I'm broken.",
        generatedAt=datetime.utcnow().isoformat() + "Z"
    )
    
    # 2. 轉換成網頁 JSON 格式回傳
    return jsonify({
        "message": greeting_object.message,
        "generatedAt": greeting_object.generatedAt
    })