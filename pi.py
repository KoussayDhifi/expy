import pickle

#Sous programme

def patient():
    p = {}
    p['numdos'] = input("numdossier: ")
    while not (p['numdos'].isnumeric() and len(p['numdos'])<=4):
        p['numdos'] = input("numdossier: ")
    p['nompat'] = input("nompat : ")
    while not (verif(p['nompat'])):
        p['nompat'] = input("nompat : ")
    p['naisspat'] = {}
    p['naisspat']['j'] = int(input(" j = "))
    p['naisspat']['m'] = int(input(" m = "))
    p['naisspat']['a'] = int(input(" a = "))
    p['telpat'] = input("telpat = ")
    while not (p['telpat'].isnumeric()) and(len(p['telpat']==8)):
        p['telpat'] = input("telpat = ")
    return p




def saisir():
    p = {}
    d = {}
    f = open("liste.dat","wb")
    ajouter = True
    while ajouter:
        p = patient()
        pickle.dump(p,f)
        rep = input("ajouter?: ")
        if (rep == "N"):
            ajouter = False
    f.close()


def ranger ():
    f = open("liste.dat","rb")
    ajouter = True
    T = []
    n = 0
    while ajouter:
        try:
            o = pickle.load(f)
            T.append(o)
            n+=1
        except:
            ajouter = False

    f.close()
    return T,n    
    
def insere(T,n):
    f = open("liste.dat","wb")
    p = int(input("position: "))
    T2 = []
    p1 = patient()
    for i in range(n+1):
        if (i<p):
            T2.append(T[i])
        if (i>p):
            T2.append(T[i-1])
        elif (i==p):
            T2.append(p1)
    print('avant insere: ')
    for i in range(n):
        print(f"{T[i]['numdos']} {T[i]['nompat']} {T[i]['naisspat']['j']}/{T[i]['naisspat']['m']}/{T[i]['naisspat']['a']} {T[i]['telpat']}")
    print('\n apres insere: ')
    for i in range(n+1):
        print(f"{T2[i]['numdos']} {T2[i]['nompat']} {T2[i]['naisspat']['j']}/{T2[i]['naisspat']['m']}/{T2[i]['naisspat']['a']} {T2[i]['telpat']}")
        pickle.dump(T2[i],f)    
    f.close()

def verif (ch):
    etat = True
    if (len(ch)>15):
        etat = False
    else:
        for i in range(len(ch)):
            if not("A"<=ch[i].upper()<="Z"):
                etat = False
    return etat

def supp ():
    f = open('liste.dat','rb')
    lire = True
    T3 = []
    n = 0
    p = int(input("position supp: "))
    while lire:
        try:
            
            o = pickle.load(f)
            if not(p == n):
                T3.append(o)
            n+=1
        except:
            lire=False
    f.close()
    f = open('liste.dat','wb')
    for i in range(n-1):
        pickle.dump(T3[i],f)
    
    f.close()
    
    f = open('liste.dat','rb')
    lire = True
    while lire:
        try:
            o = pickle.load(f)
            print(f"{o['numdos']} {o['nompat']} {o['naisspat']['j']}/{o['naisspat']['m']}/{o['naisspat']['a']} {o['telpat']}")
        except:
            lire = False

    f.close()


def existe():
    cd = input("Choix du dossier: ")
    f = open("liste.dat","rb")
    lire = True
    while lire:
    
        o = pickle.load(f)
        if (o['numdos'] == cd):
            print(f"<<Patient: {o['numdos']} {o['nompat']} {o['naisspat']['j']}/{o['naisspat']['m']}/{o['naisspat']['a']} {o['telpat']}")

        lire = False


#PP
saisir()
T,n = ranger()
insere(T,n)
supp()
existe()  
        




