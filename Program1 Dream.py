# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def capteur1 ():
    bunch = []
    for i in range (0,100):
        print (i)
        import random
        x10=random.randint(0,50)
        x20=random.randint(0,50)+x10
        x1=random.uniform(x10,x20)
        bunch.append(x1)
    print (bunch)
    return (bunch)
    
def capteur2 ():
    import random 
    x10=random.random()
    print (x10)
    x20=round (x10)
    print (x20)
    return (x20)
    
def capteur3 ():
    import random
    d01 = "une grenouille vit un oeuf, qui lui sembla de belle taille. elle, qui n etait pas grosse en tout comme un oeuf, envieuse, s'etend, et s'enfle, et se travaille, pour egaler l'animal en grosseur, disant, regardez bien, ma sœur, est-ce assez ? dites-moi ; n'y suis-je point encore. nenni. m y voici donc. point du tout. m y voila? vous n en approchez point. la chetive pecore s'enfla si bien qu'elle creva. le monde est plein de gens qui ne sont pas plus sages : tout bourgeois veut batir comme les grands seigneurs, tout petit prince a des ambassadeurs, tout marquis veut avoir des pages."
    x100=len(d01)
    x10=random.randint(0,x100)
    x20=random.randint(x10,x100)
    d=d01[x10:x20]
    print (d)
    return (d)
    
def system ():
    import datetime
    date = str(datetime.datetime.now())
    date2 = date[:13]+date[14:16]+date[17:]
    d1=capteur1()
    d2=capteur2()
    d3=capteur3()
    table = open("C:\Temp\date" + date2 +".txt","a")
    table.write("System"+'\n'+date+'\n'+'\n'+"Capteur1"+'\n'+str(d1)+'\n'+'\n'+"Capteur2"+'\n'+str(d2)+'\n'+'\n'+"Capteur3"+'\n'+str(d3)+'\n')
    table.close()
    return