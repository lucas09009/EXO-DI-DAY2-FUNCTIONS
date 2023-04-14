def display_message():
    print("Salut tout le monde, ce cours me permet de savoir utiliser une fonction en python")
display_message()


def favorite_book(title):
    print("Un de mes livres préférées est:",title)
favorite_book("le roi Méroé")



def describe_city(ville="LOME", pays="TOGO"):
    print(ville,"est en",pays)
describe_city(pays="ISRAEL", ville="Tel-Aviv")


import random
def compare_Number(nombre):
    # input("Veuillez écrire un nombre compris entre 0 et 100")
    if(nombre > 0 and nombre < 101):
        num_aleatoire = random.randrange(1,101)
        if (nombre == num_aleatoire):
            print("Woah, Vous avez réussi")
        else:
            print("Désolé, vous avez perdu")
            print("Vous avez saisi",nombre,",la machine a renvoyée:",num_aleatoire)
    else:
        print("Saisie Invalide,Veuillez saisi un nombre compris entre 1 et 100")
compare_Number(-15)



def make_shirt(taille, texte):
    print("The size of the shirt is", taille,",and the text is",texte)
make_shirt("XL", "41cm")





magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magician_names):
    for item in magician_names:
        print(item)
    
show_magicians(magician_names)
        
        
def make_great(magician_names):
    for i, item in enumerate(magician_names):
        magician_names[i] = "The Great "+ item
    print(magician_names)
        
make_great(magician_names)