from django.test import TestCase

class SimpleTest(TestCase):
    def test_sum(self):
        self.assertEqual(2 + 2, 4)
