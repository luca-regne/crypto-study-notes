def bytes2matrix(text: str) -> list[int]:
    """Converts a 16-byte array into a 4x4 matrix."""
    return [list(text[i : i + 4]) for i in range(0, len(text), 4)]


def matrix2bytes(matrix: list[int]) -> str:
    """Converts a 4x4 matrix into a 16-byte array."""
    return "".join([chr(i) for r in matrix for i in r])


matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

if __name__ == '__main__':
    print(matrix2bytes(matrix))
