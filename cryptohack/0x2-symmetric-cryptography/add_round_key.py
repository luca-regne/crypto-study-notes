from matrix import matrix2bytes

state = [
    [206, 243, 61, 34],
    [175, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    rounded = []
    for i in range(4):
        t = []
        for j in range(4):
            t.append(s[i][j] ^ k[i][j])
        rounded.append(t)
    return rounded


if __name__ == "__main__":
    print(matrix2bytes(add_round_key(state, round_key)))
