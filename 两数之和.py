"""给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。
"""

class Solution:
    def twoSum(self, nums, target: int):
        List=[]
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):

                if nums[i]+nums[j]==target and i!=j:
                    print(i)
                    print(j)
                    if i not in List and j not in List:
                        List.append(i)
                        List.append(j)
        print(List)
        return(List)
if __name__ == '__main__':
    Solution().twoSum([2,7,11,15],9)