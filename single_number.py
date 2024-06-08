from collections import defaultdict

class Solution(object):
    
    def singleNumber(self, nums):
        # freq = defaultdict(int): create a defautdict called freq, where the
        # standart value for new any key will be 0 (because int() return 0).
        # 'key': value  
        freq = defaultdict(int)  
        for n in nums:
            freq[n] += 1

        res = []
        # num = key f = value
        for num, f in freq.items():
            if f == 1:
                res.append(num)

        return res
    
list = [1,2,1,3,2,5]
res = Solution()
func = res.singleNumber(list)   
print(func)

