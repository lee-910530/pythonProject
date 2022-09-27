from collections import Counter
import numpy as np
import math


class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)

    def twoSum(self, nums, target):
        dic = dict()
        for index, fig in enumerate(nums):
            if target - fig in dic:
                return dic[target - fig], index
            dic[fig] = index

    def searchInsert(self, nums, target):
        if target in nums:
            return (nums.index(target))
        else:
            nums.append(target)
            nums.sort()
            return (nums.index(target))

    def plusOne(self, digits):
        ans = 0
        digits = digits[::-1]
        ans = digits[0] + 1
        for i in range(len(digits)):
            if i != 0:
                ans = ans + digits[i] * (10 ** i)

        digits = str(ans)
        x = list(digits[::1])
        return (x)

    def singleNumber(self, nums):
        dic = dict()
        numset = set(nums)
        for i in numset:
            dic[i] = 0
            print(dic)
        for i in nums:
            dic[i] += 1
        for i in numset:
            if dic[i] == 1:
                return (i)

    def search(self, nums, target):
        l = 0
        r = len(nums)
        while (l < r):
            m = l + (r - l) // 2
            # print(m)
            if (nums[m] == target):
                return m
            elif (nums[m] < target):
                l = m + 1
            else:
                r = m
        return -1

    def sortedSquares(self, nums):
        x = list()
        for i in nums:
            x.append(i ** 2)
        x.sort()
        return (x)

    def rotate(self, nums, k):
        l = len(nums)
        nums_new = nums[l - k:] + nums[:l - k]
        return (nums_new)

    def moveZeroes(self, nums):
        nums.sort()
        l = len(nums)
        amount = nums.count(0)
        num_new = nums[l - amount - 1:] + nums[:l - amount - 1]
        return (num_new)

    def reverseString(self, s):
        return (s[::-1])

    def reverseWords(self, s):
        new = list()
        x = s.split(" ")
        for i in range(len(x)):
            new.append(x[i][::-1])
        new = " ".join((new))
        return (new)

    def rotate1(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        return matrix

    def spiralOrder(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

    def minDistance(self, word1, word2) :
        list1 = list(word1)
        list2 = list(word2)
        return(list(set(list1).intersection(set(list2))))

    def trailingZeroes(self, n) :
        # count = 0
        # ans = math.factorial(n)
        # m = ans
        # while ans >= 10:
        #     i, x = divmod(m, 10)
        #     if x == 0:
        #         count += 1
        #         m = i
        #     else:
        #         break
        # return (count)
        x = 5
        res = 0
        while x <= n:
            res += n // x
            x *= 5
        return res

    def minSubsequence(self, nums) :
        nums.sort()
        res = []
        while sum(res) <= sum(nums):
            res.append(nums.pop())
        return res

    def maxDistance(self, colors):
        i, j = 0, len(colors) - 1
        while colors[0] == colors[j]:
            j -= 1
        while colors[-1] == colors[i]:
            i += 1
        return (max(j, len(colors) - 1 - i))

    def numDecodings(self, s):
        pre_way, now_way, digit = 0, int(s > ""), ""
        for load in s:
            pre_way, now_way, digit = now_way, (10 <= int(digit + load) <= 26) * pre_way + int(
                load != "0") * now_way, load
        return (now_way)

    def containsDuplicate(self, nums) :
        set_nums = list(set(nums))
        if len(set_nums) < len(nums) :
            return True
        else :
            return False

    def maxSubArray(self, nums) :
        for i in range(1, len(nums)):
            if nums[i - 1] >= 0:
                nums[i] += nums[i - 1]
        return (max(nums))

    def fib(self, n) :
        a,b = 0,1
        for i in range(n):
            a,b = b,a + b
        return a

    def tribonacci(self, n) :
        if n == 0:
            return 0
        elif n < 3:
            return 1
        a, b, c = 0, 1, 1
        for i in range(3,n+1):
            a, b, c = b, c, a + b + c
        return c

    def runningSum(self, nums) :
        ans = []
        temp = 0
        for i in range(len(nums)):
            temp = temp + nums[i]
            ans.append(temp)
        return (ans)

    def pivotIndex(self, nums) :
        for i in range(len(nums)):
            if sum(nums[0:i]) == sum(nums[i + 1::]):
                return i

        return -1
# ...........................................................
ss = Solution()

# .........................data..............................
nums = [2,1,-1]
# .........................main..............................
if __name__ == '__main__':

    print(ss.pivotIndex(nums))


