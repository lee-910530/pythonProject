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

    def rotate(self, matrix):
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

# ...........................................................
ss = Solution()

# .........................data..............................
n = 3
m = 12
# .........................main..............................
if __name__ == '__main__':
    ans = math.factorial(n)
    (i,x) = divmod(m,10)


