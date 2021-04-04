## this is for study

""" 文件内容组成：
1. 创建基础 app 对象
2. 注册蓝图
3. 定义基本router
4. 定期server启动参数
"""

from flask import Flask , jsonify ## 导入Flask
from libs.base_fun import make_response  ## 导入基础方法
from datetime import datetime 

from apps import app_bp  ## 导入蓝图
app = Flask(__name__)  ## 生成APP 对象

## 注册蓝图
app.register_blueprint(app_bp, url_prefix='/apps')  ## 注册蓝图到 app

# 各种路由
@app.route("/")
def hello_world():
    return "hello tuotuo"

@app.route("/name")
def return_name():
    return "my name is tuotuo"

@app.route("/healthz")
def health_check():
    # return jsonify({
    #                 "code": 200,
    #                 "data": "healthy"
    #                 })
    data = {
        "action": "health check",
        "test": "tttt"
    }
    message = "this is only for health check "
    response = make_response(200,data,message)  ## return json格式 data

    return response

##请求前必须执行的段
@app.before_request
def before_check():
    print(f"this is before request ,time is {datetime.now()}")

#访问后必须执行的段
## 这里函数是截取请求返回的response，在这里可以做处理或其他
@app.after_request
def after_request(response):
    print(f"this is after  request ,time is {datetime.now()}")
    print(f"{response.headers}")
    print(response.data)
    return response
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=9527)  ## 启动方法及参数
