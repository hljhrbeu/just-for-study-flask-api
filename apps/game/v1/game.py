from apps import app_bp as app_game_v1  ## 导入蓝图并向次蓝图中添加URL
from libs.base_fun import make_response

@app_game_v1.route("/game/")
def hello_game():
    return make_response(code = 2002, data = {"from": "game","result": True}, message = "good"
    )
 