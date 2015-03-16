from init import *

PI = np.pi
maxK = 3
L=5.0
maxNsteps = 100

thres = 1e-5
l = 1+2*maxK

def Hamiiltonian(KList,n_k):
	mag = Kmag(KList)
	n = len(KList)
	H = np.zeros((n,n))
	for i in range (0,n):
		if mag[i] !=0:
			H[i][i] = -0.5*pow(mag[i],2) - 8*PI*PI/pow(mag[i],2) + 8*PI*PI*n_k[i]/pow(mag[i],2)
		# end if
    # end for
	return H	
# end def Hamiltonian

if __name__ == "__main__":

    KList = LegalKVecs(maxK,L)
    oldn = guessDensity(KList)
    normalizeDensity(oldn,KList,L)
    
    plotDensity(oldn,KList)
    
    converged = False
    for step in range(maxNsteps):
        w,v = np.linalg.eig(Hamiiltonian(KList,oldn))
        newn = newDensity(w,v,KList)
        newn = mixDensity(newn,oldn,.1)
        normalizeDensity(newn,KList,L)
        
        if np.linalg.norm(newn-oldn)<thres:
            converged = True
            break
        # end if
        if not (step%10):
            print np.linalg.norm(newn-oldn)
        # end if
          
        oldn = newn  
    # end for 
	
    if converged:
        print "converged in ", step, " steps, energy=", min(w)
    else:
        print "Did not converge in ",step, " steps, energy=", min(w)
    # end if
    
    plotDensity(newn,KList)
    
# end __main__


