# Ecrire un scrip


a = 520

while True:

    entree = input("Entrez un nombre entre 1 et 1000 puis entree faites 'q' pour quitter:")

    if entree == 'q':
        break
    elif not entree.isnumeric():
        print("Vous devez entrer un nombre entier.")

    elif int(entree) <= 0:
        print("Entrez un nombre plus grand ou egal a 1.")
        continue

    elif int(entree) > 1000:
        print("Entrez un nombre plus petit ou egal a 100.")
        continue

    elif int(entree) < a:
        print("plus grand.")
        continue # commande au choix

    elif int(entree) <= 0:
        print("plus petit")
        continue

    elif int(entree) == a:
        print("GAGNE !!!")
        break




