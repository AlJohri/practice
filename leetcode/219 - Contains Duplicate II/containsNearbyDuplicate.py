class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        hash = {}
        for i, number in enumerate(nums):
            if number in hash:
                j = hash[number]
                if (i - j) <= k:
                    return True
                else:
                    hash[number] = i
            else:
                hash[number] = i
        return False
