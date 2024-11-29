from grid import empty_grid, print_grid, initial_grid, ask_length
import os

def stage(grille) :
    '''permet de faire evoluer la grille'''
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

            if grille[y][x] == 1: 
                if voisins_vivants == 2 or voisins_vivants == 3 :  
                    nouvelle_grille[y][x] = 1
                else:
                    nouvelle_grille[y][x] = 0  
            elif grille[y][x] == 0 and voisins_vivants == 3:
                nouvelle_grille[y][x] = 1  

    return nouvelle_grille

def jouer():
    '''Fonction principale pour jouer au jeu de la vie '''
    if os.path.exists("grille.txt"):
        choix = input("Voulez-vous (n)ouvelle grille ou (r)écupérer la grille sauvegardée? (n/r): ")
        if choix.lower() == 'r':
            with open("grille.txt", "r") as file:  
                grille = [list(map(int, line.split())) for line in file]
        else:
            grille = initial_grid(ask_length())
    else:
        grille = initial_grid(ask_length())

    derniere = []  
    i = 0
    while True:
        i += 1
        print_grid(grille)
        
        # Check for cycles
        if grille in derniere:
            debut_cycle = derniere.index(grille)
            longueur_cyvle = i - debut_cycle
            print(f"Cycle detecté! Débute à la génération {debut_cycle}, longueur {longueur_cyvle}.")
        
        derniere.append(grille) 
        
        with open("grille.txt", "w") as file:
            for ligne in grille:
                file.write(" ".join(map(str, ligne)) + "\n")
        
        # Prompt for user input to continue or quit
        user_input = input("Appuyez sur Enter pour passer au tour suivant ou 'q' pour quitter: ")
        if user_input.lower() == 'q':  
            print("Merci d'avoir joué!")
            break  

        print("Tour", i)
        grille = stage(grille) 