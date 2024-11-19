import random


def main() :
    name = input("Enter the size of the grid: ")
    size = int(name)

    grid = create_grid(size)
    print_grid(grid)


def create_grid(size) :
    grid = []
    for i in range(size) :
        inter_grid = []
        for j in range(size) :
            inter_grid.append(random.randint(0, 1))
        grid.append(inter_grid)

    return grid


def print_grid(grid) :
    for i in range(len(grid)) :
        for j in range(len(grid[i])) :
            print(grid[i][j], end = " ")
        print()           
            

main()