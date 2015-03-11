import numpy as np

def LegalKVecs(maxK,L=1.0):
    kList=[]
    # calculate a list of legal k vectors
    for kx in range(maxK):
        for ky in range(maxK):
            for kz in range(maxK):
                kList.append([2*np.pi/L*kx,2*np.pi/L*ky,2*np.pi/L*kz])
            # end kz
        # end ky
    # end kx        
    return kList
# end def 


def kMag(kList):
    magList = []
    for k in kList:
        magList.append( np.array(k).norm() )
    # end for k
    return magList
# end def kMag
