#!/usr/bin/env python

"""
Created on Wed Oct 30 2019
@author: Vikas Bhat
Homework9
Unit Testing

"""

import unittest
from HW09_Vikas_Bhat import StevensRepository, StudentInfo, InstructorInfo


class TestCases(unittest.TestCase):



    def test_StevensRepository(self):
        "Testing whole reprository"
        test_info = StevensRepository("/Users/vikasbhat/Desktop/SSW_HW09")
        test_info.student_repository()
        test_info.instructor_repository()
        test_info.grades_repository()

        self.assertEqual(test_info.student_info, {
            '10103': ['Baldwin, C', 'SFEN', {'SSW 567': 'A', 'SSW 564': 'A-', 'SSW 687': 'B', 'CS 501': 'B'}],
            '10115': ['Wyatt, X', 'SFEN', {'SSW 567': 'A', 'SSW 564': 'B+', 'SSW 687': 'A', 'CS 545': 'A'}],
            '10172': ['Forbes, I', 'SFEN', {'SSW 555': 'A', 'SSW 567': 'A-'}],
            '10175': ['Erickson, D', 'SFEN', {'SSW 567': 'A', 'SSW 564': 'A', 'SSW 687': 'B-'}],
            '10183': ['Chapman, O', 'SFEN', {'SSW 689': 'A'}],
            '11399': ['Cordova, I', 'SYEN', {'SSW 540': 'B'}],
            '11461': ['Wright, U', 'SYEN', {'SYS 800': 'A', 'SYS 750': 'A-', 'SYS 611': 'A'}],
            '11658': ['Kelly, P', 'SYEN', {'SSW 540': 'F'}],
            '11714': ['Morton, A', 'SYEN', {'SYS 611': 'A', 'SYS 645': 'C'}],
            '11788': ['Fuller, E', 'SYEN', {'SSW 540': 'A'}]})
        self.assertEqual(test_info.instructor_info, {
            '98765': ['Einstein, A', 'SFEN', {'SSW 567': 4, 'SSW 540': 3}],
            '98764': ['Feynman, R', 'SFEN', {'SSW 564': 3, 'SSW 687': 3, 'CS 501': 1, 'CS 545': 1}],
            '98763': ['Newton, I', 'SFEN', {'SSW 555': 1, 'SSW 689': 1}],
            '98762': ['Hawking, S', 'SYEN', {}], '98761': ['Edison, A', 'SYEN', {}],
             '98760': ['Darwin, C', 'SYEN', {'SYS 800': 1, 'SYS 750': 1, 'SYS 611': 2, 'SYS 645': 1}]})

    def test_studentInfo(self):

        student1 = StudentInfo("11714", "Morton, A", "SYEN", {})
        self.assertEqual(student1.student(), ["11714", "Morton, A", "SYEN", {}])


        student2 = StudentInfo("11714", "Morton, A", "SYEN", {})
        self.assertNotEqual(student2.student(), ["98763", "Newton, I", "SFEN", {}])

    def test_InstructorInfo(self):

        Instructor1 = InstructorInfo("98763", "Newton, I", "SFEN", {})
        self.assertEqual(Instructor1.instructor(), ["98763", "Newton, I", "SFEN", {}])

        Instructor2 = InstructorInfo("98763", "Newton, I", "SFEN", {})
        self.assertNotEqual(Instructor2.instructor(), ["11714", "Morton, A", "SYEN", {}])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

