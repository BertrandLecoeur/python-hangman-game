from random import randint
#import corrige_pendu

#Question 0
#Compléter dans les chaînes ci-dessous, sans enlever les guillemets:
NOM = "LECOEUR"
PRENOM = "BERTRAND"
EMAIL = "bertrand.lecoeur@universite-paris-saclay.fr"


#Question 1
def charge_mots(chemin):
    t=open(chemin,"r")  
    t=t.read()
    t=t.split()
    lmax=0
    for i in range(len(t)):
        if (len(t[i])>lmax):
            lmax=len(t[i])
    return(t,lmax)
    #return corrige_pendu.charge_mots(chemin)

 
   
   
    

#Question 2
def test_charge_mots():
    tableau,mot_le_plus_long=charge_mots("mots.txt")
    assert(mot_le_plus_long==25)
    assert(len(tableau)==59705)
    assert (tableau[54+1]=="abdomen")
    assert (tableau[456+1]=="accedez")
    
    return


#Question 3
def mots_par_longueur(tab_mots, lmax):
    nvt=[]
    for i in range(lmax+1):
        nvt.append([])
    for mot in tab_mots:
        nvt[len(mot)].append(mot)
    return nvt
    
    #return corrige_pendu.mots_par_longueur(tab_mots, lmax)

#Question 4
def test_mots_par_longueur():
    assert (mots_par_longueur(["a", "bonbon", "code", "dos", "etre"],6)==[ [], ["a"], [], ["dos"], ["code", "etre"], [], ["bonbon"] ])
    assert (mots_par_longueur(["cas","autre","voiture"],7)==[[],[],[],["cas"],[],["autre"],[],["voiture"]])
    return
#print(test_mots_par_longueur())

#Question 5
def choix_mot(tab_mots_long, l):
    if (not tab_mots_long[l]): 
        return ''
    n=randint(0,len(tab_mots_long[l])-1)
    return tab_mots_long[l][n]
    #return corrige_pendu.choix_mot(tab_mots_long, l)
#print(choix_mot([ [], ["a"], [], ["dos"], ["code", "etre"], [], ["bonbon"] ],4))

#Question 6
def test_choix_mot():
    #tab_mots_long POUR VOS TESTS
    #NE PAS MODIFIER LES 2 LIGNES SUIVANTES
    tab_mots, lmax = corrige_pendu.charge_mots("mots.txt")
    tab_mots_long = corrige_pendu.mots_par_longueur(tab_mots, lmax)
    assert (choix_mot([ [], ["a"], [], ["dos"], ["code", "etre"], [], ["bonbon"] ],4)in ["code", "etre"])
    assert (choix_mot(tab_mots_long,25)=="anticonstitutionnellement")
    return


#Question 7
def init_probleme(mot):
    l=[]
    for i in range(len(mot)):
        l.append((mot[i],False))
    return l
    
    #return corrige_pendu.init_probleme(mot)

#Question 8
def test_init_probleme():
    assert(init_probleme("mange")==[("m", False), ("a", False), ("n", False), ("g", False), ("e",False)])
    assert(init_probleme("vendre")==[("v", False), ("e", False), ("n", False), ("d", False), ("r",False), ("e",False)])
    return

#Question 9
def num_inconnues (probleme):
    a=0
    for lettre ,inconnues in probleme:
        if (inconnues==False):
            a+=1
    return a
    #return corrige_pendu.num_inconnues(probleme)
#print(num_inconnues([ ("c", False), ("o", False), ("d", False), ("e", False) ]))

# Question 10
def test_num_inconnues ():
    assert((num_inconnues([ ("c", False), ("o", False), ("d", False), ("e", False) ]))==4)
    assert((num_inconnues([ ("d", False), ("o", False), ("r", False), ("t", True) ]))==3)
    assert((num_inconnues([ ("a", True), ("i", True), ("m", True), ("e", True) ]))==0)
    return
#test_num_inconnues()

# Question 11
def joue(probleme, lettre):
    a = []
    
    for lettre1, f in probleme:
        if (lettre1 == lettre):
            a.append((lettre1, True))
        else:
            a.append((lettre1, f))
    return a
    #return corrige_pendu.joue(probleme, lettre)

#print(joue([ ("c", False), ("o", False), ("d", False), ("e", False) ],"e"))


# Question 12
def test_joue():
    
    assert((joue([ ("c", False), ("o", False), ("d", False), ("e", False) ],"j"))==[ ("c", False), ("o", False), ("d", False), ("e", False) ])
    assert((joue([ ("d", False), ("d", False), ("r", False), ("t", False) ],"d"))==[ ("d", True), ("d", True), ("r", False), ("t", False) ])
    assert((joue([ ("a", False), ("i", False), ("m", False), ("e", False) ],"e"))==[ ("a", False), ("i", False), ("m", False), ("e", True) ])
    return
print(test_joue())
# Question 13
def affiche_probleme(tab):
    #REMPLACER LA LIGNE CI-DESSOUS PAR VOTRE CODE
    for lettre, inconnues in tab:
        if (inconnues==True):
            print (lettre,end="")
        else:
            print(".",end="")
    print()
    
    #corrige_pendu.affiche_probleme (tab)
    
#print(affiche_probleme([ ("c", True), ("o", False), ("d", True), ("e", False) ]))


PENDU = (
    '  ___ ',
    ' |   |',
    ' o   |',
    '/|\  |',
    '/ \  |',
    '     |')

# Question 14
def affiche_pendu(n):
    k=0
    for i in range (6):
        for c in PENDU[i]:
            if (c==" "):
                print (c,end="")
            elif (k<n):
                print (c,end="")
                k+=1
            else:
                print (" ",end="")
        print()
#print(affiche_pendu(15))

    #REMPLACER LA LIGNE CI-DESSOUS PAR VOTRE CODE
    #corrige_pendu.affiche_pendu (n)


# Question 15 #donné par Jeremy Labiche L1 MI3
def partie(mot):
    alphabet=[i for i in 'abcdefghijklmnopqrstuvwxyz'] 
    probleme=init_probleme(mot)
    nbr_essai=0
    while ((num_inconnues(probleme)!=0)and(nbr_essai!=15)):
        affiche_probleme(probleme)
        lettre=input("Veuillez saisir une lettre: ")
        while (not (lettre in alphabet)):
            print("Lettre invalide ")
            affiche_probleme(probleme)
            lettre=input("Veuillez saisir une lettre: ")
        num_inconnues_avant=num_inconnues(probleme)
        probleme=joue(probleme,lettre)
        if(num_inconnues(probleme)==num_inconnues_avant):
            nbr_essai+=1
            affiche_pendu(nbr_essai)
    
    print("le mot à deviner était "+mot)
    if ((num_inconnues(probleme)==0)):
        print("Vous avez deviné le mot en faisant "+str(nbr_essai)+" erreurs")
        
    else:
        print("Vous n'avez pas réussit à devier le mot")
        
    
            
            
            
            
        
    
    #corrige_pendu.partie(mot)

#### NE PAS MODIFIER LE CODE CI-DESSOUS

def jeu():
    mots, lmax = charge_mots("mots.txt")
    lmots = mots_par_longueur(mots, lmax)
    while True:
        s = input("Saisir une longueur de mot ou q pour quitter: ")
        if s == 'q':
            print ("Au revoir.")
            return
        try:
            l = int(s)
            if l > lmax or l <= 0:
                print ("Longueur invalide")
                continue
            mot = choix_mot(lmots, l)
            partie (mot)
        except ValueError:
            print ("Saisie invalide")



jeu()
