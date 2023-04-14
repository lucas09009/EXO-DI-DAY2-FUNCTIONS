import random
def throw_dice():
    return  random.randrange(1,7)
    
throw_dice()   
    
def throw_until_doubles():
    global dé1, dé2, compte
    compte = 0
    
    dé1 = throw_dice()
    dé2 = throw_dice()
    
    while(dé1 != dé2):
        dé1 = throw_dice()
        dé2 = throw_dice()
        resultat = dé1, dé2
        print(resultat)
        compte += 1
    else:
        print("Le dé a été lancée",compte,"fois")
throw_until_doubles()


x = 0
def main():
    print("yes")
    print(throw_until_doubles())
    if(dé1 == dé2):
        # while(x < 2):
            print(throw_until_doubles())
             
x += 1
main()
print(x, dé1, dé2)      

