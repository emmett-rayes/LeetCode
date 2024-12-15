def tribonacci_rec(n: int) -> int:
    def rec(n_3: int, n_2: int, n_1: int, n: int) -> int:
        if n == 0:
            return n_2
        else:
            return rec(n_2, n_1, n_3 + n_2 + n_1, n - 1)

    return rec(0, 0, 1, n)


def tribonacci_iter(n: int) -> int:
    n_3, n_2, n_1 = 0, 0, 1
    for _ in range(n):
        n_3, n_2, n_1 = n_2, n_1, n_3 + n_2 + n_1
    return n_2
