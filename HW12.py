#!/usr/bin/env python

"""
Created on Thursday Nov 20 2019
@author: Vikas Bhat
Homework12

"""

from flask import Flask, render_template
import sqlite3
app = Flask(__name__)


@app.route('/instructor_courses')
def instructor_courses():
    db_file = "810_startup.db"

    try:
        db = sqlite3.connect(db_file)
    except sqlite3.OperationalError:
        return f"Database Error at: {db_file}"

    else:
        query =  """SELECT InstructorCWID, Name, Dept, Course, count(*) as Students
                    from instructors join grades
                    on instructors.CWID = grades.InstructorCWID
                    group by instructors.Name, grades.Course
                    order by InstructorCWID; """

        data1 = [{'CWID': CWID, 'Name': Name, 'Dept': Dept, 'Course': Course, 'Students': Students}
            for CWID, Name, Dept, Course, Students in db.execute(query)]

        print(data1)
        db.close()

        return render_template('instructor_courses.html', title= "Stevens Repo", table_title= "Instructor information", instructors = data1)


if __name__ == '__main__':
    app.run(debug=True)
