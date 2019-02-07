"""
Instructions:
    - Implement the function `path_exists` below.
    - Save this file as `{first_name}_{last_name}_solve.py`.

Constraints:
    - Your solution will be run in a Python2.7 environment.
    - Only python standard library imports can be used and they must be imported within `path_exists`.
    - The function signature of `path_exists` cannot be modified.
    - Additional functions can be included, but must be defined within `path_exists`.
    - There will be two sets of input, small and large, each with different time limits.
"""


def path_exists(grid, queries):
    """
    Determines whether for every start=(i1, j1) -> end=(i2, j2) query in `queries`,
    there exists a path in `grid` from start to end.

    The rules for a path are as follows:
        - A path consists of only up-down-left-right segments (no diagonals).
        - A path must consist of the same values. i.e. if grid[i1][j1] == 1, the path is comprised of only 1's.

    Examples:
        grid (visual only)

                1 0 0
                1 1 0
                0 1 1

        start     end       answer
        (0, 0) -> (2, 2)    True
        (2, 0) -> (0, 2)    False


    :param grid:        The grid on which `queries` are asked.
    :type grid:         list[list[int]], values can only be [0, 1].
    :param queries:     A set of queries for `grid`. Queries will be non-trivial.
    :type queries:      Iterable, contains elements of type tuple[tuple[int, int]].

    :return:            The result for each query, whether a path exists from start -> end.
    :rtype:             list[bool]
    """


    '''
    Edge Cases : input not valid
    Cases:
        only 1 1
        dfs breaks
    '''


    def check_valid_neighbors(row, col, row_max, col_max):
        row_check = [-1, 1, 0, 0]
        col_check = [0, 0, -1, 1]
        valid_neighbors = []

        for r ,c in zip(row_check, col_check):
            if row + r >= 0 and row + r < row_max and col + c >= 0 and col + c < col_max:
                if grid[row+r][col+c]:
                    valid_neighbors.append((row+r, col+c))
        return valid_neighbors


    # def is_valid_input(start_row_idx, start_col_idx , end_row_idx, end_col_idx):
    #     rows = len(grid)
    #     cols = len(grid[0])
    #     if start_row_idx < 0 or start_row_idx >= rows or grid[start_row_idx][start_col_idx] != 1
    #         or end_row_idx < 0 or end_row_idx >= rows or :

    if queries:
        print(len(queries))
        result = [False] * len(queries)
    else:
        return []
    # result = []
    ## housekeeping check:
    if not grid:
        return result

    row_max = len(grid)
    col_max = len(grid[0])

    visited = [[False] * col_max] * row_max

    queue = []

    for i, query in enumerate(queries):
        start_row_idx = query[0][0]
        start_col_idx = query[0][1]
        end_row_idx = query[0][0]
        end_col_idx = query[0][1]

        ## If the value at start-index or value at end-index is not 1
        if not grid[start_row_idx][start_col_idx] and not grid[end_row_idx][end_col_idx]:
            # result.append(False)
            result[i] = False
            break

        queue.append((start_row_idx, start_col_idx))

        while queue:
            node = queue.pop()
            if node[0] == end_row_idx and node[1] == end_col_idx:
                # result.append(True)
                result[i] = True
                break
            valid_neighbors = check_valid_neighbors(node[0], node[1], row_max, col_max)
            if not valid_neighbors:
                # result.append(False)
                result[i] = False
                break
            else:
                queue.extend(valid_neighbors)
        result[i] = False
        # result.append(False)
    return result
    # raise NotImplementedError


queries = [((0, 0), (6, 6)), ((1, 1), (4, 4)), ((0,), (4, 4)), ((0, 0), (0, 4)), ((0, 0), (6, 3))]
grid = [[1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 0],
        [1, 1, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 0, 1],
        [1, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0]]
print(path_exists(grid, queries))