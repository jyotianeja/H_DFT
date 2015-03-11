import numpy as np

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

<<<<<<< HEAD
def Kmag(kList):
    magList = []
    for k in kList:
        magList.append( np.linalg.norm(k) )
    # end for k
    return magList
# end def kMag

if __name__=="__main__":
    print LegalKVecs(1)
    print Kmag(LegalKVecs(1))
# end __main__
=======

def kMag(kList):
    magList = []
    for k in kList:
        magList.append( np.array(k).norm() )
    # end for k
    return magList
# end def kMag
>>>>>>> 5ccfde210cb6c57689bf438afe48b4009d6b4e96
