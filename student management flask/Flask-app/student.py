import sqlite3


from flask_restful import Resource, reqparse


db_location = "data.db"

class Students(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('fees',
        type= float ,
        required=True,
        help="This field cannot be left empty!"
    )
    parser.add_argument('clg',
                        type=str,
                        required=True,
                        help="This field cannot be left empty!"
                        )
    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect(db_location)
        cursor = connection.cursor()

        query = "SELECT * FROM student WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            return row

    @classmethod
    def insert_student(cls, student):
        connection = sqlite3.connect(db_location)
        cursor = connection.cursor()
        query = "INSERT INTO student VALUES (?, ?,?)"
        cursor.execute(query, (student['name'],  student['fees'], student['clg']))
        connection.commit()
        connection.close()

    @classmethod
    def update_student(cls, student):
        connection = sqlite3.connect(db_location)
        cursor = connection.cursor()
        query = "UPDATE student SET fees=? WHERE name=?"
        cursor.execute(query, (student['name'], student['fees']))
        connection.commit()
        connection.close()


    def post(self, name):
        if Students.find_by_name(name):
            return {'message': "An student with name '{}' already exists".format(name)}, 400
        data = Students.parser.parse_args()
        student = {
            'name': name,
            'fees': data['fees'],
            'clg': data['clg']

        }
        try:
            Students.insert_student(student)
        except:
            return {"message": "Error Occured inserting student"}, 500

        return student, 201


    def get(self, name):
        student = Students.find_by_name(name)
        if student:
            response = {"student": {
                'name': student[0],
                'fees': student[1],
                'clg': student[2]
            }}
            return response, 200

        response = {
            "message": "student Not Found"
        }
        return response, 400


    def put(self, name):
        data = Students.parser.parse_args()

        student = Students.find_by_name(name)
        updated_student = {
                'name': name,
                'fees': data['fees'],
                'clg': data['clg']
            }
        if student is None:
            try:
                Students.insert_student(updated_student)
            except:
                return {"message": "Error Occured inserting Student"}, 500
        else:
            try:
                Students.update_student(updated_student)
            except:
                return {"message": "Error Occured Updating Student"}, 500

        return updated_student, 201

    def delete(self, name):
        connection = sqlite3.connect(db_location)
        cursor = connection.cursor()
        query = "DELETE FROM student WHERE name=?"
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()

        return {'message': 'student Deleted'}, 201

class StudentsList(Resource):

    def get(self):
        connection = sqlite3.connect(db_location)
        cursor = connection.cursor()
        query = "SELECT * FROM student"
        result = cursor.execute(query)

        students= []
        for row in result:
            students.append({
                'name': row[0],
                'fees': row[1],
                'clg': row[2]
            })

        connection.commit()
        connection.close()

        return {'students': students}, 200