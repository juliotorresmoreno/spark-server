

import json
from flask import request
from flask_restful import Resource

todos = {}

class Todo(Resource):
    def get(self, collection, id):
        if id in todos:
            return {id: todos[id]}
        return {}

    def put(self, collection, id):
        todos[id] = request.form['data']
        return {id: todos[id]}
    
    def delete(self, collection, id):
        return {}


class TodoList(Resource):
    def get(self, collection):
        return {"data":todos}
    
    def post(self, collection):
        return {}