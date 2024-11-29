import tkinter as tk
from tkinter import simpledialog
import random
import os
from grid import empty_grid, initial_grid
from play import stage

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

        self.controls = tk.Frame(self.root)
        self.controls.pack()
        self.next_button = tk.Button(self.controls, text="Tour Suivant", command=self.next_turn)
        self.next_button.pack(side=tk.LEFT)
        self.auto_button = tk.Button(self.controls, text="Auto", command=self.toggle_auto)
        self.auto_button.pack(side=tk.LEFT)
        self.save_button = tk.Button(self.controls, text="Sauvegarder", command=self.save_grid)
        self.save_button.pack(side=tk.LEFT)
        self.load_button = tk.Button(self.controls, text="Charger", command=self.load_grid)
        self.load_button.pack(side=tk.LEFT)

        self.auto_mode = False  
        self.draw_grid()

    def demander_taille_grille(self):
        taille = simpledialog.askinteger("Taille de la grille", "Entrez la taille de la grille (min : 5, max : 45) :", minvalue=5, maxvalue=45)
        return taille or 20  

    def draw_grid(self):
        self.canvas.delete("all")
        for y, row in enumerate(self.grille):
            for x, cell in enumerate(row):
                color = "black" if cell == 0 else "green"
                self.canvas.create_rectangle(
                    x * 20, y * 20, (x + 1) * 20, (y + 1) * 20,
                    fill=color, outline="white"
                )

    def next_turn(self):
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
        self.auto_mode = not self.auto_mode
        if self.auto_mode:
            self.next_turn()

    def save_grid(self):
        with open("grille.txt", "w") as file:
            for row in self.grille:
                file.write(" ".join(map(str, row)) + "\n")
        print("Grille sauvegardée.")

    def load_grid(self):
        if os.path.exists("grille.txt"):
            with open("grille.txt", "r") as file:
                self.grille = [list(map(int, line.split())) for line in file]
            print("Grille chargée.")
            self.draw_grid()
        else:
            print("Aucun fichier de sauvegarde trouvé.")