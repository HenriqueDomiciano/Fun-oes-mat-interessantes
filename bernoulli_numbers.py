import numpy as np
prec = int(input("Digite a precisão"))
pascal = np.zeros((prec,prec),dtype=np.float64)
pascal[:,0]=1

for i in range(1,prec):
    for j in range(1,i+1):
        pascal[i][j] = pascal[i-1][j-1]+ pascal[i-1][j]
pascal = pascal[~np.eye(pascal.shape[0],dtype=bool)].reshape(pascal.shape[0],-1)
pascal = np.delete(pascal,0,0)
pascal = np.linalg.pinv(pascal)
bernoulli = pascal[:,0]
print([np.round(i,8) for i in bernoulli])