from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')
# 블루 프린트 객체 생성

@bp.route('/hello')
def hello_pybo():
    return 'Hello, pybo!'

@bp.route('/')
def index():
    return 'Pybo index'