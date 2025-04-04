from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self) -> None:
        self.test_student1 = Student("Mike", {"Maths": ["n1", "n2"], "Physics": ["n1"]})
        self.test_student2 = Student("Peter")

    def test_init_with_courses(self):
        self.assertEqual("Mike", self.test_student1.name)
        self.assertEqual({"Maths": ["n1", "n2"], "Physics": ["n1"]}, self.test_student1.courses)

        self.assertIsInstance(self.test_student1.name, str)
        self.assertIsInstance(self.test_student1.courses, dict)

    def test_init_without_courses(self):
        self.assertEqual("Peter", self.test_student2.name)
        self.assertEqual({}, self.test_student2.courses)
        self.assertIsInstance(self.test_student2.name, str)
        self.assertIsInstance(self.test_student2.courses, dict)

    def test_enroll_course_already_existing(self):
        result = self.test_student1.enroll("Maths", ["n3", "n4"])

        self.assertEqual({"Maths": ["n1", "n2", "n3", "n4"], "Physics": ["n1"]}, self.test_student1.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

        result = self.test_student1.enroll("Maths", ["n5", "n6"], "N")

        self.assertEqual({"Maths": ["n1", "n2", "n3", "n4", "n5", "n6"], "Physics": ["n1"]}, self.test_student1.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_course_not_existing_adding_notes_with_empty_string(self):
        result = self.test_student1.enroll("Geography", ["n1", "n2"], "")

        self.assertIn("Geography", self.test_student1.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["n1", "n2"], self.test_student1.courses["Geography"])

    def test_enroll_course_not_existing_adding_notes_with_empty_Y(self):
        result = self.test_student1.enroll("Geography", ["n1", "n2"], "Y")

        self.assertIn("Geography", self.test_student1.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["n1", "n2"], self.test_student1.courses["Geography"])

    def test_enroll_course_not_existing_without_adding_notes(self):
        result = self.test_student2.enroll("Geography", ["n1", "n2"], "N")

        self.assertIn("Geography", self.test_student2.courses)
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.test_student2.courses["Geography"])

    def test_add_notes_to_existing_course(self):
        self.test_student2.enroll("Geography", ["n1", "n2"])
        result = self.test_student2.add_notes("Geography", "n3")

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["n1", "n2", "n3"], self.test_student2.courses["Geography"])

    def test_add_notes_to_not_existing_course_raises_ex(self):
        with self.assertRaises(Exception) as ex:
            self.test_student2.add_notes("Python", "n1")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        result = self.test_student1.leave_course("Maths")

        self.assertEqual("Course has been removed", result)
        self.assertNotIn("Maths", self.test_student1.courses)

    def test_leave_not_existing_course_raises_ex(self):
        with self.assertRaises(Exception) as ex:
            self.test_student1.leave_course("Python")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
