from reverse import Reverse
import unittest

__author__ = 'mandreacchio'


class ReverseTest(unittest.TestCase):

    def test_reverse_def(self):
        self.assertEquals(Reverse.reverse("Hello"), "olleH")
        self.assertNotEquals(Reverse.reverse("Hello"), "Hello")


if __name__ == "__main__":
    unittest.main()
