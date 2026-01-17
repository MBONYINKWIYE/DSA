class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        myCounts = 0
        n = len(piles)
        maximum = max(piles)+1
        freq = [0]*maximum
        for i in range(n):
            freq[piles[i]] += 1
        
        j = 0
        for y in range(len(freq)):
            for _ in range(freq[y]):
                piles[j] = y
                j +=1

        print(piles)
        for i in range(len(piles )// 3, len(piles), 2):
           myCounts += piles[i]
        return myCounts