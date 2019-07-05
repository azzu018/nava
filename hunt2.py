N=int(input())
m=list(map(int, input().split()))[:N]
m.sort(reverse=True)
print(''.join(str(num) for num in m))
