from flask import render_template
from flask import request
from flask import jsonify
import flask as flask
from flask_cors import CORS, cross_origin
from flaskexample import app


@app.route('/')
@app.route('/index')
def index():

    return render_template('master.html')

@app.route('/go')
def go():

    query = request.args.get('query', '')

    return render_template(

        'go.html',

        query=query,

    )

@app.route('/chatbot', methods=['POST','GET','OPTIONS', 'PUT'])
def chatbot():

    if request.method == 'OPTIONS':
        
        response = flask.make_response()

        response.headers['Access-Control-Allow-Origin'] = '*'

        response.headers['Access-Control-Allow-Headers'] = '*'

        response.headers['Access-Control-Allow-Methods'] = '*'

        return response

    else:

        var = request.json['passValue']

        var = str(var) + ' extravaganza!'

        response = flask.Response("You have connected to dan's " + var)

        return response


