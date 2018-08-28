# change the size
# recovery the size 
import numpy as np
from parm import Para as P
def t2b(X,P):
    patsize = P.patsize
    step = P.step
    sz = np.shape(X)
    print(sz)
    TotalpatNum =int((np.floor((sz[0]-patsize)/step)+1)*(np.floor((sz[1]-patsize)/step)+1)*(np.floor((sz[2]-patsize)/step)+1))
    Z = np.zeros([patsize,patsize,patsize,TotalpatNum])
    for i in range(patsize):
        for j in range(patsize):
            for k in range(patsize):
                tempPatch = X[i:sz[0]-patsize+i+1,j:sz[1]-patsize+j+1,k:sz[2]-patsize+k+1][::step,::step,::step]
                Z[i,j,k,:] =np.reshape(tempPatch,[1,TotalpatNum],order = 'F')

    Y = np.transpose(np.reshape(Z,[patsize*patsize,patsize,TotalpatNum],order = 'F'),[0,2,1])
    return Y

   
def b2t(lu,P,size_X):
    patsize = P.patsize
    step = P.step
    TempR = int(np.floor((size_X[0]-patsize)/step))+1
    TempC = int(np.floor((size_X[1]-patsize)/step))+1
    TempS = int(np.floor((size_X[2]-patsize)/step))+1
    TempOffsetR = np.arange(0,(TempR-1)*step+1,step)
    TempOffsetC = np.arange(0,(TempC-1)*step+1,step)
    TempOffsetS = np.arange(0,(TempS-1)*step+1,step)
    xx = np.size(TempOffsetR)
    yy = np.size(TempOffsetC)
    zz = np.size(TempOffsetS)
    print(xx)
    print(yy)
    print(zz)
    E_V = np.zeros(size_X)
    Weight = np.zeros(size_X)
    N = lu.shape[1]
    ZPat = np.reshape(np.transpose(lu,[0,2,1]),[patsize,patsize,patsize,N],order = 'F')
    for i in range(patsize):
        for j in range(patsize):
            for k in range(patsize):
                E_V[TempOffsetR-1+i,TempOffsetC-1+j,TempOffsetS-1+k] = E_V[TempOffsetR-1+i,TempOffsetC-1+j,TempOffsetS-1+k]+np.reshape(ZPat[i,j,k,:],[xx,yy,zz],order = 'F') 
                Weight[TempOffsetR-1+i,TempOffsetC-1+j,TempOffsetS-1+k] = Weight[TempOffsetR-1+i,TempOffsetC-1+j,TempOffsetS-1+k]+np.ones([xx,yy,zz])

    E_V = E_V/(Weight+np.spacing(1))
    return E_V

if __name__ == '__main__':
    print('smys')
    han = np.random.rand(25,33614,5)
    size = [101,101,31]
    print(b2t(han,P,size).shape)
    print('nihao')
