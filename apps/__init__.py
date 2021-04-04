from flask import Blueprint
app_bp = Blueprint('app_bp',__name__)  ## 生成蓝图

from .views import *  ## 导入此蓝图的所有view