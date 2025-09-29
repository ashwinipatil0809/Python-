a=[10,20,30,-3,5,-9,0,-2,4,6,7,0,12,-5,9,-2]
c1=0
c2=0
c3=0
for i in range(len(a)):
    if a[i]>0:
        c1=c1+1
    elif a[i]<0:
        c2=c2+1
    else:
        c3=c3+1

print(a)
print("positive count:",c1)
print("nigative count:",c2)
print("zero count:",c3)
