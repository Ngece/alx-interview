#!/usr/bin/python3

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    Returns an empty list if n <= 0.
    """

    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                prev_row = triangle[i - 1]
                value = prev_row[j - 1] + prev_row[j]
                row.append(value)
        triangle.append(row)

    return triangle
