from unittest import TestCase
from context import src
from src.my_module import get_cheapest_hotel

class MyTest(TestCase):
    def test1(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"))

    def test2(self):
        result = "Bridgewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))

    def test3(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"))

    def test_one_day_weekday_rewards(self):
        # Verify only 1 day WEEKDAY and REWARDS
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 26Mar2009(thur)"))

    def test_one_day_weekday_regular(self):
        # Verify only 1 day WEEKDAY and REGULAR
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 25Mar2009(wed)"))

    def test_one_day_weekend_rewards(self):
        # Verify only 1 day WEEKEND and REWARDS
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 28Mar2009(sat)"))

    def test_one_day_weekend_regular(self):
        # Verify only 1 day WEEKEND and REGULAR
        result = "Bridgewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 28Mar2009(sun)"))

    def test_all_week_rewards(self):
        # Verify one complete week REWARDS
        result = "Lakewood"
        week = "Rewards: 22Mar2009(sun), 23Mar2009(mon), 24Mar2009(tues), 25Mar2009(wed), 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"
        self.assertEqual(result, get_cheapest_hotel(week))

    def test_all_week_regular(self):
        # Verify one complete week REGULAR
        result = "Lakewood"
        week = "Regular: 22Mar2009(sun), 23Mar2009(mon), 24Mar2009(tues), 25Mar2009(wed), 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"
        self.assertEqual(result, get_cheapest_hotel(week))

    def test_weekend_rewards(self):
        # Verify weekend and Regular
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 28Mar2009(sat), 29Mar2009(sun)"))

    def test_weekend_regular(self):
        # Verify weekend and Regular
        result = "Bridgewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 28Mar2009(sat), 29Mar2009(sun)"))

    def test_weekend_an_weekday_rewards(self):
        # Verify weekend day and weekday - Regular
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 29Mar2009(sun), 30Mar2009(mon)"))

    def test_weekend_an_weekday_regular(self):
        # Verify weekend day and weekday - Regular
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 29Mar2009(sun), 30Mar2009(mon)"))