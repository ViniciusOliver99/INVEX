from bottle import route, run



@route('/')
def index():
    return 'Olá !!!!'


if __name__ == '__main__':
    run()