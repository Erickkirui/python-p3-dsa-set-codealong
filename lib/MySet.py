import unittest
from MySet import MySet

class TestSet(unittest.TestCase):

    def test_init(self):
        '''Test __init__ set with list'''
        test_set = MySet([1,2,3,4])
        set_list = [1,2,3,4]
        for num in set_list:
            self.assertIn(num, test_set.dictionary)

    def test_add(self):
        '''Test add() to set'''
        test_set = MySet([1,2,3,4])
        test_set.add(5)
        set_list = [1,2,3,4,5]
        for num in set_list:
            self.assertIn(num, test_set.dictionary)

    def test_delete(self):
        '''Test delete()'''
        test_set = MySet([1,2,3,4])
        test_set.delete(2)
        set_list = [1,3,4]
        for num in set_list:
            self.assertIn(num, test_set.dictionary)

    def test_has(self):
        '''Test has()'''
        test_set = MySet([1,2,3,4])
        self.assertTrue(test_set.has(1))
        self.assertFalse(test_set.has(7))

    def test_size(self):
        '''Test size()'''
        test_set = MySet([1,2,3,4])
        self.assertEqual(len(test_set.dictionary), 4)

if __name__ == '__main__':
    unittest.main()

