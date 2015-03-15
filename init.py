import numpy as np
import matplotlib.pyplot as plt

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

def guessDensity(KList):
    n = np.zeros(len(KList))
    mag = Kmag(KList)
    for i in range(len(n)):
        n[i] = 50./( (4+mag[i]*mag[i])**2 )
    # end for i
    return n[:]
# end def guessDensity

def densityNorm(n,kList,L):
    norm = 0.0
    mag = Kmag(kList)
    for i in range(len(kList)):
        k = kList[i]
        if (k[0]>0):
            norm += 2*n[i]*(-2*np.pi*L/(mag[i]*mag[i]))*(-1)**(2*L/np.pi*(k[0]+k[1]+k[2]))
        # end if
    # end for i
    return norm
# end def densityNorm

def normalizeDensity(n,kList,L,N=1):
    # normalize density n to have the number of electrons N
    norm = densityNorm(n,kList,L)
    for i in range(len(n)):
        n[i] *= N/norm
    # end for
# end def normalizeDensity

def newDensity(w,v,kList,N=1):
    min = w[0]
    minidx = 0
    for i in range(len(w)):
        if w[i] < min:
            minidx = i
        # end if
    # end for i
    psi = v[minidx][:]
    # construct \psi^*
    psistar = psi[:]
    for i in range(len(psistar)):
        k = kList[i]
        if k[0]>0:
            for j in range(len(kList)): # find -\vec{k}
                negk = kList[j]
                if (negk[0]==-k[0] and negk[1]==-k[1] and negk[2]==-k[2]):
                    psistar[i],psistar[j] = psistar[j],psistar[i]
                # end if
            # end for j
        # end if
    # end for i
    newn = np.array(psi)+np.array(psistar)
    return newn
# end def newDensity

def plotDensity(n,kList):
    mag = Kmag(kList)
    plt.figure()
    plt.plot(mag,n)
    plt.show()
# end def

def mixDensity(newn,oldn,beta=0.1):
    myn = np.zeros(len(oldn))
    for i in range(len(oldn)):
        myn[i] = beta*newn[i] + (1-beta)*oldn[i]
    # end for i
    return myn[:]
# end def mixDensity


def Vxc():
    pass
# end def Vxc

if __name__=="__main__":
    #print LegalKVecs(1)
    #print Kmag(LegalKVecs(1))
    psi = [[1,0,0],[0,0,1]]
    epsilon = [1,2]
    newn = newDensity(psi,epsilon)
    oldn = [0,.5,0]
    normalizeDensity(oldn)
    print oldn
# end __main__
