#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):

    """
Calculates the perimeter of the island as described.

:param grid: List of list of integers where:
             0 represents water
             1 represents land
:return: Integer representing the perimeter of the island
"""
    columns = len(grid[0])
    rows = len(grid)
    perimeter = 0

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == columns - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
