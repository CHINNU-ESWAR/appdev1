import os
from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(current_dir, "exdatabase.sqlite3")
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()


class STUDENT(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    student_name = db.Column(db.String, unique=True)
    student_mail = db.Column(db.String, unique=True)


class COURSE(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    course_name = db.Column(db.String, unique=True)
    course_description=db.Column(db.String)
    students =db.relationship("STUDENT",secondary="student_course")


class STUDENTCOURSE(db.Model):
    __tablename__ = 'student_course'
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), primary_key=True, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), primary_key=True, nullable=False)


@app.route('/', methods=['GET', 'POST'])
def courses():
    courses = COURSE.query.all()
    return render_template('courses.html',courses=courses)

@app.route('/courses_by/<student_name>',methods=['GET','POST'])
def courses_by_student(student_name):
    courses=COURSE.query.filter(COURSE.students.any(student_name=student_name))
    return render_template("courses_by_student.html",courses=courses,student_name=student_name)
if __name__ == "__main__":
    app.run(
        host='0.0.0.0', debug=True, port=8080)
