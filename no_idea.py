# https://www.hackerrank.com/challenges/no-idea/problem


if __name__ == "__main__":
    lines = [[3, 2], [1, 5, 3], [3, 1], [5, 7]]
    n, m = lines[0][0], lines[0][1]
    if not (1 <= n <= 10 ** 5 and 1 <= m <= 10 ** 5):
        assert False

    values = lines[1]
    cA, cB = set(lines[-2]), set(lines[-1])
    assert sum([(i in cA) - (i in cB) for i in values]) == 1
