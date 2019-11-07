#!/usr/bin/env python

"""
Created on Thursday Nov 7 2019
@author: Vikas Bhat
Homework10
Unit Testing

"""

import unittest
from HW10_Vikas_Bhat import StevensRepository


class TestStevensRepository(unittest.TestCase):

    def test_repo(self):
        dir_path = '/Users/vikasbhat/Desktop/SSW810_HW/'
        stevens = StevensRepository(dir_path)

        self.assertEqual(stevens._dir_path, dir_path)
        majors = dict()

        for name, major in stevens.majorsInfo.items():
            majors[name] = major.attributes()

        major_data = {
            'SFEN': [
                'SFEN',
                ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'],
                ['CS 501', 'CS 513', 'CS 545']
            ],
            'SYEN': [
                'SYEN',
                ['SYS 612', 'SYS 671', 'SYS 800'],
                ['SSW 540', 'SSW 565', 'SSW 810']
            ]
        }

        students = dict()
        for cwid, student in stevens.studentsInfo.items():
            students[cwid] = student.attributes()
        student_data = {
            '10103': [
                '10103',
                'Baldwin, C',
                'SFEN',
                ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'],
                ['SSW 540', 'SSW 555'],
                None
            ],
            '10115': [
                '10115',
                'Wyatt, X',
                'SFEN',
                ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'],
                ['SSW 540', 'SSW 555'],
                None
            ],
            '10172': [
                '10172',
                'Forbes, I',
                'SFEN',
                ['SSW 555', 'SSW 567'],
                ['SSW 540', 'SSW 564'],
                ['CS 501', 'CS 513', 'CS 545']
            ],
            '10175': [
                '10175',
                'Erickson, D',
                'SFEN',
                ['SSW 564', 'SSW 567', 'SSW 687'],
                ['SSW 540', 'SSW 555'],
                ['CS 501', 'CS 513', 'CS 545']
            ],
            '10183': [
                '10183',
                'Chapman, O',
                'SFEN',
                ['SSW 689'],
                ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'],
                ['CS 501', 'CS 513', 'CS 545']
            ],
            '11399': [
                '11399',
                'Cordova, I',
                'SYEN',
                ['SSW 540'],
                ['SYS 612', 'SYS 671', 'SYS 800'],
                None
            ],
            '11461': [
                '11461',
                'Wright, U',
                'SYEN',
                ['SYS 611', 'SYS 750', 'SYS 800'],
                ['SYS 612', 'SYS 671'],
                ['SSW 540', 'SSW 565', 'SSW 810']
            ],
            '11658': [
                '11658',
                'Kelly, P',
                'SYEN',
                ['SSW 540'],
                ['SYS 612', 'SYS 671', 'SYS 800'],
                ['SSW 540', 'SSW 565', 'SSW 810']
            ],
            '11714': [
                '11714',
                'Morton, A',
                'SYEN',
                ['SYS 611', 'SYS 645'],
                ['SYS 612', 'SYS 671', 'SYS 800'],
                ['SSW 540', 'SSW 565', 'SSW 810']
            ],
            '11788': [
                '11788',
                'Fuller, E',
                'SYEN',
                ['SSW 540'],
                ['SYS 612', 'SYS 671', 'SYS 800'],
                None
            ]
        }

        instructors = dict()

        for cwid, instructor in stevens.instructorsInfo.items():
            for course in instructor.attributes():
                instructors[cwid] = course

        # create another dictionary based on the raw data
        instructor_data = {
            '98765': ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3],
            '98764': ['98764', 'Feynman, R', 'SFEN', 'CS 545', 1],
            '98763': ['98763', 'Newton, I', 'SFEN', 'SSW 689', 1],
            '98760': ['98760', 'Darwin, C', 'SYEN', 'SYS 645', 1]
        }

        self.assertEqual(majors, major_data)
        self.assertEqual(students, student_data)
        self.assertEqual(instructors, instructor_data)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)