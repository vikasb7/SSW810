#!/usr/bin/env python

"""
Created on Thursday Nov 13 2019
@author: Vikas Bhat
Homework11

"""
import os
from collections import defaultdict
from prettytable import PrettyTable
import sqlite3


class StevensRepository:
    """ class Repository to hold the students, instructors and grades for a single University """

    def file_reading_gen(path, fields, sep=',', header=False):
        """ Generator function to read file line by line """
        try:
            fp = open(path, 'r')
        except FileNotFoundError:
            raise FileNotFoundError(f"Unable to open {path}")
        else:
            with fp:
                for n, line in enumerate(fp):
                    line = line.strip('\n')
                    line = line.split(sep)
                    if len(line) != fields:
                        raise ValueError(f" Invalid values as expected values are :  {fields}")
                    # no need to take the headings skipping the first line
                    elif n == 0 and header is False:
                            continue
                    else:
                        yield tuple(line)

    def __init__(self, dir_path):



        self._dir_path = dir_path

        self.studentsInfo = {}
        self.instructorsInfo = {}
        self.majorsInfo = {}

        self.majors_repo()
        self.students_repo()
        self.instructors_repo()
        self.grades_repo()

        self.majors_disp()
        self.students_dsip()
        self.instructors_disp()

        self.instructor_table_db()

    def students_repo(self):
        path = os.path.join(self._dir_path, 'students.txt')

        try:
            # generating tuple of values from students
            for cwid, name, major in StevensRepository.file_reading_gen(path, 3, '\t', False):
                    major = self.majorsInfo[major]
                    self.studentsInfo[cwid] = Student(cwid, name, major)

        except FileNotFoundError:
            print(f"Unable to open {path}")

        except ValueError:
            print(f" Invalid values as expected values are :  {fields}")

    def instructors_repo(self):
        path = os.path.join(self._dir_path, 'instructors.txt')

        try:
            # generating tuple of values from instructors
            for cwid, name, department in StevensRepository.file_reading_gen(path, 3, '\t', False):
                    self.instructorsInfo[cwid] = Instructor(cwid, name, department)

        except FileNotFoundError:
            print(f"Unable to open {path}")

        except ValueError:
            print(f" Invalid values as expected values are :  {fields}")

    def grades_repo(self):
        path = os.path.join(self._dir_path, 'grades.txt')

        try:
            # generating tuple of values from grades
            for student_cwid, course, grade, instructor_cwid in StevensRepository.file_reading_gen(path, 4, '\t', False):
                    student = self.studentsInfo[student_cwid]
                    student.new_grades(course, grade)

                    instructor = self.instructorsInfo[instructor_cwid]
                    instructor.increment_course(course)

        except FileNotFoundError:
            print(f"Unable to open {path}")

        except ValueError:
            print(f" Invalid values as expected values are :  {fields}")

    def majors_repo(self):
        path = os.path.join(self._dir_path, 'majors.txt')

        try:
            # generating tuple of values from major
            for major, req, course in StevensRepository.file_reading_gen(path, 3, '\t', False):
                if major not in self.majorsInfo:
                    self.majorsInfo[major] = Major(major)
                self.majorsInfo[major].new_course(req, course)

        except FileNotFoundError:
            print(f"Unable to open {path}")

        except ValueError:
            print(f" Invalid values as expected values are :  {fields}")

    def majors_disp(self):
        # generating pretty table for majors
        pt = PrettyTable(Major.field_names)

        for major in self.majorsInfo.values():
            pt.add_row(major.attributes())
        print(pt)

    def students_dsip(self):
        # generating pretty table for students
        pt = PrettyTable(Student.field_names)

        for student in self.studentsInfo.values():
            pt.add_row(student.attributes())
        print(pt)

    def instructors_disp(self):
        # generating pretty table for instructors
        pt = PrettyTable(Instructor.field_names)

        for instructor in self.instructorsInfo.values():
            for course in instructor.attributes():
                pt.add_row(course)
        print(pt)

    def instructor_table_db(self):
        db_file = "810_startup.db"
        stevens_db = sqlite3.connect(db_file)

        query = """select CWID, Name, Dept, Course, count(Course)
                    from instructors join grades
                    on CWID = InstructorCWID
                    group by course, InstructorCWID """

        pt = PrettyTable(Instructor.field_names)

        for row in stevens_db.execute(query):
            pt.add_row(row)

        print(pt)



class Student:
    # attributes for field names for the pretty table

    field_names = ['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required', 'Remaining Electives']

    def __init__(self, cwid, name, major):
        self._cwid = cwid
        self._name = name
        self._major = major
        self._grade_dict = defaultdict(str)

    def new_grades(self, course, grade):
        self._grade_dict [course] = grade

    def attributes(self):
         # fields as a list
        return [self._cwid,self._name, self._major.name(), sorted(self._grade_dict .keys()),
                self._major.required_courses_summary(self._grade_dict ), self._major.elective_courses_summary(self._grade_dict)]


class Instructor:
    # attributes for field names for the pretty table

    field_names = ['CWID', 'Name', 'Dept', 'Course', 'Students']

    def __init__(self, cwid, name, department):
        self._cwid = cwid
        self._name = name
        self._department = department
        self._courses_dict = defaultdict(int)

    def increment_course(self, course):
        # number of students in the course
        self._courses_dict[course] += 1

    def attributes(self):
        for course, students in self._courses_dict.items():
            # fields as a list
            yield [self._cwid, self._name, self._department, course, students]


class Major:
    # attributes for field names for the pretty table
    field_names = ['Dept', 'Required', 'Electives']

    def __init__(self, name):
        self._name = name
        # no duplicates
        self._required = set()
        self._elective = set()

    def new_course(self, req, course):
        #required
        if req.lower() == 'r':
            if course in self._required:
                print("This Course is already existing")
            else:
                self._required.add(course)

        elif req.lower() == 'e':
            # electives
            if course in self._elective:
                print("This elective is already existing")
            else:
                self._elective.add(course)

    def required_courses_summary(self, course_info):
        courses_cleared = set()

        for course, grade in course_info.items():
            # passing grades
            if grade.lower() in ['a', 'a-', 'b+', 'b', 'b-', 'c+', 'c']:
                courses_cleared.add(course)
        # other
        courses_left = self._required - courses_cleared

        return sorted(courses_left)

    def elective_courses_summary(self, course_info):
        courses_cleared = set()

        for course, grade in course_info.items():
            # passing grades
            if grade.lower() in ['a', 'a-', 'b+', 'b', 'b-', 'c+', 'c']:
                if course in self._elective:
                    return None
                else:
                    courses_cleared.add(course)
        # other
        courses_left = self._elective - courses_cleared

        return sorted(courses_left)

    def attributes(self):

        # list for printing pretty table
        return [self._name, sorted(self._required), sorted(self._elective)]

    def name(self):
        # major names for table
        return self._name


def main():
    StevensRepository('/Users/vikasbhat/Documents/SSW 810')


if __name__ == '__main__':
    main()
