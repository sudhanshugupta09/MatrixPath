import unittest
import solve


class TestSolve(unittest.TestCase):

    QUERIES = [((0, 0), (6, 6)), ((1, 1), (4, 4)), ((0, 1), (4, 4)), ((0, 0), (0, 4)), ((0, 0), (6, 3))]
    GRID = [[1, 1, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0, 1, 0],
            [1, 1, 0, 1, 0, 1, 1],
            [0, 1, 1, 1, 0, 1, 1],
            [0, 1, 1, 1, 1, 0, 1],
            [1, 1, 0, 0, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0]]

    def test_path_exists(self):
        self.assertEqual([False], solve.path_exists(self.GRID, [((-1, 0), (6, 3))]))
        self.assertEqual([True], solve.path_exists(self.GRID, [((0, 0), (0, 0))]))
        self.assertEqual([False], solve.path_exists(self.GRID, [((0, 0), (6, 6))]))
        self.assertEqual([False], solve.path_exists(self.GRID, [((1, 1), (4, 4))]))
        self.assertEqual([False], solve.path_exists(self.GRID, [((0, 0), (0, 4))]))
        self.assertEqual([True], solve.path_exists(self.GRID, [((0, 0), (6, 3))]))
        self.assertEqual([False], solve.path_exists(self.GRID, [((-100, 300), (6, 3))]))
        self.assertEqual([], solve.path_exists(self.GRID, []))
        self.assertEqual([False], solve.path_exists([[]], [((-100, 300), (6, 3))]))
        self.assertEqual([False, False, True, False, True], solve.path_exists(self.GRID, [((0, 0), (6, 6)), ((1, 1), (4, 4)), ((0, 1), (4, 4)), ((0, 0), (0, 4)), ((0, 0), (6, 3))]))
        self.assertEqual([False], solve.path_exists(self.GRID, [(('s', 0), (6, 3))]))

