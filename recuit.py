import numpy as np
import random as rand
import math
# version2
def readMatrice(x):
    matrice = np.loadtxt(x, delimiter=";", dtype='i')
    return matrice


def calculCoutSolution():
    #vecteur solution
    gap = readMatrice("Bur26gGAP.txt")
    print(gap)
    #matrice des distances
    matrice1 = readMatrice("Bur26g1.txt")
    #matrice des flots
    matrice2 = readMatrice("Bur26g2.txt")
    total = 0
    #l'indice est l'emplacement et la valeur est l'objet
    for i in range(0, 26):
        Oi = gap[i]-1
        for j in range(0,26):
            Oj= gap[j]-1
            total += matrice2[Oi,Oj] * matrice1[i,j]
    return total

def calculCoutSolutionVecteur(gap, matrice1, matrice2):
    total = 0
    #l'indice est l'emplacement et la valeur est l'objet
    for i in range(0, 26):
        Oi = gap[i]-1
        for j in range(0,26):
            Oj= gap[j]-1
            total += matrice2[Oi,Oj] * matrice1[i,j]
    return total

def calculTempInitiale():
    #vecteur solution
    gap = readMatrice("Bur26gGAP.txt")
    #matrice des distances
    matrice1 = readMatrice("Bur26g1.txt")
    #matrice des flots
    matrice2 = readMatrice("Bur26g2.txt")
    cout1 = calculCoutSolutionVecteur(gap, matrice1, matrice2)
    somDelta = 0
    for i in range(100):
        calculCoutSolutionVecteur(gap, matrice1, matrice2)
        u = rand.randint(0,25)
        v= rand.randint(0,25)
        aux = gap[u]
        gap[u]=gap[v]
        gap[v]= aux
        cout2 =  calculCoutSolutionVecteur(gap, matrice1, matrice2)
        somDelta = somDelta + abs(cout2-cout1)
        cout1 = cout2
    moyDelta = somDelta/100
    T0 = round (-moyDelta/math.log(0.5))
    print(T0)
    return T0

def simulatedAnnealing():
    #vecteur solution
    gap = readMatrice("Bur26gSolInit.txt")
    #matrice des distances
    matrice1 = readMatrice("Bur26g1.txt")
    #matrice des flots
    matrice2 = readMatrice("Bur26g2.txt")
    T = calculTempInitiale()
    cout1 = calculCoutSolutionVecteur(gap, matrice1, matrice2)
    bestCost = cout1
    print (bestCost)
    for cycle in range (1000):
        for perturbation in range (10000):
            u = rand.randint(0,25)
            v= rand.randint(0,25)
            aux = gap[u]
            gap[u]=gap[v]
            gap[v]= aux
            cout2 =  calculCoutSolutionVecteur(gap, matrice1, matrice2)
            delta = cout2-cout1
            if(delta > 0):
                if (rand.random() < math.exp(-delta/T)):
                    cout1 = cout2
                else:
                    #on annule la permutation
                    aux = gap[u]
                    gap[u]=gap[v]
                    gap[v]= aux
            else:
                 cout1 = cout2
                 if (cout1 < bestCost):
                     bestCost = cout1
                     print (bestCost)
        T= T*0.9
                 
                   
    print(gap)
    return bestCost       
            



#cout = calculCoutSolution()
#print(cout)

#calculTempInitiale()
simulatedAnnealing()