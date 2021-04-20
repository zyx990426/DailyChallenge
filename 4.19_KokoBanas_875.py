class Solution(object):
    def minEatingSpeed(self, piles, H):
        # Can Koko eat all bananas in H hours with eating speed K?
        start = 1
        end = 1000000000
        
        while start + 1 < end:
            mid = (start + end) // 2
            if self.SpeedCheck(piles, mid, H):
                end = mid
            else:
                start = mid
                
        if self.SpeedCheck(piles, start, H):
            return start
        return end
                
        
        
    def SpeedCheck(self, piles, speed, H):
        time = 0
        for p in piles:
            time += math.ceil(p / speed)
        if time > H:
            return False
        return True