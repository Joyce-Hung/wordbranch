from unittest import TestCase
from wiw_sort import wiw_sort


class OrderingTest(TestCase):

    def test_sort_case_1(self):
        result = wiw_sort(word='basketball', words=['basket', 'ball'])
        self.assertEqual(result, ['basket', 'ball'])

    def test_sort_case_1_2(self):
        ''' 三個字 '''
        result = wiw_sort(word='basketball', words=['ball', 'basket'])
        self.assertEqual(result, ['basket', 'ball'])

    def test_sort_case_2(self):
        ''' 多餘的字母 '''
        result = wiw_sort(word='acetic', words=['ac', 'ic'])
        self.assertEqual(result, ['ac', 'ic'])

    def test_sort_case_2_2(self):
        result = wiw_sort(word='acetic', words=['ic', 'ac'])
        self.assertEqual(result, ['ac', 'ic'])

    def test_sort_case_3(self):
        ''' 模糊比對 '''
        result = wiw_sort(word='asexual', words=['sexual', 'an'])
        self.assertEqual(result, ['an', 'sexual'])

    def test_sort_case_3_2(self):
        result = wiw_sort(word='asexual', words=['an', 'sexual'])
        self.assertEqual(result, ['an', 'sexual'])

    def test_sort_case_4(self):
        ''' 更模糊的比對'''
        result = wiw_sort(word='irascible', words=['ire', 'able'])
        self.assertEqual(result, ['ire', 'able'])

    def test_sort_case_4_2(self):
        result = wiw_sort(word='irascible', words=['able', 'ire'])
        self.assertEqual(result, ['ire', 'able'])
        
    def test_sort_case_5(self):
        result = wiw_sort(word='companionship', words=['companion', 'ship'])
        self.assertEqual(result, ['companion', 'ship'])

    def test_sort_case_5_2(self):
        result = wiw_sort(word='companionship', words=['ship', 'companion'])
        self.assertEqual(result, ['companion', 'ship'])
        
    def test_sort_case_6(self):
        result = wiw_sort(word='internationalization',
                          words=['internationalize', 'ion'])
        self.assertEqual(result, ['internationalize', 'ion'])

    def test_sort_case_6_2(self):
        result = wiw_sort(word='internationalization',
                          words=['ion', 'internationalize'])
        self.assertEqual(result, ['internationalize', 'ion'])