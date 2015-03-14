import numpy as np

def LegalKVecs(maxK,L=1.0):
    kList=[]
    # calculate a list of legal k vectors
    for kx in range(-maxK,maxK+1):
        for ky in range(-maxK,maxK+1):
            for kz in range(-maxK,maxK+1):
                #kList.append([2*np.pi/L*kx,2*np.pi/L*ky,2*np.pi/L*kz])
                kList.append([kx,ky,kz])
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

def normalizeDensity(n,N=1):
    # normalize density n to have the number of electrons N
    norm = np.linalg.norm(n)
    for i in range(len(n)):
        n[i] *= N/norm
    # end for
# end def normalizeDensity

def newDensity(w,v,N=1):
    min = w[0]
    minidx = 0
    for i in range(len(w)):
        if w[i] < min:
            minidx = i
        # end if
    # end for
    newn = np.array(v[minidx])*np.array(v[minidx])
    return newn
# end def newDensity

def mixDensity(newn,oldn,beta=0.1):
    return beta*np.array(newn)+np.array(oldn)
# end def mixDensity

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
