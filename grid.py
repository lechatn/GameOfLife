import random
import os


def initial_grid(size) :
    '''creer la grid et la remplie avec des valeurs aleatoires'''
    grid = []
    for i in range(size) :
        inter_grid = []
        for j in range(size) :
            inter_grid.append(random.randint(0, 1))
        grid.append(inter_grid)

    return grid


def empty_grid(size) :
    '''creer une grid vide'''
    grid = []
    for i in range(size) :
        inter_grid = []
        for j in range(size) :
            inter_grid.append(0)
        grid.append(inter_grid)

    return grid

def print_grid(grid):
    ''''affiche la grid dans le terminal en remplacant les 1 par des carres blancs et les 0 par des carres noirs'''
    os.system('cls' if os.name == 'nt' else 'clear') 
    for row in grid:
        print(" ".join('⬜' if cell == 1 else '⬛' for cell in row))        
def ask_length() :
    while True :
        try :
            size = int(input("Entrez la taille de la grille (entre 5 et 45) : "))
            if 5 <= size <= 45:
                return size
            else:
                print("Veuillez entrer un nombre entier entre 5 et 45")
        except ValueError:
            print("Veuillez entrer un nombre entier")