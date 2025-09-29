a=[12,3,4,56,6,9,34,56,7,1,77,8,21,78,3,9,87]
ec=0
oc=0
for i in range(len(a)):
    if a[i]%2==0:
        ec=ec+1
    else:
        oc=oc+1

print("even number count:",ec)
print("odd number count:",oc)
