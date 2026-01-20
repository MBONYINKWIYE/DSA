t = int(input())
for _ in range(t):
    bananas = list(map(int, input().split()))
    
    for i in range(5):
        bananas.sort()
        bananas[0] += 1            
    print(bananas[0]*bananas[1]*bananas[2])