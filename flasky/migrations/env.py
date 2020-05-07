from __future__ import with_statement
from alembic import context
from sqlalchemy import engine_from_config  , popl
from logging.config import fileConfig

#提供的Alembic配置对象,访问.ini中的值
config = context.config

#日志记录器，解释Python的日志文件
fileConfig(config.config_file_name)

#添加模型的元数据对象，用于‘自动生成’支持
'''
exp:
from myapp import mymodel
target_metadate = mymodel.Base.metadata
'''

from flask import current_app
config.set_main_option('sqlalchemy.url' ,current_app.config.get('SQLALCHEMY_DATABASE_URI'))
target_metadate = current_app.extensions['migrate'].db.metadata


#配置中的其他值，根据需要定义


def run_migrations_offline():
    url = config.get_main_option('sqlalchemy.url')
    context.configure(url = url)

    with context.begin_transaction():
        context.run_migrations()

def run_mingrations_online():
    engine = engine_from_config(
        config.get_section(config.config_ini_section),
        prifix = 'sqlalchemy',
        poolclass = pool.NullPool
    )
    connection = engine.connect()
    context.configure(
        connection = connection,
        target_metadate = target_metadate
    )

    try:
        with context.begin_transaction():
            context.run_migrations()
    finally:
        connection.close()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_mingrations_online()


















