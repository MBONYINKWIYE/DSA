n, m = map(int, input().split())
arr1 = list(map(int, input().split()))  
arr2 = list(map(int, input().split()))
i = 0
j = 0
count = 0
result = []
while j < m:
    if i < n and arr2[j] > arr1[i]:
        count += 1
        i += 1
    else:
        result.append(count)
        j += 1

print(" ".join(map(str, result)))
