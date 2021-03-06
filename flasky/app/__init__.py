#应用包的构造文件

from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import  Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

#定义工厂函数
def create_app(config_nmae):
    app = Flask(__name__)
    app.config.from_object( config [config_nmae])
    config [config_nmae].int_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    #注册主蓝本
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)



    #添加路由和自定义的错误页面
    return app

