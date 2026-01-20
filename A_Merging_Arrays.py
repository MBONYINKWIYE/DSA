n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
result = []
i = 0
j = 0
while i < n and j <m:
    if arr1[i] <= arr2[j]:
        result.append(arr1[i])
        i += 1
    elif arr1[i] >= arr2[j]:
        result.append(arr2[j])
        j += 1
# We need to check the element out of bounds for every array because we don't
#know which will be out of bounds
while i < n:
    result.append(arr1[i])
    i += 1
while j < m:
    result.append(arr2[j])
    j += 1
# Until all elements finished in arrays
print(" ".join(map(str, result)))