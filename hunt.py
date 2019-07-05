n=int(input())
k=list(map(int,input().split()))
k.sort()
b=[]
for i in range (len(k)-1):
  if k[i]==k[i+1]:
    b.append(k[i])
if b:
    for x in set(b):
        print(x,end=" ")
else:
    print("unique")
