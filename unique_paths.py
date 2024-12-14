from typing import List


def unique_paths_rec(grid: List[List[int]]) -> int:
    def neighbors(i: int, j: int) -> List[tuple[int, ...]]:
        result = []
        if i < len(grid) - 1:
            result.append((i + 1, j))
        if j < len(grid[i]) - 1:
            result.append((i, j + 1))

        return [(i_next, j_next) for (i_next, j_next) in result if grid[i_next][j_next] == 0]

    def dfs(i: int, j: int, visited: set[tuple[int, ...]]) -> int:
        if i == len(grid) - 1 and j == len(grid[i]) - 1:
            return 1 if grid[-1][-1] == 0 else 0

        count = 0
        for indices in neighbors(i, j):
            if indices in visited:
                continue
            visited.add(indices)
            count += dfs(*indices, visited=visited)
            visited.remove(indices)

        return count

    if grid[0][0] == 1:
        return 0
    else:
        return dfs(0, 0, {(0, 0)})


def unique_paths_dp(grid: List[List[int]]) -> int:
    dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            if i == 0 and j == 0:
                if grid[0][0] == 1:
                    return 0
                else:
                    dp[0][0] = 1
            else:
                dp[i][j] = 0 if grid[i][j] == 1 else \
                    (dp[i - 1][j] if 0 < i else 0) + (dp[i][j - 1] if 0 < j else 0)
    return dp[-1][-1]


def unique_paths_dp_space_optimized(grid: List[List[int]]) -> int:
    dp = 0
    dp_prev = [0 for _ in range(len(grid[0]))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == 0 and j == 0:
                if grid[0][0] == 1:
                    return 0
                else:
                    dp = 1
            else:
                dp = 0 if grid[i][j] == 1 else dp_prev[j] + (0 if j == 0 else dp_prev[j - 1])
            dp_prev[j] = dp
    return dp


print(unique_paths_dp_space_optimized([[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))
