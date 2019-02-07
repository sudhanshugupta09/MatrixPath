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
        self.assertTrue(solve.path_exists(self.GRID, ((0, 0), (6, 6))))