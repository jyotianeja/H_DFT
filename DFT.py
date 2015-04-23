#!/usr/bin/env python

import random
import numpy as np

N = 1
maxK = 2
basisSep=2.13
maxNsteps = 500
thres = 1e-5
mixing = 0.5

def normalize(wavevec):
    # assume each planewave basis function is normalize
    # normalize wf such that density integrates to 1
    norm = np.linalg.norm(wavevec)
    for i in range(len(wavevec)):
        wavevec[i] /= norm
    # end for i
# end def normalize

# basis for wavevec
kList=[[basisSep*kx,basisSep*ky,basisSep*kz] for kx in range(-maxK,maxK+1) for ky in range(-maxK,maxK+1) for kz in range(-maxK,maxK+1) if not (kx==ky==kz==0)]
kMag = [np.linalg.norm(k) for k in kList]
kSize=len(kList)

def psi2density(wavevec):
    density=np.zeros(kSize)
    for i in range(len(wavevec)):
        ci=wavevec[i]
        ki = kList[i]
        for j in range(len(wavevec)):
            cj=wavevec[j]
            kj=kList[j]
            
            idx = 0
            kdiff = list( np.array(ki)-np.array(kj) )
            for k in range(len(kList)):
                if kdiff==kList[k]:
                    idx = k
                # end if kdiff
            # end for k
            density[idx] += ci*cj 
        # end for j
    # end for i
    return density
# end def psi2density

def plotPsi(psi):
    x = []
    y = np.ones( 9 )
    for i in range( len(kMag) ):
        kmag = kMag[i]
        if kmag not in x:
            x.append(kmag)
        # end if 
        y[x.index(kmag)] += psi[i]
    # end for i
    plt.plot(x,y,'-x')
    plt.show()
# end def plotPsi

def HamVec(n_k):
    # return Hamiltonian on planewave basis grid
    return [
        0.5*pow(kMag[i],2)                      # kinetic
        - 4*np.pi/pow(kMag[i],2)                # external
        + 8*np.pi*np.pi*n_k[i]/pow(kMag[i],2)   # Hatree
    for i in range(0,kSize)]
# end def HamVec


import matplotlib.pyplot as plt
if __name__ == "__main__":

    # make an initial guess
    psi = np.random.random(pow(1+2*maxK,3) -1)
    normalize(psi)
    # self-consistently solve the KS equations
    energy=0
    converged = False
    
    for step in range(maxNsteps):
        print energy
        H=HamVec(psi2density(psi))
        newPsi=np.zeros(kSize)
        newPsi[H.index(min(H))]=1
        psi =psi*(1-mixing)+newPsi*mixing
        normalize(psi)
        #newEnergy=np.dot(H,psi*psi) # shouldn't it be this? -> newEnergy=min(H)
        newEnergy=min(H)
        if abs(energy-newEnergy)<thres:
            converged = True
            break
        # end if thres
        energy = newEnergy
    # end for step
    
    if converged:
        print "converged in ", step, " steps, energy=", energy
    else:
        print "Did not converge in ",step, " steps, energy=",energy
    # end if converged
   
# end __main__
