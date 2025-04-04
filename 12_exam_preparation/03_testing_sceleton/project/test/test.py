from unittest import TestCase, main
from project.senior_student import SeniorStudent


class TestSeniorStudent(TestCase):
    test_student_id = "1234"
    test_student_name = "Test"
    test_student_gpa = 4.7

    def setUp(self) -> None:
        self.test_student = SeniorStudent(self.test_student_id, self.test_student_name, self.test_student_gpa)

    def test_init(self):
        self.assertEqual(self.test_student_id, self.test_student.student_id)
        self.assertEqual(self.test_student_name, self.test_student.name)
        self.assertEqual(self.test_student_gpa, self.test_student.student_gpa)
        self.assertEqual(0, len(self.test_student.colleges))

    def test_student_id_too_short(self):
        with self.assertRaises(ValueError) as e:
            self.test_student.student_id = "123"
        self.assertEqual("Student ID must be at least 4 digits long!", str(e.exception))

        with self.assertRaises(ValueError) as e:
            self.test_student.student_id = "  123 "
        self.assertEqual("Student ID must be at least 4 digits long!", str(e.exception))

    def test_student_id_valid_stripped(self):
        self.test_student.student_id = "12345 "
        self.assertEqual("12345", self.test_student.student_id)

    def test_name_valid(self):
        self.test_student.name = "Johnny Bravo"
        self.assertEqual("Johnny Bravo", self.test_student.name)

    def test_name_empty(self):
        with self.assertRaises(ValueError) as e:
            self.test_student.name = ""
        self.assertEqual("Student name cannot be null or empty!", str(e.exception))

        with self.assertRaises(ValueError) as e:
            self.test_student.name = "   "
        self.assertEqual("Student name cannot be null or empty!", str(e.exception))

    def test_student_gpa_valid(self):
        self.test_student.student_gpa = 5.5
        self.assertEqual(5.5, self.test_student.student_gpa)

    def test_student_gpa_not_valid(self):
        with self.assertRaises(ValueError) as e:
            self.test_student.student_gpa = 0.7
        self.assertEqual("Student GPA must be more than 1.0!", str(e.exception))

        with self.assertRaises(ValueError) as e:
            self.test_student.student_gpa = 0.0
        self.assertEqual("Student GPA must be more than 1.0!", str(e.exception))

    def test_apply_to_college_low_gpa(self):
        actual = self.test_student.apply_to_college(4.9, "Harvard")
        expected = 'Application failed!'
        self.assertEqual(expected, actual)
        self.assertEqual(0, len(self.test_student.colleges))

    def test_apply_to_college_success(self):
        actual = self.test_student.apply_to_college(4.2, "Harvard")
        expected = f'{self.test_student_name} successfully applied to Harvard.'
        self.assertEqual(expected, actual)
        self.assertEqual(1, len(self.test_student.colleges))

    def test_apply_to_college_multi(self):
        self.test_student.apply_to_college(4.2, "Harvard")
        self.test_student.apply_to_college(4.2, "MIT")
        self.test_student.apply_to_college(4.2, "HarVArD")
        self.test_student.apply_to_college(4.2, "mIt")
        self.assertEqual(2, len(self.test_student.colleges))

    def test_update_gpa_not_successful(self):
        actual = self.test_student.update_gpa(0.9)
        expected = "The GPA has not been changed!"
        self.assertEqual(expected, actual)
        self.assertEqual(4.7, self.test_student.student_gpa)

        actual = self.test_student.update_gpa(1.0)
        expected = "The GPA has not been changed!"
        self.assertEqual(expected, actual)
        self.assertEqual(4.7, self.test_student.student_gpa)

    def test_update_gpa_successful(self):
        actual = self.test_student.update_gpa(5.1)
        expected = "Student GPA was successfully updated."
        self.assertEqual(expected, actual)
        self.assertEqual(5.1, self.test_student.student_gpa)

    def test__eq__valid(self):
        test_student2 = SeniorStudent("7889", "Jane Daniels", 4.7)
        self.assertTrue(self.test_student == test_student2)

    def test__eq__not_valid(self):
        test_student2 = SeniorStudent("7889", "Jane Daniels", 5.3)
        self.assertFalse(self.test_student == test_student2)

        test_student3 = SeniorStudent("7889", "Jane Daniels", 3.7)
        self.assertFalse(self.test_student == test_student3)


if __name__ == "__main__":
    main()