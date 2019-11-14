#!/usr/bin/env python

"""
Created on Thursday Nov 13 2019
@author: Vikas Bhat
Homework11
Unit Testing
"""


import unittest
import sqlite3


from HW11_Vikas_Bhat import StevensRepository


class TestStevensRepository(unittest.TestCase):

    def test_repo(self):
        dir_path = '/Users/vikasbhat/Documents/SSW810'
        stevens = StevensRepository(dir_path)

        self.assertEqual(stevens._dir_path, dir_path)

        majors = dict()

        for name, major in stevens.majorsInfo.items():
            majors[name] = major.attributes()

        major_data = {
            'SFEN': [
                'SFEN',
                ['SSW 540', 'SSW 555', 'SSW 810'],
                ['CS 501', 'CS 546']
            ],
            'CS': [
                'CS',
                ['CS 546', 'CS 570'],
                ['SSW 565', 'SSW 810']
            ]
        }


        students = dict()

        for cwid, student in stevens.studentsInfo.items():
            students[cwid] = student.attributes()

        student_data = {
            '10103': [
                '10103',
                'Jobs, S',
                'SFEN',
                ['CS 501', 'SSW 810'],
                ['SSW 540', 'SSW 555'],
                None
            ],
            '10115': [
                '10115',
                'Bezos, J',
                'SFEN',
                ['CS 546', 'SSW 810'],
                ['SSW 540', 'SSW 555'],
                ['CS 501', 'CS 546']
            ],
            '10183': [
                '10183',
                'Musk, E',
                'SFEN',
                ['SSW 555', 'SSW 810'],
                ['SSW 540'],
                ['CS 501', 'CS 546']
            ],
            '11714': [
                '11714',
                'Gates, B',
                'CS',
                ['CS 546', 'CS 570', 'SSW 810'],
                [],
                None
            ]
        }

        instructors = dict()
        for cwid, instructor in stevens.instructorsInfo.items():
            # need to extra because of generator
            for course in instructor.attributes():
                cwid, name, dept, crs, num_students = course
                instructors[cwid, name, dept, crs] = course

        # create another dictionary based on the raw data
        instructor_data = {
            ('98764', 'Cohen, R', 'SFEN', 'CS 546'):
                ['98764', 'Cohen, R', 'SFEN', 'CS 546', 1],
            ('98763', 'Rowland, J', 'SFEN', 'SSW 810'):
                ['98763', 'Rowland, J', 'SFEN', 'SSW 810', 4],
            ('98763', 'Rowland, J', 'SFEN', 'SSW 555'):
                ['98763', 'Rowland, J', 'SFEN', 'SSW 555', 1],
            ('98762', 'Hawking, S', 'CS', 'CS 501'):
                ['98762', 'Hawking, S', 'CS', 'CS 501', 1],
            ('98762', 'Hawking, S', 'CS', 'CS 546'):
                ['98762', 'Hawking, S', 'CS', 'CS 546', 1],
            ('98762', 'Hawking, S', 'CS', 'CS 570'):
                ['98762', 'Hawking, S', 'CS', 'CS 570', 1]
        }

        instructors1 = dict()
        db_path = '/Users/vikasbhat/Documents/SSW810/810_startup.db'
        stevens_db = sqlite3.connect(db_path)

        query = """select CWID, Name, Dept, Course, count(Course)
                    from instructors join grades
                    on CWID = InstructorCWID
                    group by course, InstructorCWID """

        for row in stevens_db.execute(query):
            cwid, name, dept, course, num_students = row
            instructors1[cwid, name, dept, course] = row


        instructor_data1 = {
            ('98762', 'Hawking, S', 'CS', 'CS 501'):
                ('98762', 'Hawking, S', 'CS', 'CS 501', 1),
            ('98762', 'Hawking, S', 'CS', 'CS 546'):
                ('98762', 'Hawking, S', 'CS', 'CS 546', 1),
            ('98762', 'Hawking, S', 'CS', 'CS 570'):
                ('98762', 'Hawking, S', 'CS', 'CS 570', 1),
            ('98763', 'Rowland, J', 'SFEN', 'SSW 555'):
                ('98763', 'Rowland, J', 'SFEN', 'SSW 555', 1),
            ('98763', 'Rowland, J', 'SFEN', 'SSW 810'):
                ('98763', 'Rowland, J', 'SFEN', 'SSW 810', 4),
            ('98764', 'Cohen, R', 'SFEN', 'CS 546'):
                ('98764', 'Cohen, R', 'SFEN', 'CS 546', 1)
        }

        self.assertEqual(majors, major_data)
        self.assertEqual(students, student_data)
        self.assertEqual(instructors, instructor_data)
        self.assertEqual(instructors1, instructor_data1)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)