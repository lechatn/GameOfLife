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

def print_grid(grid) :
    for i in range(len(grid)) :
        for j in range(len(grid[i])) :
            print(grid[i][j], end = " ")
        print()           


def stage(grille) :
    HAUTEUR = len(grille)
    LARGEUR = HAUTEUR
    nouvelle_grille = empty_grid(len(grille))
    for y in range(HAUTEUR):
        for x in range(LARGEUR):
            voisins = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1), (1, 0), (1, 1)
            ]
            voisins_vivants = 0

            for dy, dx in voisins:
                ny, nx = y + dy, x + dx
                if 0 <= ny < HAUTEUR and 0 <= nx < LARGEUR:
                    voisins_vivants += grille[ny][nx]

            # Appliquer les règles du jeu
            if grille[y][x] == 1:  # Cellule vivante
                if voisins_vivants == 2 or voisins_vivants == 3 :  # Meurt si elle n'a pas 2 voisins vivants
                    nouvelle_grille[y][x] = 1
                else:
                    nouvelle_grille[y][x] = 0  # Reste vivante si elle a 2 voisins vivants
            elif grille[y][x] == 0 and voisins_vivants == 3:
                nouvelle_grille[y][x] = 1  # Cellule morte devient vivante si elle a 3 voisins vivants

    return nouvelle_grille



def jouer():
    grille = initial_grid(int(input("Entrez la taille de la grille : ")))
    while True:
        print_grid(grille)
        input("Appuyez sur Enter pour passer au tour suivant...")  # Attendre que l'utilisateur appuie sur Entrée
        grille = stage(grille)  # Calculer la prochaine génération

jouer()