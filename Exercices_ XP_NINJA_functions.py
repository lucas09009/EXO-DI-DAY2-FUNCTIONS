#EXO 1
#Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
#For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as

def box_printer(*elts):
    print("*********************")
    for elt in elts:
        print(elt,end="\n")
    print("*********************")

box_printer("Hello", "World", "in", "reallylongword", "a", "frame")



#EXO 2
#Analyse this code before executing it. What is the purpose of this code?

#CE CODE CLASSE LES ELEMENTS D'UNE LISTE DU PLUS PETIT AU PLUS GRAND
#...........................................................DETAILS.....................................................................
#insertion_sort est une fonction qui prend en argument une liste:
#pour les éléments de la liste dont l'index dont les éléments se situent entre 1 et la longueur de la liste, on assigne leur valeur 
#une à une à la variable current et leus index à la variable current.

#tant que l'index d'un élément est strictement supérieur à 0 et l'index de cet élément - 1 est supérieur à la valeur courante, alors 
#l'élément se trouvant à la position "position" est échangée avec l'élément à la position "position-1", de même que l'index de l'élément.


def insertion_sort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)