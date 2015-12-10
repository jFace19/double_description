import numpy as np
import tolerant_rank_kern as tlr

def double_description(matrix, m, d):
    W=matrix[:int(d),:].copy()
    W=W.getI()
    for j in range (d,m):
        plusList=[]
        minusList=[]
        equalList=[]
        print("Dimensio W:  ", W.shape)
        for i in range(W.shape[0]):
            #wirklich w[i] Zeilen?
            print("Product:  ", (W[i,:]) * (matrix[j,:]).T)
            if np.isclose((W[i,:]) * (matrix[j,:]).T,0):
                equalList.append(W[i,:])
            elif (W[i,:]) * (matrix[j,:]).T < 0:
                minusList.append(W[i,:])
            elif (W[i,:]) * (matrix[j,:]).T > 0:
                plusList.append(W[i,:])
        if len(minusList)==0:
            print("Laenge  Liste <> < 0:  0")
        else:
            X=[]
            for el in plusList:
                for nel in minusList:
                    HL=[]
                    for l in range(j-1):
                        tmp=nel  * (matrix[l,:]).T
                        if np.isclose(el * (matrix[l,:]).T,tmp, 0, 1e-12) and np.isclose(0,tmp, 0, 1e-12):
                            HL.append(matrix[l,:])
                    H=np.matrix(HL)
                    print("Matrix H: ", H)
                    if tlr.rank(H) == d-2:
                        array=tlr.nullspace(H)
                        x=array[:,0].T
                        if x[0] != 0:
                            x=x/x[0]
    
                        X.append(x)
                print("pluslist: ", plusList, '\n', "minus:  ", minusList,'\n' "equal:  ", equalList)
                tempW = plusList + equalList + X
                arrayW = np.asarray(tempW)
                print("arrayW:  ", arrayW)
                print("Partitionen hintereinander in Liste: ", tempW)
                W=np.matrix(arrayW)
                print("W nach Schleife:  ", W)
    m=W.shape[0]
    return (W,m)
    pass