from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    username = "Test"
    level = 3
    health = 5.5
    damage = 7.5

    def setUp(self) -> None:
        self.test_hero = Hero(self.username, self.level, self.health, self.damage)

    def test_class_attributes_types(self):
        self.assertIsInstance(self.test_hero.username, str)
        self.assertIsInstance(self.test_hero.health, float)
        self.assertIsInstance(self.test_hero.damage, float)
        self.assertIsInstance(self.test_hero.level, int)

    def test_init(self):
        self.assertEqual(self.username, self.test_hero.username)
        self.assertEqual(self.level, self.test_hero.level)
        self.assertEqual(self.health, self.test_hero.health)
        self.assertEqual(self.damage, self.test_hero.damage)

    def test_usernames_equal(self):
        enemy = Hero(self.username, self.level, self.health, self.damage)
        with self.assertRaises(Exception) as ex:
            self.test_hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_own_health_not_enough(self):
        self.test_hero.health = 0
        enemy = Hero("Enemy", self.level, self.health, self.damage)
        with self.assertRaises(ValueError) as e:
            self.test_hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(e.exception))

        self.test_hero.health = -1

        enemy = Hero("Enemy", self.level, self.health, self.damage)
        with self.assertRaises(ValueError) as e:
            self.test_hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(e.exception))

    def test_enemy_health_not_enough(self):
        enemy = Hero("Enemy", self.level, 0, self.damage)
        with self.assertRaises(ValueError) as e:
            self.test_hero.battle(enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(e.exception))

        enemy.health = -1
        with self.assertRaises(ValueError) as e:
            self.test_hero.battle(enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(e.exception))

    def test_draw_result(self):
        enemy = Hero("Enemy", self.level, self.health, self.damage)

        result = self.test_hero.battle(enemy)
        self.assertEqual(self.level, self.test_hero.level)
        self.assertEqual(-17.0, self.test_hero.health)
        self.assertEqual(self.damage, self.test_hero.damage)
        self.assertEqual("Draw", result)

        self.assertEqual(self.level, enemy.level)
        self.assertEqual(-17.0, enemy.health)
        self.assertEqual(self.damage, enemy.damage)

    def test_hero_wins(self):
        enemy = Hero("Enemy", 1, 1, 1)
        result = self.test_hero.battle(enemy)

        self.assertEqual(4, self.test_hero.level)
        self.assertEqual(9.5, self.test_hero.health)
        self.assertEqual(12.5, self.test_hero.damage)
        self.assertEqual("You win", result)

        self.assertEqual(1, enemy.level)
        self.assertEqual(-21.5, enemy.health)
        self.assertEqual(1, enemy.damage)

    def test_hero_loses(self):
        enemy = Hero("Enemy", 100, 100, 100)
        result = self.test_hero.battle(enemy)

        self.assertEqual(self.level, self.test_hero.level)
        self.assertEqual(-9994.5, self.test_hero.health)
        self.assertEqual(self.damage, self.test_hero.damage)
        self.assertEqual("You lose", result)

        self.assertEqual(101, enemy.level)
        self.assertEqual(82.5, enemy.health)
        self.assertEqual(105, enemy.damage)

    def test_str(self):
        expected_result = f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"
        self.assertEqual(expected_result, str(self.test_hero))


if __name__ == "__main__":
    main()
