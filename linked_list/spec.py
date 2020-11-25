import unittest
from index import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        empty_linked_list = LinkedList()
        linked_list = LinkedList()
        for i in range(10):
            linked_list.append(i)
        self.empty_linked_list = empty_linked_list # []
        self.linked_list = linked_list # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def tearDown(self):
        del self.empty_linked_list
        del self.linked_list

    def test_is_empty(self):
        self.assertTrue(self.empty_linked_list.is_empty())
        self.assertFalse(self.linked_list.is_empty())

    def test_get_tail(self):
        self.assertIsNone(self.empty_linked_list.get_tail())
        self.assertEqual(self.linked_list.get_tail().value, 9)

    def test_to_list(self):
        self.assertEqual(self.empty_linked_list.to_list(), [])
        self.assertEqual(self.linked_list.to_list(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_index(self):
        self.assertEqual(self.empty_linked_list.index(0), -1)
        self.assertEqual(self.linked_list.index(10), -1)
        self.assertEqual(self.linked_list.index(0), 0)
        self.linked_list.reverse()
        self.assertEqual(self.linked_list.index(0), 9)
        
    def test_at_index(self):
        self.assertEqual(self.linked_list.at_index(2), 2)
        self.linked_list.reverse()
        self.assertEqual(self.linked_list.at_index(2), 7)
    
    def test_append(self):
        for i in range(10):
            self.empty_linked_list.append(i)
            self.assertEqual(self.empty_linked_list.head.value, 0)
            self.assertEqual(self.empty_linked_list.tail.value, i)
            self.assertEqual(self.empty_linked_list.length, i+1)
        self.assertEqual(self.empty_linked_list.to_list(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    def test_left_append(self):
        for i in range(10):
            self.empty_linked_list.left_append(i)
            self.assertEqual(self.empty_linked_list.head.value, i)
            self.assertEqual(self.empty_linked_list.tail.value, 0)
            self.assertEqual(self.empty_linked_list.length, i+1)
        self.assertEqual(self.empty_linked_list.to_list(), [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    
    def test_insert(self):
        self.linked_list.insert(8, 8)
        self.assertEqual(self.linked_list.to_list(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9])
        self.assertEqual(self.linked_list.length, 11)
        self.linked_list.insert(5, 5)
        self.assertEqual(self.linked_list.to_list(), [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9])
        self.assertEqual(self.linked_list.length, 12)
        self.linked_list.insert(0, -1)
        self.assertEqual(self.linked_list.to_list(), [-1, 0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9])
        self.assertEqual(self.linked_list.length, 13)
        self.assertEqual(self.linked_list.head.value, -1)
        self.linked_list.insert(13, 100)
        self.assertEqual(self.linked_list.to_list(), [-1, 0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 100])
        self.assertEqual(self.linked_list.length, 14)
        self.assertEqual(self.linked_list.tail.value, 100)
    
    def test_remove(self):
        self.linked_list.remove(5)
        self.assertEqual(self.linked_list.to_list(), [0, 1, 2, 3, 4, 6, 7, 8, 9])
        self.assertEqual(self.linked_list.length, 9)
        self.linked_list.remove(3)
        self.assertEqual(self.linked_list.to_list(), [0, 1, 2, 4, 6, 7, 8, 9])
        self.assertEqual(self.linked_list.length, 8)
        self.linked_list.remove(0)
        self.assertEqual(self.linked_list.to_list(), [1, 2, 4, 6, 7, 8, 9])
        self.assertEqual(self.linked_list.length, 7)
        self.assertEqual(self.linked_list.head.value, 1)
        removed_value = self.linked_list.remove(6)
        self.assertEqual(removed_value, 9)
        self.assertEqual(self.linked_list.to_list(), [1, 2, 4, 6, 7, 8])
        self.assertEqual(self.linked_list.length, 6)
        self.assertEqual(self.linked_list.tail.value, 8)

    def test_pop(self):
        ls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for _ in range(10):
            self.assertEqual(self.linked_list.pop(), ls.pop())
            self.assertEqual(self.linked_list.to_list(), ls)
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)
    
    def test_left_pop(self):
        ls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for _ in range(10):
            self.assertEqual(self.linked_list.pop(), ls[-1])
            ls = ls[:-1]
            self.assertEqual(self.linked_list.to_list(), ls)
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)

    def test_remove_first(self):
        self.linked_list.remove_first(5)
        self.assertEqual(self.linked_list.to_list(), [0, 1, 2, 3, 4, 6, 7, 8, 9])
        self.assertEqual(self.linked_list.length, 9)
        self.linked_list.remove_first(3)
        self.assertEqual(self.linked_list.to_list(), [0, 1, 2, 4, 6, 7, 8, 9])
        self.assertEqual(self.linked_list.length, 8)
        self.linked_list.remove_first(0)
        self.assertEqual(self.linked_list.to_list(), [1, 2, 4, 6, 7, 8, 9])
        self.assertEqual(self.linked_list.length, 7)
        self.assertEqual(self.linked_list.head.value, 1)
        removed_position = self.linked_list.remove_first(9)
        self.assertEqual(removed_position, 6)
        self.assertEqual(self.linked_list.to_list(), [1, 2, 4, 6, 7, 8])
        self.assertEqual(self.linked_list.length, 6)
        self.assertEqual(self.linked_list.tail.value, 8)
        self.linked_list.append(8)
        self.linked_list.append(8)
        self.linked_list.append(8)
        self.linked_list.append(1)
        removed_position = self.linked_list.remove_first(8)
        self.assertEqual(removed_position, 5)
        self.assertEqual(self.linked_list.to_list(), [1, 2, 4, 6, 7, 8, 8, 8, 1])
        self.assertEqual(self.linked_list.length, 9)
        self.assertEqual(self.linked_list.tail.value, 1)
    
    def test_find_min(self):
        self.assertEqual(self.linked_list.find_min(), 0)
        self.linked_list.append(-1)
        self.assertEqual(self.linked_list.find_min(), -1)
    
    def test_find_max(self):
        self.assertEqual(self.linked_list.find_max(), 9)
        self.linked_list.left_append(11)
        self.assertEqual(self.linked_list.find_max(), 11)

    def test_count(self):
        self.assertEqual(self.linked_list.count(8), 1)
        self.linked_list.append(8)
        self.linked_list.append(8)
        self.linked_list.append(8)
        self.assertEqual(self.linked_list.count(8), 4)
        self.linked_list.remove_first(8)
        self.linked_list.remove_first(8)
        self.linked_list.remove_first(8)
        self.linked_list.remove_first(8)
        self.assertEqual(self.linked_list.count(8), 0)
    
    def test_reverse(self):
        self.empty_linked_list.reverse()
        self.assertEqual(self.empty_linked_list.to_list(), [])
        self.empty_linked_list.append(0)
        self.empty_linked_list.append(1)
        self.empty_linked_list.reverse()
        self.assertEqual(self.empty_linked_list.to_list(), [1, 0])
        self.linked_list.reverse()
        self.assertEqual(self.linked_list.to_list(), [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        self.assertEqual(self.linked_list.head.value, 9)
        self.assertEqual(self.linked_list.tail.value, 0)
        self.linked_list.reverse()
        self.assertEqual(self.linked_list.to_list(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(self.linked_list.head.value, 0)
        self.assertEqual(self.linked_list.tail.value, 9)

if __name__ == '__main__':
    unittest.main()
