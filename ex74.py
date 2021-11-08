t=[0]*30
t[0]=0
t[1]=1
for i in range(2,30):
    t[i]=t[i+1]+t[i+2]
print(t)