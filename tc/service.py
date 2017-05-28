#!/usr/bin/env python3
import flask  # Flask, request
import flask_restful  # Resource, Api

class Root(flask_restful.Resource):
    def get(self):
        return {'name': 'Root', 'value': 0 }

class Dept(flask_restful.Resource):
    def get(self, attr_name):
        result = {'attribute': attr_name}
        return result
 
class TodoSimple(flask_restful.Resource):
    todos = {}
    def get(self, todo_id):
        return {todo_id: self.todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: self.todos[todo_id]}

def main(argv):
    """Example rest service."""
    exit_code = 0
    app = flask.Flask(__name__)
    api = flask_restful.Api(app)

    api.add_resource(Root, '/root')
    api.add_resource(Dept, '/dept/<string:attr_name>')
    api.add_resource(TodoSimple, '/<string:todo_id>')

    app.run(debug=True)
    return exit_code

if __name__ == '__main__':
    sys.exit(main(sys.argv))
