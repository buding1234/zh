"""在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，
但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
"""

#哈希表 / Set
class Solution:
    def test01(self, nums):
        dic=set()
        for i in nums:
            if i in dic:return i
            dic.add(i)


#原地交换 会数组越界错误的写法
    def test02(self, nums):
        i =0
        while i < len(nums):
            # print(nums[nums[i]])
            if nums[i]!=i:
                if nums[nums[i]]==nums[i]: #会数组越界
                    return nums[i]

                nums[nums[i]],nums[i]=nums[i],nums[nums[i]]
            else:
                i+=1
        return -1
if __name__ == '__main__':
    nums=[1, 2, 6, 3, 5]
    print(Solution().test03(nums))