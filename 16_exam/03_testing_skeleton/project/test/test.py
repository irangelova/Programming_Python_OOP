from unittest import TestCase, main
from project.star_system import StarSystem

class TestStarSystem(TestCase):
    name = "Test"
    star_type = "Red giant"
    system_type = "Multiple"
    num_planets = 7
    habitable_zone_range = None

    def setUp(self) -> None:
        self.test_star_system1 = StarSystem(self.name, self.star_type, self.system_type, self.num_planets)
        self.test_star_system2 = StarSystem(self.name, self.star_type, self.system_type, self.num_planets, (1, 3))

    def test_class_attributes_types(self):
        self.assertIsInstance(self.test_star_system1.name, str)
        self.assertIsInstance(self.test_star_system1.star_type, str)
        self.assertIsInstance(self.test_star_system1.system_type, str)
        self.assertIsInstance(self.test_star_system1.num_planets, int)

    def test_init_with_habitable_zone_range(self):
        self.assertEqual(self.name, self.test_star_system1.name)
        self.assertEqual(self.star_type, self.test_star_system1.star_type)
        self.assertEqual(self.system_type, self.test_star_system1.system_type)
        self.assertEqual(self.num_planets, self.test_star_system1.num_planets)

        self.assertEqual((1, 3), self.test_star_system2.habitable_zone_range)

    def test_init_without_habitable_zone_range(self):
        self.assertEqual(self.name, self.test_star_system1.name)
        self.assertEqual(self.star_type, self.test_star_system1.star_type)
        self.assertEqual(self.system_type, self.test_star_system1.system_type)
        self.assertEqual(self.num_planets, self.test_star_system1.num_planets)

    def test_is_habitable(self):
        self.assertEqual(True, self.test_star_system2.is_habitable)

    def test_is_not_habitable(self):
        self.assertEqual(False, self.test_star_system1.is_habitable)

    def test_empty_and_stripped_name(self):
        with self.assertRaises(ValueError) as e:
            self.test_star_system1.name = ""
        self.assertEqual("Name must be a non-empty string.", str(e.exception))

        with self.assertRaises(ValueError) as e:
            self.test_star_system1.name = "   "
        self.assertEqual("Name must be a non-empty string.", str(e.exception))

    def test_valid_name(self):
        self.test_star_system2.name = "TestStar"
        self.assertEqual("TestStar", self.test_star_system2.name)

    def test_star_type_not_in_defined_types(self):
        with self.assertRaises(ValueError) as e:
            self.test_star_system1.star_type = "Not_valid_star_type"
        self.assertEqual((f"Star type must be one of ['Blue giant', 'Brown dwarf',"
                          f" 'Red dwarf', 'Red giant', 'Yellow dwarf']."), str(e.exception))

    def test_star_type_in_defined_types(self):
        self.test_star_system1.star_type = "Blue giant"
        self.assertEqual("Blue giant", self.test_star_system1.star_type)

    def test_system_type_not_in_defined_types(self):
        with self.assertRaises(ValueError) as e:
            self.test_star_system1.system_type = "Not_valid_system_type"
        self.assertEqual((f"System type must be one of "
                          f"['Binary', 'Multiple', 'Single', 'Triple']."), str(e.exception))

    def test_system_type_in_defined_types(self):
        self.test_star_system1.system_type = "Multiple"
        self.assertEqual("Multiple", self.test_star_system1.system_type)

    def test_num_planets_not_valid(self):
        with self.assertRaises(ValueError) as e:
            self.test_star_system2.num_planets = -1
        self.assertEqual("Number of planets must be a non-negative integer.", str(e.exception))

    def test_num_planets_valid(self):
        self.test_star_system2.num_planets = 9
        self.assertEqual(9, self.test_star_system2.num_planets)

    def test_habitable_zone_range_is_none(self):
        self.test_star_system1.habitable_zone_range = None
        self.assertEqual(None, self.test_star_system1.habitable_zone_range)

    def test_habitable_zone_range_is_not_none_and_len_more_than_2(self):
        with self.assertRaises(ValueError) as e:
            self.test_star_system1.habitable_zone_range = [1, 3, 5]
        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.", str(e.exception))

    def test_habitable_zone_range_is_not_none_and_len_less_than_2(self):
        with self.assertRaises(ValueError) as e:
            self.test_star_system1.habitable_zone_range = [1]
        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.", str(e.exception))

    def test_habitable_zone_range_is_not_none_len_is_equal_2_and_first_element_is_bigger_than_second(self):
        with self.assertRaises(ValueError) as e:
            self.test_star_system1.habitable_zone_range = [5, 3]
        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.", str(e.exception))

    def test_habitable_zone_range_is_not_none_len_is_equal_2_and_first_element_is_smaller_than_second(self):
        self.test_star_system1.habitable_zone_range = [1, 3]
        self.assertEqual([1, 3], self.test_star_system1.habitable_zone_range)

    def test_habitable_zone_range_is_not_none_len_is_equal_2_and_first_element_is_equal_to_second(self):
        with self.assertRaises(ValueError) as e:
            self.test_star_system1.habitable_zone_range = [3, 3]
        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.",
                         str(e.exception))

    def test__gt__valid_and_true(self):
        self.test_star_system3 = StarSystem("TestSystem3", "Yellow dwarf", "Triple", 9, (2, 5))
        self.assertTrue(self.test_star_system3 > self.test_star_system2)

    def test__gt__valid_and_false(self):
        self.test_star_system3 = StarSystem("TestSystem3", "Yellow dwarf", "Triple", 9, (2, 5))
        self.assertFalse(self.test_star_system2 > self.test_star_system3)

    #TODO
    def test__gt__invalid(self):
        self.test_star_system3 = StarSystem("TestSystem3", "Yellow dwarf", "Triple", 9, habitable_zone_range=None)
        with self.assertRaises(ValueError) as e:
            self.test_star_system3.__gt__(self.test_star_system2)
        self.assertEqual("Comparison not possible: One or both systems lack a defined habitable zone or planets.", str(e.exception))

    def test_compare_star_systems_valid_first_system_bigger(self):
        self.test_star_system3 = StarSystem("TestSystem3", "Yellow dwarf", "Triple", 9, (1, 3))
        self.test_star_system4 = StarSystem("TestSystem4", "Yellow dwarf", "Triple", 9, (1, 2))
        self.assertEqual("TestSystem3 has a wider habitable zone than TestSystem4.", StarSystem.compare_star_systems(self.test_star_system3, self.test_star_system4))

    def test_compare_star_systems_valid_second_system_bigger(self):
        self.test_star_system3 = StarSystem("TestSystem3", "Yellow dwarf", "Triple", 9, (1, 2))
        self.test_star_system4 = StarSystem("TestSystem4", "Yellow dwarf", "Triple", 9, (1, 3))
        self.assertEqual("TestSystem4 has a wider or equal habitable zone compared to TestSystem3.", StarSystem.compare_star_systems(self.test_star_system3, self.test_star_system4))

    def test_compare_star_systems_invalid_systems(self):
        self.test_star_system3 = StarSystem("TestSystem3", "Yellow dwarf", "Triple", 9)
        self.test_star_system4 = StarSystem("TestSystem4", "Yellow dwarf", "Triple", 4, (1, 3))
        self.assertEqual("Comparison not possible: One or both systems lack a defined habitable zone or planets.", StarSystem.compare_star_systems(self.test_star_system3, self.test_star_system4))


if __name__ == "__main__":
    main()
