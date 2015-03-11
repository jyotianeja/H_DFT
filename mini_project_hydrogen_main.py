

import numpy, math, random, cmath
import matplotlib.pyplot as pl

from init import *


PI = np.pi
maxK = 5
maxNsteps = 400

thres = 1e-2
l = 1+2*maxK
oldn = np.random.random(l*l*l)
normalizeDensity(oldn)

def Hamiiltonian(KList,n_k,):
	mag = Kmag(KList)
	n = len(KList)
	H = np.zeros((n,n))
	for i in range (0,n):
		if mag[i] !=0:
			H[i][i] = -0.5*pow(mag[i],2) + 8*PI*PI/pow(mag[i],2) + 8*PI*PI*n_k[i]/pow(mag[i],2) 

	return H	
# end def Hamiltonian	


if __name__ == "__main__":
	converged = False
	for step in range(maxNsteps):
		w,v = np.linalg.eig(Hamiiltonian(LegalKVecs(maxK),oldn))
		newn = newDensity(w,v)
		newn = mixDensity(newn,oldn,0.2)
		normalizeDensity(newn)
		if np.linalg.norm(newn-oldn)<thres:
			converged = True
			break
		# end if
		oldn = newn
	# end for 
	print "converged in ", step, " steps, energy=", w.min()
	#print oldn 
# end __main__


