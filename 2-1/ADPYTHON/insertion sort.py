n=int(input("enter ele:"))
l=[]
for i in range(0,n):
    ele=int(input("enter the element:"))
    l.append(ele)
print("list before sorting:",l)
for i in range(1,len(l)):
    j=i-1
    next_ele=l[i]
    while(l[j]>next_ele)and j>=0:
        l[j+1]=l[j]
        j=j-1
        l[j+1]=next_ele
print("list after sorting:" ,l)        
