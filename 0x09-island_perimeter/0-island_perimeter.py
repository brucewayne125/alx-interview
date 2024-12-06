#!/usr/bin/python3
# island_perimeter: is a function returns the perimeter of the island.
# return: returns the perimeter of the island by taking the total sum.


def island_perimeter(grid):
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
