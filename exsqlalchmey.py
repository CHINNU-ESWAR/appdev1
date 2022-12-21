import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table,Column,Integer,String,ForeignKey
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
#we need to define the class to make models for each table
Base=declarative_base()
#models for the tables
class Student(Base):
  __tablename__="student"
  student_id=Column(Integer,autoincrement=True,primary_key=True)
  student_name=Column(String,unique=True)
  student_mail=Column(String,umique=True)
class Course(Base):
  __tablename__="course"
  course_id=Column(Integer,autoincrement=True,primary_key=True)
  course_name=Column(String,unique=True)
engine=create_engine("sqlite:///./exdatabase.sqlite3")
if __name__=="__maim__":
  stmt=select(student)
  print(stmt)
  with engine.connect() as conn:
    for row in conn.exceute(stmt):
      print(row)
