from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
#parser.add_argument('class', type=list)
parser.add_argument('id', type=int)

todos = [
  {
    "id": 1,
    "name":"mano",
    "item": "Create sample app",
    "status": "Completed"
  },
  {
    "id": 2,
    "name":"mano",
    "item": "Deploy in Heroku",
    "status": "Open"
  },
  {
    "id": 3,
    "name":"mano",
    "item": "Publish",
    "status": "Open"
  }
]

class Todo(Resource):
  def get():
    args = parser.parse_args()
    id = args['id']
    for todo in todos:
      if(id == todo["id"]):
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
