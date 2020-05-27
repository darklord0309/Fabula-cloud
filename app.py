from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('id', type=int)

todos = [
  {
    "id": 1,
    "name":"mano1",
    "item": "Create sample app",
    "status": "Completed"
  },
  {
    "id": 2,
    "name":"mano2",
    "item": "Deploy in Heroku",
    "status": "Open"
  },
  {
    "id": 3,
    "name":"mano3",
    "item": "Publish",
    "status": "Open"
  }
]

class Todo(Resource):
  def get(self):
    args = parser.parse_args()
    id = args['id']
    name = args['name']
    for todo in todos:
      if(id == todo["id"] and name == todo["name"]):
        return todo, 200
    return "Item not found for the id: {}".format(id), 404

    def put(self, id):
      for todo in todos:
        if(id == todo["id"]):
          todo["item"] = request.form["data"]
          todo["status"] = "Open"
          return todo, 200
      return "Item not found for the id: {}".format(id), 404




api.add_resource(Todo, "/item")




if __name__ == "__main__":
  app.run()
