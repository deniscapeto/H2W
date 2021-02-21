from typing import List


def create_matrix(x_size: int, y_size: int) -> List[List]:
    """
    Create a matrix with `x_size` x `y_size`
    """
    matrix = [list(range(y_size))] * x_size
    return matrix


def main():
    """
    Iterates in a matrix with 5 x 7 with only one for-loop

    The sub-lists should be with a fix size, emulating a matrix.
    """
    x_size = 5
    y_size = 7

    matrix = create_matrix(x_size, y_size)

    print(f'Matrix: {matrix}\n')

    for n in range(x_size * y_size):
        j = n % x_size  # Extracts sub-index
        # We need to use '//' to force integer division;
        i = (n - j) // y_size  # Extract first index

        print(f'matrix[{i}][{j}] = {matrix[i][j]}')


if __name__ == '__main__':
    main()
