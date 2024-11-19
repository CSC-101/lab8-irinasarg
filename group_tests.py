import unittest
import group

class TestCases(unittest.TestCase):

    def test_groups_of_3_1(self):
        input = [1, 2, 3, 4, 5, 6]
        expected = [[1, 2, 3], [4, 5, 6]]
        result = group.groups_of_3(input)
        self.assertEqual(result, expected)




    if __name__ == "__main__":
        unittest.main()