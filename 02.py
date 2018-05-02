from PIL import Image
import numpy as np
import scipy.misc

key1 = Image.open('key1.png')
key2 = Image.open('key2.png')
eprime = Image.open('Eprime.png')
I = Image.open('I.png')

a = np.asarray(key1).copy()
b = np.asarray(key2).copy()
c = np.asarray(eprime).copy()
d = np.asarray(I).copy()


data = np.zeros((120000,3),int)

e = np.zeros((120000,1),int)

for y in range(300):
    for x in range(400):
      data[y*400+x][0] = a[y][x]
      data[y*400+x][1]= b[y][x]
      data[y*400+x][2] = d[y][x]
      e[y*400+x] = c[y][x]

       
w = np.array([0,0,0]) 

maxlimit = 10
temp_w0 = 10
temp_w1 = 10
temp_w2 = 10

epoch = 1
while epoch < maxlimit and abs(w[0] - temp_w0) > 0.00001 and abs(w[1] - temp_w1) > 0.00001 and abs(w[2] - temp_w2) > 0.00001:
    temp_w0 = w[0]
    temp_w1 = w[1]
    temp_w2 = w[2] 
    for i, x in enumerate(data): 
        t = w[0]*x[0]+w[1]*x[1]+w[2]*x[2]
        p = e[i] - t
        w = w +  0.00001*p*x
    epoch += 1 

print(w[0],w[1],w[2])

img = np.zeros((300,400),int)
      
for j in range(300):
    for i in range(400):
        img[j][i] = (c[j][i]-w[0]*a[j][i]-w[1]*b[j][i])/w[2]
        
scipy.misc.imsave('output.jpg', img)

