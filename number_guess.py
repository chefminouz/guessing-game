import random

def number_guess():
    #Input de l'entier Minimum avec gestion des erreurs
    while True:
        try:
            x = int(input("Définis l'entier Mininimum : "))
            break
        except ValueError:
            print("Tu dois choisir un nombre entier !!")

    #Input de l'entier Maximum avec gestion des erreurs
    while True :         
        try:     
            y = int(input("Définis l'entier Maximum : "))
            break
        except:
            print("Tu dois choisir un nombre entier !!")
    
    # Génération aléatoire de l'entier compris dans la range [x, y]
    r = random.randint(x, y)
    print(r)


    while True :
        try:
            #Si l'input est égal au chiffre mystère, le jeux prend fin immédiatement 
            c = int(input("Tente ta chance : "))
            if c == r:
                print("Bien joué, tu as deviné le nombre mystère")
                break

            else:
                #Tant que l'input n'est pas égal au chiffre mystère :
                while c != r:
                        if c >r:
                            print("Essaie encore, trop grand")
                            c = int(input("Retente ta chance : "))
                        elif c <r:
                            print("Essaie encore, trop petit")
                            c = int(input("Retente ta chance : "))
                        if c == r :
                            print("Bien joué, tu as deviné le nombre mystère !")
                break

        except ValueError:
            print("Tu dois choisir un nombre entier !!")


    
    
number_guess()
