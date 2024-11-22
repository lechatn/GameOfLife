import random
import os


def initial_grid(size) :
    grid = []
    for i in range(size) :
        inter_grid = []
        for j in range(size) :
            inter_grid.append(random.randint(0, 1))
        grid.append(inter_grid)

    return grid


def empty_grid(size) :
    grid = []
    for i in range(size) :
        inter_grid = []
        for j in range(size) :
            inter_grid.append(0)
        grid.append(inter_grid)

    return grid

def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')  # Nettoyer l'écran
    for row in grid:
        print(" ".join('⬜' if cell == 1 else '⬛' for cell in row))        