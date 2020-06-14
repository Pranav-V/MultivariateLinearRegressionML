import numpy as np

def gradientd():
    param[0][0]=float(param[0][0])-((lrate)*(1/m)*(diff.sum()))
    column=np.zeros(10).reshape(10,1)
    arr = x.tolist()
    for i in range(m):
        i=i+1
        for n in range(m):
            column[n][0]=float(arr[i-1][n])
        param[i][0]=float(param[i][0])-((lrate)*(1/m)*(diff.getT()*column))

def formatprint():
    stuff = ""
    arr = param.tolist()
    for i in range(m+1):
        print('Theta'+str(i)+': '+ str(arr[i][0]))
    print('Cost:', cost)


m=3

x = np.matrix('-25.836 -48.53978 11 1; -25.835727	-48.539798 9 1; -15.819654 -47.946023	1098 1; -15.81876 -47.945077 1097.3 1; 14.347203 100.569012	6.8 1; 14.349005 100.569951 8.5 1; 0.197225	32.523705 1201.5 1; 0.197225 32.525502 1191 1 ; 0.218938	32.529995 1154.6 1; 0.206272	32.539881 1167.3 1')
y=np.matrix('0;0;0;0;0;0;1;1;1;1')
param=np.zeros(4).reshape(4,1)
lrate = .000005
for i in range(10000):
    calcy = x*param
    diff = calcy-y
    cost = (1/(2*m))*(float(diff.getT()*diff))
    gradientd()
    formatprint()
    print()
