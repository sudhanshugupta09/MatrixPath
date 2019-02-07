"""
Instructions:
    - Implement the function `path_exists` below.
    - Save this file as `{first_name}_{last_name}_solve.py`.

Constraints:
    - Your solution will be run in a Python2.7 environment.
    - Only python standard library imports can be used and they must be imported
      within `path_exists`.
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
        - A path must consist of the same values. i.e. if grid[i1][j1] == 1, the path is
          comprised of only 1's.

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

    # def display_grid(grid):
    #     for row in grid:
    #         print(row)

    def check_valid_neighbors(row, col):
        row_check = [-1, 1, 0, 0]
        col_check = [0, 0, -1, 1]
        valid_neighbors_list = []

        for r_move, c_move in zip(row_check, col_check):
            if 0 <= row + r_move < row_max and 0 <= col + c_move < col_max:
                # print('row value being checked')
                # print(row+r)
                # print('col value being checked')
                # print(col+c)
                if grid[row+r_move][col+c_move] and not visited[row+r_move][col+c_move]:
                    valid_neighbors_list.append((row+r_move, col+c_move))
                    # print('location to be updated row: {} and col: {}'.format(row + r, col + c))
                    # x = row+r
                    # y = col+c
                    # print('x', x)
                    # print('y', y)
                    visited[row+r_move][col+c_move] = True
                    # print('--- in function call----')
                    # display_grid(visited)
                    # print('--- after function call----')
        return valid_neighbors_list, visited


    # def is_valid_input(start_row_idx, start_col_idx , end_row_idx, end_col_idx):
    #     rows = len(grid)
    #     cols = len(grid[0])
    #     if start_row_idx < 0 or start_row_idx >= rows or grid[start_row_idx][start_col_idx] != 1
    #         or end_row_idx < 0 or end_row_idx >= rows or :

    if queries:
        # print(len(queries))
        result = [False] * len(queries)
    else:
        return []
    # result = []
    ## housekeeping check:
    if not grid:
        return result

    row_max = len(grid)
    col_max = len(grid[0])



    queue = []

    for i, query in enumerate(queries):
        start_row_idx = query[0][0]
        start_col_idx = query[0][1]
        end_row_idx = query[1][0]
        end_col_idx = query[1][1]

        ## Validate the query input
        #
        # if start_row_idx < 0 or start_row_idx >= row_max or \
        #     start_col_idx < 0 or start_col_idx >= col_max or \
        #     end_row_idx < 0 or end_row_idx >= row_max or \
        #     end_col_idx < 0 or end_col_idx >= col_max:
        #
        #     raise ValueError("Invalid indexes provided in query input")


        # print(start_row_idx)
        # print(start_col_idx)

        visited = [[False for _ in range(col_max)] for _ in range(col_max)]


        ## If the value at start-index or value at end-index is not 1
        try:
            if not grid[start_row_idx][start_col_idx] or not grid[end_row_idx][end_col_idx]:
                # result.append(False)
                # print('not valid')
                continue
        except IndexError:
            print("Invalid indexes passed in query number: {} \ninput value {}".format(i, query))
            continue

        # print('still going on')
        queue.append((start_row_idx, start_col_idx))

        while queue:
            # print('queue', queue)
            node = queue.pop(0)
            # print('popped node', node)
            # print('pop queue', queue)
            # print('node 0: ', node[0])
            # print(end_row_idx)
            # print('node 1: ', node[1])
            # print(end_col_idx)
            if node[0] == end_row_idx and node[1] == end_col_idx:
                # print('result found!!')
                result[i] = True
                break
            visited[node[0]][node[1]] = True
            valid_neighbors, visited = check_valid_neighbors(node[0], node[1])
            # display_grid(visited)
            # if valid_neighbors:
                # print('list extended')
            queue.extend(valid_neighbors)
            # else:
            #     print('empty neighbors')
        # result.append(False)
        # print('after processing')
        # print(visited)
    return result
    # raise NotImplementedError


# queries = [((-1, 1), (4, 8)), ((1, 1), (4, 4)), ((0, 1), (4, 4))]
QUERIES = [((0, 0), (6, 6)), ((1, 1), (4, 4)), ((0, 1), (4, 4)), ((0, 0), (0, 4)), ((0, 0), (6, 3))]
GRID = [[1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 0],
        [1, 1, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 0, 1],
        [1, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0]]
print(path_exists(GRID, QUERIES))
