Ce projet est une implémentation en Python du célèbre Jeu de la Vie, un automate cellulaire imaginé par John Conway.

🌟 Fonctionnalités
Simule l'évolution d'une grille de cellules vivantes et mortes.
Respecte les règles classiques : sous-population, surpopulation, équilibre, reproduction.
Affiche la grille qui évolue génération après génération.

📋 Règles du Jeu
Une cellule vivante :
  Meurt avec moins de 2 voisins (sous-population).
  Meurt avec plus de 3 voisins (surpopulation).
  Survit avec 2 ou 3 voisins.
Une cellule morte devient vivante si elle a exactement 3 voisins (reproduction).

🚀 Pour lancer le projet
  `python main.py`
