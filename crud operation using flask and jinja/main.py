import sqlite3

from flask import*

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/add')
def add():
    return render_template("add.html")

@app.route('/savedetails', methods =["POST","GET"])
def savedetails():
     msg = "msg"
     if request.method=="POST":
         try:
             rollno = int(request.form["rollno"])
             name = request.form["name"]
             email = request.form["email"]
             clg = request.form["clg"]
             fees = int(request.form["fees"])
             with sqlite3.connect("student.db") as con:
                  cur = con.cursor()
                  cur.execute("insert into students values(?,?,?,?,?)",(rollno,name,email,clg,fees))
                  con.commit()
                  msg = "record added sucessfully"
         except:
           con.rollback()
           msg = "failed to add student"
         finally:
              return render_template("sucess.html", msg = msg)
              con.close()

@app.route('/delete')
def delete():
     return render_template("delete.html")

@app.route('/deleterecord', methods = ["POST"])
def deleterecord():
    rollno = request.form["rollno"]
    with sqlite3.connect("student.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from students where rollno = ?", rollno)
            con.commit()
            msg = "record deleted sucessfully"
        except:
            con.rollback()
            msg = "record not found"
        finally:
            return render_template("deleterecord.html", msg = msg)
            con.close()

@app.route('/view')
def view():
    con = sqlite3.connect("student.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from students")
    rows = cur.fetchall()
    return render_template("view.html", rows = rows)

if __name__ == '__main__':
    app.run(debug = True, port = 5000)