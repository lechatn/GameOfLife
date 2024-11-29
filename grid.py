import random
import os


def initial_grid(size) :
    '''creer la grid et la remplie avec des valeurs aleatoires'''
    grille = []
    for i in range(size) :
        inter_grid = []
        for j in range(size) :
            inter_grid.append(random.randint(0, 1))
        grille.append(inter_grid)

    return grille


def empty_grid(taille) :
    '''creer une grid vide'''
    grille = []
    for i in range(taille) :
        inter_grid = []
        for j in range(taille) :
            inter_grid.append(0)
        grille.append(inter_grid)

    return grille

def print_grid(grille):
    ''''affiche la grid dans le terminal en remplacant les 1 par des carres blancs et les 0 par des carres noirs'''
    os.system('cls' if os.name == 'nt' else 'clear') 
    for ligne in grille:
        print(" ".join('⬜' if cell == 1 else '⬛' for cell in ligne))        
def ask_length() :
    while True :
        try :
            taille = int(input("Entrez la taille de la grille (entre 5 et 45) : "))
            if 5 <= taille <= 45:
                return taille
            else:
                print("Veuillez entrer un nombre entier entre 5 et 45")
        except ValueError:
            print("Veuillez entrer un nombre entier")