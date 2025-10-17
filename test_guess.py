import unittest
from guess import guess_number, build_range

class TestGuessNumber(unittest.TestCase):
    def test_slow(self):
        nums = build_range(1, 10)
        self.assertEqual(guess_number(7, nums, "slow"), (7, 7))

    def test_binary(self):
        nums = build_range(0, 7)
        found, guesses = guess_number(3, nums, "binary")
        self.assertEqual(guess_number(3, nums, "binary"), (3, 1))

    def test_not_sorted_slow(self):
        nums = [5, 2, 9, 1, 7]
        self.assertEqual(guess_number(7, nums, "slow"), (7, 5))

    def test_not_sorted_binary(self):
        nums = [5, 2, 9, 1, 7]
        self.assertEqual(guess_number(7, nums, "binary"), (7, 2))

    def test_one_element(self):
        nums = [42]
        self.assertEqual(guess_number(42, nums, "slow"), (42, 1))
        self.assertEqual(guess_number(42, nums, "binary"), (42, 1))

    def test_invalid_method(self):
        nums = build_range(1, 5)
        with self.assertRaises(AssertionError):
            guess_number(3, nums, "Ali") 

    def test_Target_is_not_in_list(self):
        nums = build_range(1, 5)
        with self.assertRaises(AssertionError):
            guess_number(10, nums, "slow")

    def test_non_unique_list(self):
        nums = [1, 2, 2, 3]
        with self.assertRaises(AssertionError):
            guess_number(2, nums, "binary")

    def test_empty_list(self):
        with self.assertRaises(AssertionError):
            guess_number(1, [], "slow")

    def test_type_checks_build_range(self):
        with self.assertRaises(AssertionError):
            build_range(5.0, 10)
        with self.assertRaises(AssertionError):
            build_range(10, 5)

    def test_type_checks_guess_number(self):
        with self.assertRaises(AssertionError):
            guess_number("3", [1,2,3], "slow")
        with self.assertRaises(AssertionError):
            guess_number(3, (1,2,3), "slow") 
        with self.assertRaises(AssertionError):
            guess_number(3, [1, 2.0, 3], "slow")

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)
