from flask import Blueprint

#创建主蓝本
main = Blueprint('main',__name__)

#相对导入， '.'表示当前包，即main/
from .import views,errors