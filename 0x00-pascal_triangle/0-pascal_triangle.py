#!/usr/bin/python3
def pascal_triangle(n):

    """
    Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    Generate Pascal's triangle of n rows and return it as a list of lists.

    Args:
    - n: An integer representing the number of rows to generate in the Pascal's triangle.

    Returns:
    - A list of lists representing the Pascal's triangle of n rows.
    """

    triangle = []
    row = []

    if n <= 0:
        return triangle

    row.append(1)
    triangle.append(row)

    for i in range(1, n):
        current_row = [1]
        for j in range(1, len(row)):
            current_row.append(row[j] + row[j-1])
        current_row.append(1)
        triangle.append(current_row)
        row = current_row

    return triangle

(pascal_triangle(5))
