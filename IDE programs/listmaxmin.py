a=[10,20,30,40,50]
max_value=a[0]
min_value=a[0]
for i in range(len(a)):
    if a[i]>max_value:
        max_value=a[i]
    elif a[i]<min_value:min_value=a[i]

print("maximum value=:",max_value)
print("minmum value=:",min_value)
