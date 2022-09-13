import numpy as np


def readMatrice(x):
    matrice = np.loadtxt(x, delimiter=";", dtype='i')
    return matrice


def calculGap():
    gap = readMatrice("Bur26gGAP.txt")
    matrice1 = readMatrice("Bur26g1.txt")
    matrice2 = readMatrice("Bur26g2.txt")
    total = 0
    for i in range(0, 26):
        g = gap[i]
        #total += matrice1[i,g-1] * matrice2[i,g-1]
        total += matrice1[g-1,i] * matrice2[g-1,i]
    return total



def calculCout():
    matrice1 = readMatrice("Bur26g1.txt")
    matrice2 = readMatrice("Bur26g2.txt")
    total = 0
    
    for i in range(26):
        #print(gp)
        for j in range(26):
            total += matrice1[i, j] * matrice2[i, j]
    return total


cout = calculCout()
print(cout)

gap = calculGap()
print(gap)
