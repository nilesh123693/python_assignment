from flask import Flask
from flask_restful import Api
from student import Students, StudentsList

app = Flask(__name__)
api = Api(app)

api.add_resource(Students, '/student/<string:name>')
api.add_resource(StudentsList, "/students")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
