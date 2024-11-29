from play import jouer
from graphic import JeuDeLaVie
import tkinter as tk


if __name__ == "__main__":
    choice = input("Voulez-vous jouer en mode (g)raphique ou (c)onsole? (g/c): ")
    if choice.lower() == 'g':
        root = tk.Tk()
        jeu = JeuDeLaVie(root)
        root.mainloop()
    else:
        jouer()