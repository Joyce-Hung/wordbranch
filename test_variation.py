from unittest import TestCase
from variation import find_variation


class OrderingTest(TestCase):
    def test_sort_case_1(self):
        result = find_variation('contest', ['co', 'col', 'cor', 'com'])
        self.assertEqual(result, 'co')

    def test_sort_case_2(self):
        result = find_variation('company', ['co', 'col', 'cor', 'com'])
        self.assertEqual(result, 'com')

    def test_sort_case_3(self):
        result = find_variation('along', ['ante', 'anti'])
        self.assertEqual(result, 'ante')
