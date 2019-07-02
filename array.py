n,k=map(int,input().split())
sums=0
array=list(map(int,input().split()))

for i in range(0,k):
    sums=sums+array[i]
print(sums)
