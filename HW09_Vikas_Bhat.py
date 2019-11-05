#!/usr/bin/env python

"""
Created on Wed Oct 30 2019
@author: Vikas Bhat
Homework9

"""

from prettytable import PrettyTable
from collections import defaultdict
import os


class StevensRepository:
    """Student, grades & instructors data"""

    def __init__(self, path):
        self.path = path
        try:
            os.chdir(self.path)
        except FileNotFoundError:
            raise FileNotFoundError("Wrong Path")

        self.student_info = {}
        self.instructor_info = {}
        self.student_grades = defaultdict(lambda: defaultdict(str))
        self.instructor_Courses = defaultdict(lambda: defaultdict(str))

    def student_repository(self):

        file = "students.txt"
        try:
            fp = open(file, 'r')
        except FileNotFoundError:
            return "Not able to open this file"
        with fp:
            "Checking if file is not empty"
            if os.stat(file).st_size != 0:
                lines = fp.readlines()
                for i in lines:
                    values = i.strip().split("\t")
                    "The length of values should be less than 3 which as we can see in student.txt"
                    if len(values) != 3:
                        raise IOError("Wrong File")
                    student_values = StudentInfo(values[0], values[1], values[2], {})
                    cwid, name, dept, course_grade = student_values.student()
                    self.student_info[cwid] = self.student_info.get(cwid, [name, dept, course_grade])
                    if not self.student_info:
                        raise IOError("Not a valid student")
            else:
                return "File is empty"

    def instructor_repository(self):

        file = "instructors.txt"
        try:
            fp = open(file, 'r')
        except FileNotFoundError:
            return "Not able to open this file"
        with fp:
            "Checking if file is not empty"
            if os.stat(file).st_size != 0:
                lines = fp.readlines()
                for i in lines:
                    values = i.strip().split("\t")
                    "The length of values should be less than 3 which as we can see in instructors.txt"
                    if len(values) != 3:
                        raise IOError("Wrong File")
                    instructor_values = InstructorInfo(values[0], values[1], values[2], {})
                    cwid, name, dept, course_student_count = instructor_values.instructor()
                    self.instructor_info[cwid] = self.instructor_info.get(cwid, [name, dept, course_student_count])
            else:
                raise IOError("Not a valid instructor")

    def grades_repository(self):

        file = "grades.txt"
        try:
            fp = open(file, 'r')
        except FileNotFoundError:
            return "Not able to open this file"
        with fp:
            "Checking if file is not empty"
            if os.stat(file).st_size != 0:
                lines = fp.readlines()
                for i in lines:
                    self.student_grades.clear()
                    self.instructor_Courses.clear()
                    values = i.strip().split("\t")
                    "checking the length of values"
                    if len(values) != 4:
                        raise IOError("Wrong File")
                    for student_key, student_value in self.student_info.items():
                        if student_key == values[0]:
                            student_value[2][values[1]] = student_value[2].get(values[1], "") + values[2]
                    for instructor_key, instructor_value in self.instructor_info.items():
                        if instructor_key == values[3].strip():
                            instructor_value[2][values[1]] = instructor_value[2].get(values[1], 0) + 1
            else:
                raise IOError("Invalid grades")

    def pretty_table(self):
        "Table one for students record"
        student_table = PrettyTable(field_names=['CWID', 'Name', 'Completed Courses'])
        for i in self.student_info:
            student_course_record = []
            name, major, student_course_record_dict = self.student_info[i]
            for key, value in student_course_record_dict.items():
                student_course_record.append(key)
            student_table.add_row([i, name, student_course_record])
        print(student_table)

        "Table two for instructors record"
        instructor_table = PrettyTable(field_names=['CWID', 'Name', 'Dept', 'Course', 'Students'])
        for i in self.instructor_info:
            courses_amount = []
            students_amount = []
            name, major, instructor_course_record_dict = self.instructor_info[i]
            for key, value in instructor_course_record_dict.items():
                courses_amount.append(key)
                students_amount.append(value)
            if not courses_amount:
                continue
            else:
                if len(students_amount)> 1:
                    for instructor_key, instructor_value in zip(courses_amount, students_amount):
                        instructor_table.add_row([i, name, major, instructor_key, instructor_value])
                else:
                    instructor_table.add_row([i, name, major, instructor_key, students_amount])

        print(instructor_table)


class StudentInfo:

    def __init__(self, cwid, name, major, course_dict):
        self.cwid = cwid
        self.name = name
        self.major = major
        self.course_dict = course_dict

    def student(self):
        return [self.cwid, self.name, self.major.strip(), self.course_dict]


class InstructorInfo:

    def __init__(self, cwid, name, major, students_dict):
        self.cwid = cwid
        self.name = name
        self.major = major
        self.students_dict = students_dict

    def instructor(self):
        return [self.cwid, self.name, self.major, self.students_dict]


"""
Pleas uncomment the below code to print pretty table
"""



def main():
    try:
        table = StevensRepository("/Users/vikasbhat/Desktop/SSdW_asdsadasdHW09")
        result_students = table.student_repository()
        if result_students is not None:
            print(result_students)
        result_instructors = table.instructor_repository()
        if result_instructors is not None:
            print(result_instructors)
        result_grades = table.grades_repository()
        if result_grades is not None:
            print(result_grades)

        table.pretty_table()

    except FileNotFoundError:
        print("Wrong file direcotory")


if __name__ == '__main__':
    main()



