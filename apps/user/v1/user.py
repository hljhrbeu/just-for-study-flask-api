from apps import app_bp as app_user_v1 
from libs.base_fun import make_response

@app_user_v1.route("/user/",methods = ["GET"])
def user_index():
    return make_response(200, {"page": "home"},"welcome to user page")