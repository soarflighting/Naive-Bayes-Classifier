
# 给定一个整数数组 nums 和一个目标值 target，
# 请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。
# 但是，你不能重复利用这个数组中同样的元素。

# 本题的关键是找到num2 = target - num1
class Solution(object):
    def twoSum_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = -1
        for i in range(len(nums)):
            #判断target-nums[i] 是否出现在nums中
            if (target - nums[i]) in nums:
                #若target-nums[i]==nums[i] 并且target-nums[i]只出新了一次，说明找到的是nums[i]本身
                if (target - nums[i]) == nums[i] and nums.count(target - nums[i]) == 1:
                    continue
                else:
                    #从num[i]后的序列进行查找target-nums[i]
                    j = nums.index(target - nums[i],i+1)
                    break
        if j>0:
            return [i,j]
        else:
            return "无解"
    #解法二
    #在上一种算法的基础上进行优化算法，num2的查找每次并不需要从nums列表中进行查找一遍
    #只需查找从num1位置之前或之后查找即可,为了方便index，这里选择num1之前查找
    def twoSum_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        j = -1
        lens = len(nums)
        for i in range(1,lens):
            temp = nums[:i]
            if (target - nums[i]) in temp:
                j = temp.index(target - nums[i])
                break
        if j>=0:
            return [j,i]
        else:
            return "无解"
    #解法三
    #通过哈希来求解，通过字典来模拟哈希查询的过程

    def twoSum_3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        j = -1
        hashmap = {}
        for ind,num  in enumerate(nums):
            hashmap[num] = ind
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]
        if j<0:
            return "无解"

    #解法四：在算法二和算法三的基础上进行改进
    #不需要在num2,不需要在在整个字典中去查找
    #可以在num1之前的字典中去查找
    def twoSum_4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i,num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                #return [i,hashmap[target-num]]
                return [i,hashmap.get(target - num)]

            hashmap[num] = i

    #算法五：
    # 先排序（伪排序，不打乱nums中索引的位置）
    #利用二分方法找到和target相等的两个数
    #利用nums.index()来找到两数的索引位置
    def twoSum_5(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lens = len(nums)
        left = 0
        right = lens - 1
        sort_nums = sorted(nums)
        sum = sort_nums[left] + sort_nums[right]
        while left < right:
            if sum == target:
                if sort_nums[left] == sort_nums[right]:
                    array = []
                    for (index,value) in enumerate(nums):
                        if value == sort_nums[left]:
                            array.append(index)
                            if len(array) == 2:
                                break
                    return array
                else:
                    return [nums.index(sort_nums[left]),nums.index(sort_nums[right])]
            elif sum < target:
                left += 1
            else:
                right -= 1
            sum = sort_nums[left] + sort_nums[right]



if __name__ == '__main__':
    s = Solution()
    # nums = [2,7,11,15,14,12,13,5]
    # target = 18
    # result = s.twoSum_2(nums,target)
    # print(result)
    # nums= [230,863,916,585,981,404,316,785,88,12,70,435,384,778,887,755,740,337,86,92,325,422,815,650,920,125,277,336,221,847,168,23,677,61,400,136,874,363,394,199,863,997,794,587,124,321,212,957,764,173,314,422,927,783,930,282,306,506,44,926,691,568,68,730,933,737,531,180,414,751,28,546,60,371,493,370,527,387,43,541,13,457,328,227,652,365,430,803,59,858,538,427,583,368,375,173,809,896,370,789]
    # target = 542
    # result = s.twoSum_4(nums,target)
    # print(result)
    nums = [3,3,4,3]
    target = 6
    result = s.twoSum_5(nums,target)
    print(result)