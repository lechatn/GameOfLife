import tkinter as tk
from tkinter import simpledialog
import random
import os

# Fonctions de la grille
def initial_grid(size):
    return [[random.randint(0, 1) for _ in range(size)] for _ in range(size)]

def empty_grid(size):
    return [[0 for _ in range(size)] for _ in range(size)]

def stage(grille):
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
                if voisins_vivants == 2 or voisins_vivants == 3:
                    nouvelle_grille[y][x] = 1
                else:
                    nouvelle_grille[y][x] = 0
            elif grille[y][x] == 0 and voisins_vivants == 3:
                nouvelle_grille[y][x] = 1
    return nouvelle_grille

# Classe pour gérer l'interface Tkinter
class JeuDeLaVie:
    def __init__(self, root):
        self.root = root
        self.taille = self.demander_taille_grille() 
        self.grille = initial_grid(self.taille)
        self.cellules = []
        self.history = []
        self.cycle_detected = False

        self.root.title("Jeu de la Vie")
        self.root.geometry(f"{self.taille * 20}x{self.taille * 20 + 50}")
        
        self.canvas = tk.Canvas(self.root, width=self.taille * 20, height=self.taille * 20, bg="white")
        self.canvas.pack()

        # Boutons de contrôle
        self.controls = tk.Frame(self.root)
        self.controls.pack()
        self.next_button = tk.Button(self.controls, text="Tour Suivant", command=self.next_turn)
        self.next_button.pack(side=tk.LEFT)
        self.auto_button = tk.Button(self.controls, text="Auto (Toggle)", command=self.toggle_auto)
        self.auto_button.pack(side=tk.LEFT)
        self.save_button = tk.Button(self.controls, text="Sauvegarder", command=self.save_grid)
        self.save_button.pack(side=tk.LEFT)
        self.load_button = tk.Button(self.controls, text="Charger", command=self.load_grid)
        self.load_button.pack(side=tk.LEFT)

        self.auto_mode = False  
        self.draw_grid()

    def demander_taille_grille(self):
        """Demande à l'utilisateur la taille de la grille."""
        taille = simpledialog.askinteger("Taille de la grille", "Entrez la taille de la grille (min : 5, max : 45) :", minvalue=5, maxvalue=45)
        return taille or 20  

    def draw_grid(self):
        """Dessine la grille sur le canevas."""
        self.canvas.delete("all")
        for y, row in enumerate(self.grille):
            for x, cell in enumerate(row):
                color = "black" if cell == 0 else "green"
                self.canvas.create_rectangle(
                    x * 20, y * 20, (x + 1) * 20, (y + 1) * 20,
                    fill=color, outline="white"
                )

    def next_turn(self):
        """Passe au tour suivant."""
        if self.grille in self.history:
            if not self.cycle_detected:
                self.cycle_detected = True
                cycle_start = self.history.index(self.grille)
                cycle_length = len(self.history) - cycle_start
                print(f"Cycle détecté! Débute à la génération {cycle_start}, longueur {cycle_length}.")
        else:
            self.cycle_detected = False

        self.history.append(self.grille)
        self.grille = stage(self.grille)
        self.draw_grid()

        if self.auto_mode:
            self.root.after(200, self.next_turn) 

    def toggle_auto(self):
        """Active ou désactive le mode automatique."""
        self.auto_mode = not self.auto_mode
        if self.auto_mode:
            self.next_turn()

    def save_grid(self):
        """Sauvegarde la grille actuelle dans un fichier."""
        with open("grille.txt", "w") as file:
            for row in self.grille:
                file.write(" ".join(map(str, row)) + "\n")
        print("Grille sauvegardée.")

    def load_grid(self):
        """Charge une grille depuis un fichier."""
        if os.path.exists("grille.txt"):
            with open("grille.txt", "r") as file:
                self.grille = [list(map(int, line.split())) for line in file]
            print("Grille chargée.")
            self.draw_grid()
        else:
            print("Aucun fichier de sauvegarde trouvé.")

if __name__ == "__main__":
    root = tk.Tk()
    jeu = JeuDeLaVie(root)
    root.mainloop()
