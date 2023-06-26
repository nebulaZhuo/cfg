import unittest
from unittest.mock import patch
from io import StringIO
from shop import purchased, retry_purchase, ThreeFailedAttempts

# A reminder of the items and prices
# prices = {"TV": 1000, "Phone": 50, "Alarm Clock": 25}

class TestingPurchased(unittest.TestCase):
    # VALID CASES
    def test_purchased_with_enough_money(self):
        self.assertEqual(True, purchased(item="Phone", balance=100))

    # INVALID/ERRONEOUS CASES
    def test_purchased_with_not_enough_money(self):
        self.assertFalse(purchased(item="TV", balance=100))
    def test_purchased_with_negative_money(self):
        self.assertEqual(False, purchased(item="Phone", balance=-100))

    # BOUNDARY CASE
    def test_purchased_with_just_enough_money(self):
        self.assertTrue(purchased(item="TV", balance=1000))

class TestingRetryPurchase(unittest.TestCase):

    # TESTING RAISED CUSTOM ERROR
    def test_retrypurchased_too_many_attempts(self):
        with self.assertRaises(ThreeFailedAttempts):
            retry_purchase(item="TV", balance=100, attempts=3)
    
    # VALID CASE
    def test_retrypurchased_successful(self):
        with patch("builtins.input", side_effect=["Y", "50"]):
            with patch("sys.stdout", new=StringIO()) as output:
                retry_purchase(item = "Phone", balance = 100, attempts = 2)
                self.assertEqual(output.getvalue().strip(), "Here's your Phone!\n\nThanks for coming to The Store. Come again!\n*******************************************")
    
    # INVALID CASE
    def test_retrypurchased_unSuccessful(self):
        with patch("builtins.input", side_effect=["N"]):
            with self.assertRaises(SystemExit):
                retry_purchase(item = "Alarm Clock", balance = 0, attempts = 2)


if __name__ == '__main__':
    unittest.main()
