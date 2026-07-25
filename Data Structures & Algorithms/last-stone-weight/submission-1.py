class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # First, make a heap from stones array
        # Space complexity = O(1), time complexity O(n)
        if len(stones) == 1:
            return stones[0]

        heapq.heapify_max(stones)
        newStoneWeight = 0

        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            if x == y:
                newStoneWeight = 0
            elif y < x:
                newStoneWeight = x - y
                heapq.heappush_max(stones, newStoneWeight)

        return stones[0] if len(stones) == 1 else 0