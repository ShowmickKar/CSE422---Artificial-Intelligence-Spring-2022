def max_infected_region(grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[False for j in range(m)] for i in range(n)]
    area = 0
    round = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            if grid[i][j] == "Y":
                round += 1
                area = max(area, backtrack(grid, i, j, visited))
    return area


def backtrack(grid, i, j, visited, area=0):
    if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or visited[i][j] or grid[i][j] == "N":
        return area
    visited[i][j] = True
    area += 1
    area = backtrack(grid, i + 1, j, visited, area)
    area = backtrack(grid, i, j + 1, visited, area)
    area = backtrack(grid, i + 1, j + 1, visited, area)
    area = backtrack(grid, i - 1, j, visited, area)
    area = backtrack(grid, i, j - 1, visited, area)
    area = backtrack(grid, i - 1, j - 1, visited, area)
    area = backtrack(grid, i - 1, j + 1, visited, area)
    area = backtrack(grid, i + 1, j - 1, visited, area)
    return area


def read(filename):
    file = open("tests/" + filename, "r")
    grid = []
    while True:
        line = file.readline().strip()
        if line == "":
            break
        grid.append(list(line.replace(" ", "")))
    file.close()
    return grid


def write(filename, result):
    file = open("tests/" + filename, "w")
    file.write(result)
    file.close()


""" Drive Code """
grid = read("q1i1.txt")
result = max_infected_region(grid)
write("q1o1.txt", str(result))

grid = read("q1i2.txt")
result = max_infected_region(grid)
write("q1o2.txt", str(result))
