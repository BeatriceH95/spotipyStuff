from app import app

import flask

from shelljob import proc


@app.route('/')
@app.route('/index')
def index():
	return "Hello world"


@app.route( '/stream' )
def stream():
    g = proc.Group()
    p = g.run( [ "bash", "-c", "for ((i=0;i<100;i=i+1)); do echo $i; sleep 1; done" ] )

    def read_process():
        while g.is_pending():
            lines = g.readlines()
            for proc, line in lines:
                yield line

    return flask.Response( read_process(), mimetype= 'text/plain' )
