l=[]
n=int(input("Enter List size:"))
for i in range(n):
    l.append(int(input()))
l.sort()
s=int(input("Enter the element to be inserted"))
i=0
while i<len(l):
    if s<l[i]:
        break
    i=i+1
l.insert(i,s)
print(l)
