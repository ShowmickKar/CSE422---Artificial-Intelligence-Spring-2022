def count_survivors(grid):
    survivor = 0
    for row in grid:
        for cell in row:
            if cell == "H":
                survivor += 1
    return survivor


def minimum_num_of_minutes(grid, n, m):
    time_spent = 0
    survivors = [None]
    while count_survivors(grid):
        survivors.append(count_survivors(grid))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "A":
                    if i + 1 < n and grid[i + 1][j] == "H":
                        grid[i + 1][j] = "Infected"
                    if i - 1 >= 0 and grid[i - 1][j] == "H":
                        grid[i - 1][j] = "Infected"
                    if j + 1 < m and grid[i][j + 1] == "H":
                        grid[i][j + 1] = "Infected"
                    if j - 1 >= 0 and grid[i][j - 1] == "H":
                        grid[i][j - 1] = "Infected"
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "Infected":
                    grid[i][j] = "A"
        if count_survivors(grid) != survivors[-1]:
            time_spent += 1
        else:
            break
    survivors = count_survivors(grid)
    return time_spent, survivors


def read(filename):
    file = open("tests/" + filename, "r")
    n = int(file.readline().strip())
    m = int(file.readline().strip())
    grid = []
    while True:
        line = file.readline().strip()
        if line == "":
            break
        grid.append(list(line.replace(" ", "")))
    file.close()
    return n, m, grid


def write(filename, time_spent, survivors):
    file = open("tests/" + filename, "w")
    line = f"Time spent: {time_spent} minute(s)\n"
    file.write(line)
    line = ("No one" if int(survivors) == 0 else survivors) + " survived\n"
    file.write(line)
    file.close()


""" Driver Code """
n, m, grid = read("q2i1.txt")
time, survived = minimum_num_of_minutes(grid, n, m)
print(time, survived)
write("q2o1.txt", str(time), str(survived))

n, m, grid = read("q2i2.txt")
time, survived = minimum_num_of_minutes(grid, n, m)
print(time, survived)
write("q2o2.txt", str(time), str(survived))
