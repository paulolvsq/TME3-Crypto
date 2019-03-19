# -*- coding: utf-8 -*-
import math
def pgcd(a, b):
    """pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"""
    if b==0:
        return a
    else:
        r=a%b
        return pgcd(b,r)
    

def pgcdE(a,b):
    r0 = a
    r1 = b
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1
    while r1>0:
        r = r0%r1
        q = (r0-r)/r1
        u = u0-q*u1
        v = v0-q*v1
        u0 = u1
        v0 = v1
        u1 = u
        v1 = v
        r0 = r1
        r1 = r
    print("\npgcd(", a, ",", b, ") =", r0, "\nValeur de u: ", u0, "\nValeur de v: ", v0);
    return u0, v0

print("Test pdcd Etendu")  
print(pgcdE(5005,1014))
        
def inverse_modulaire(a, n):
    if(pgcd(a, n) == 1):
        u0, v0 = pgcdE(a, n)
        if(a*u0 + n*v0 == 1):
            print("L'inverse modulaire de "+str(a)+" modulo n est : "+str(u0))
            return u0
    print("L'inverse modulaire de "+str(a)+" n'existe pas modulo n")
    return 
print("Test Inverse modulaire \n")  
inverse_modulaire(1014, 5005)
inverse_modulaire(59, 27)

def indicateur_euler(n):
    cpt=0
    L = []
    for i in range(n):
        if(pgcd(i, n) == 1):
            #print(i)
            cpt+=1
            L.append(i)
    print("Il y a "+str(cpt)+" nombres premier avec n entre 0 et n")
    return cpt, L 

print("\n")
print("Test indicateur_euler :")  
indicateur_euler(1000000)

def exponentiation_modulaire(a,e,m):
    if(e == 1):
        res=a%m
    else:
        res = 1
        
    for i in range(m-1,0,-1):
        res=res*(res%m)
        if e==1:
            res=(res*e)%m    
    return res

print("\n")
print("Test exponentiation modulaire :")
print(exponentiation_modulaire(3,5,13))

def nb_diviseurs(n):
    L = []
    for i in range(1,n+1):
        if(n%i == 0):
            L.append(i)
    return len(L)

def est_premier(n):
    if(nb_diviseurs(n) == 2):
        return True
    else:
        return False

def facteurs_premiers(n,liste):    
    if(est_premier(n)):
        liste.append(n)
        print("Liste finale : ",liste)
        return liste  
    else:
        print("n:",n)
        R = []
        for i in range(1, n+1):
            if est_premier(i):
                if(n%i==0):
                    R.append(i)
        
        print("r: ",R)
        print("r : ",R)
        taille=len(R)
        liste.append(R[taille-1])
        print("reste ; ",n//R[taille-1])
        return facteurs_premiers(n//R[taille-1],liste)

print("\n")
print("\n") 
facteurs_premiers(498,[])



def BSGS(n,alpha,beta):
    m = math.sqrt(n)
    liste=[]
    for j in range(m+1):
        alphabis=pow(alpha,j)
        liste.append((j,alphabis))
        
    gsinv=exponentiation_modulaire(alpha,-m,n)
    Y=beta
    for i in range(m):
        for i in liste:
            a,b=i
            if(Y==b):
                return i*m+a; #a= le j
            else:
                Y=Y*gsinv

    



                
        
            
        
    