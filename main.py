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
    # Check if a saved grid exists
    if os.path.exists("grille.txt"):
        choice = input("Voulez-vous (n)ouvelle grille ou (r)écupérer la grille sauvegardée? (n/r): ")
        if choice.lower() == 'r':
            with open("grille.txt", "r") as file:  # Load the saved grid
                grille = [list(map(int, line.split())) for line in file]
        else:
            grille = initial_grid(int(input("Entrez la taille de la grille : ")))
    else:
        grille = initial_grid(int(input("Entrez la taille de la grille : ")))

    history = []  # To store previous grid states
    i = 0
    while True:
        i += 1
        print_grid(grille)
        
        # Check for cycles
        if grille in history:
            cycle_start = history.index(grille)
            cycle_length = i - cycle_start
            print(f"Cycle detected! Starts at generation {cycle_start}, length {cycle_length}.")
        
        history.append(grille)  # Store the current grid state
        
        with open("grille.txt", "w") as file:
            for row in grille:
                file.write(" ".join(map(str, row)) + "\n")
        
        # Prompt for user input to continue or quit
        user_input = input("Appuyez sur Enter pour passer au tour suivant ou 'q' pour quitter: ")
        if user_input.lower() == 'q':  # Check if the user wants to quit
            print("Merci d'avoir joué!")
            break  # Exit the loop and end the game

        print("Tour", i)
        grille = stage(grille)  # Calculer la prochaine génération

jouer()