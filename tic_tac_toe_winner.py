from typing import List


def search(refs, moves) -> bool:
    for ref in refs:
        for move in ref:
            if move not in moves:
                break
        else:
            return True
    return False


def winning(moves: List[List[int]]) -> bool:
    rows = [[[i, 0], [i, 1], [i, 2]] for i in range(3)]
    cols = [[[0, j], [1, j], [2, j]] for j in range(3)]
    diag = [[[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]]]
    return search(rows, moves) or search(cols, moves) or search(diag, moves)


def tic_tac_toe_winner(moves: List[List[int]]) -> str:
    if winning(moves[0::2]):
        return "A"
    if winning(moves[1::2]):
        return "B"
    if len(moves) == 9:
        return "Draw"
    else:
        return "Pending"
