# Importation de la fonction random 
import random

#  Variable des caractères de notre générateur 
cara = 'abecefghijklmonpqrstuwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@$*'

# variable question - nombre de mdp à générer  
nombre = input('nombre de mot de passe à générer : ')
# On stock la réponse dans la variable nombre
nombre = int(nombre)

# variable question - longueur du mot de passe à générer 
longueur = input('Longueur du mot de passe à générer : ')
# On stock la réponse dans la variable longueur
longueur = int(longueur)

# boucle pour ajouter un mdp en fonction de la variable nombre 
for n in range(nombre) :
    password = ''
    # boucle pour ajouter un nombre aléatoire en fonction de la variable longueur 
    for l in range(longueur) :
        password += random.choice(cara)
        # On affiche le mot de passe générer 
    print(password)



