
n, k = list(map(int, input().split()))
L = list(map(int, input().split()))
k_th = L[k-1]
count = 0
for i in range(0, len(L)):
    if L[i] >= k_th and L[i] > 0:
        count += 1
print(count)
