# a=[56,46,89,54,70,32,76]
    # getting input from user
a=[]
n=int(input("no of elements in list"))
for i in range(n):
    a.append(int(input()))
    # logic for insertion
for j in range(1,len(a)):
    value=a[j]
    i=j-1
    while(i>=0 and a[i]>value):
        a[i+1]=a[i]
        i=i-1
    a[i+1]=value
print(a)   
