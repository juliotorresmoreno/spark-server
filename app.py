from train import context
from flask import Flask
from flask_restful import Resource, Api
from controllers.generic import Todo, TodoList
app = Flask(__name__)
api = Api(app)

context.inicialize()

@app.route("/")
def hello():
    return "Hello World!"

api.add_resource(TodoList, '/api/<string:collection>')
api.add_resource(Todo, '/api/<string:collection>/<string:id>')
