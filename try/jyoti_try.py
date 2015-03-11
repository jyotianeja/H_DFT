import numpy as np
import math, random, cmath

import matplotlib.pyplot as pl



PI = np.pi

maxK = 2

l = 1+2*maxK
n_k = np.random.random(l*l*l)

#print n_k
#
print len(n_k)

def LegalKVecs(maxK,L=1.0):
    kList=[]
    # calculate a list of legal k vectors
    for kx in range(-maxK,maxK+1):
        for ky in range(-maxK,maxK+1):
            for kz in range(-maxK,maxK+1):
                kList.append([2*np.pi/L*kx,2*np.pi/L*ky,2*np.pi/L*kz])
            # end kz
        # end ky
    # end kx        
    return kList
# end def 

def Kmag(kList):
    magList = []
    for k in kList:
        magList.append( np.linalg.norm(k) )
    # end for k
    return magList
# end def kMag

def Hamiiltonian(KList,n_k,):
	mag = Kmag(KList)
	n = len(KList)
	H = np.zeros((n,n))
	for i in range (0,n):
		if mag[i] !=0:
			H[i][i] = -0.5*pow(mag[i],2) + 8*PI*PI/pow(mag[i],2) + 8*PI*PI*n_k[i]/pow(mag[i],2) 

	return H		





print ("The energy is ", np.linalg.eig(Hamiiltonian(LegalKVecs(maxK, L=1.0),n_k)))
