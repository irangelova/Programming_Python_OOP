from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    fuel = 45.5
    horse_power = 125.5

    def setUp(self) -> None:
        self.test_vehicle = Vehicle(self.fuel, self.horse_power)

    def test_class_attributes_types(self):
        self.assertIsInstance(self.test_vehicle.DEFAULT_FUEL_CONSUMPTION, float)
        self.assertIsInstance(self.test_vehicle.fuel_consumption, float)
        self.assertIsInstance(self.test_vehicle.fuel, float)
        self.assertIsInstance(self.test_vehicle.capacity, float)
        self.assertIsInstance(self.test_vehicle.horse_power, float)

    def test_init(self):
        self.assertEqual(self.fuel, self.test_vehicle.fuel)
        self.assertEqual(self.fuel, self.test_vehicle.capacity)
        self.assertEqual(self.horse_power, self.test_vehicle.horse_power)
        self.assertEqual(1.25, self.test_vehicle.fuel_consumption)

    def test_drive_successful(self):
        self.test_vehicle.drive(20)
        self.assertEqual(20.5, self.test_vehicle.fuel)

    def test_drive_not_successful(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.drive(3000)
        self.assertEqual("Not enough fuel", str(ex.exception))
        self.assertEqual(self.fuel, self.test_vehicle.fuel)

    def test_refuel_successful(self):
        self.test_vehicle.fuel = 1
        self.test_vehicle.refuel(30.5)
        self.assertEqual(31.5, self.test_vehicle.fuel)

    def test_refuel_not_successful(self):
        self.test_vehicle.fuel = 40
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.refuel(30)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str(self):
        expected_result = f"The vehicle has {self.horse_power} horse power with {self.fuel} fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_result, str(self.test_vehicle))


if __name__ == "__main__":
    main()
