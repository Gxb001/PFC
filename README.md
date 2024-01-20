# Pierre Feuille Ciseaux

Ce script Python implémente le jeu "Pierre Feuille Ciseaux" avec une interface graphique utilisant Tkinter. Le jeu consiste à faire un choix entre pierre, feuille ou ciseaux, et l'ordinateur génère également un choix de manière aléatoire. Les résultats du jeu sont affichés dans des fenêtres contextuelles.

## Installation des dépendances

Le script utilise la bibliothèque Tkinter pour l'interface graphique. Aucune installation supplémentaire n'est nécessaire car Tkinter est inclus dans la plupart des distributions Python par défaut.

## Comment jouer

1. Lancez le script en exécutant le fichier Python.
2. Une fenêtre s'ouvrira, affichant le titre du jeu et un message de bienvenue.
3. Cliquez sur l'un des boutons "Pierre", "Feuille" ou "Ciseaux" pour faire votre choix.
4. Une fenêtre contextuelle s'ouvrira, affichant le résultat du jeu contre l'ordinateur.

## Fonctionnement du code

Le code est organisé de la manière suivante :

- Il utilise Tkinter pour créer une fenêtre graphique.
- Trois fonctions (`create1`, `create2`, et `create3`) sont définies pour générer le résultat du jeu pour les choix de pierre, feuille et ciseaux respectivement.
- Chaque fonction crée une fenêtre contextuelle avec le résultat du jeu (gagné, perdu, égalité) et se ferme automatiquement après une seconde.
- Trois boutons (`pierre_button`, `feuille_button`, et `ciseau_button`) sont ajoutés à la fenêtre principale pour permettre à l'utilisateur de faire son choix.

L'interface graphique est personnalisée avec des couleurs et des polices pour une expérience utilisateur agréable.

## Exécution du script

Assurez-vous que Python est installé sur votre système, puis exécutez le script en utilisant la commande suivante dans votre terminal :

```bash
python main.py
