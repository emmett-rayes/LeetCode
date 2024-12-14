from typing import List

Combination = tuple[int, ...]
Instance = tuple[int, Combination]
Result = set[Combination]


def change_rec(amount: int, coins: List[int]) -> int:
    cache: dict[Instance, Result] = {}

    def rec(instance: Instance) -> Result:
        if instance in cache:
            return cache[instance]

        (a, c) = instance
        if a < 0 or len(c) == 0:
            return set()
        if a == 0:
            return {(a,)}

        result = set()
        for solution in rec((a, c[1:])):
            result.add(tuple(sorted(solution)))

        for solution in rec((a - c[0], c)):
            result.add((c[0],) + tuple(sorted(solution)))

        cache[instance] = result
        return result

    combinations = rec((amount, tuple(coins)))
    return len(combinations)


def change_dp(amount: int, coins: List[int]) -> int:
    # initialization
    dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
    dp[0][0] = 1

    # tabulation
    for i in range(1, len(dp)):
        for j in range(len(dp[i])):
            dp[i][j] = dp[i - 1][j] + (dp[i][j - coins[i - 1]] if 0 <= j - coins[i - 1] < len(dp[i]) else 0)
    return dp[-1][-1]


def change_dp_space_optimized(amount: int, coins: List[int]) -> int:
    # initialization
    dp_prev = [0 for _ in range(amount + 1)]
    dp = [0 for _ in range(amount + 1)]
    dp_prev[0] = 1

    # tabulation
    for i in range(1, len(coins) + 1):
        for j in range(len(dp)):
            dp[j] = dp_prev[j] + (dp[j - coins[i - 1]] if 0 <= j - coins[i - 1] < len(dp) else 0)
        (dp_prev, dp) = (dp, dp_prev)
    return dp_prev[-1]
