from typing import List


class Solution:

  # Convert list to sorted key
  # [3,2,1] => '1/2/3'
  def convertListToSortKeyStr(self, items: List[str]):
    return '/'.join([item for item in list(set(items))])

  def findBFS(self, nums: List[str], path: List[str], dictAns: dict):

    for i in range(len(nums)):
      newPath = path + [nums[i]]
      keyStr = self.convertListToSortKeyStr(newPath)

      if keyStr not in dictAns:
        dictAns[keyStr] = newPath
        self.findBFS(nums[:i] + nums[i + 1:], newPath, dictAns)

  def subsets(self, nums: List[int]) -> List[List[str]]:
    dictAns = {}
    strNums = [str(item) for item in sorted(nums)]

    self.findBFS(strNums, [], dictAns)

    return list(dictAns.values()) + [[]]

  # Iteratively
  def subsets3(self, nums):
    res = [[]]
    # [1,2,3]
    for num in sorted(nums):
      # 1. num = 1
      # 2. num = 2
      # 3. num = 3
      print('num %d' % num)
      res += [item + [num] for item in res]
      # 1. [] + [1] = [1]
      #
      # 2. [] + [2] = [2]
      # 2. [1] + [2] = [1,2]
      #
      # 3. [] + [3] = [3]
      # 3. [1] + [3] = [1, 3]
      # 3. [2] + [3] = [2, 3]
      # 3. [1,2] + [3] = [1, 2, 3]

      print('res', res)
      # 1. [[], [1]]
      # 2. [[], [1], [2], [1,2]]
      # 3. [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
    return res

  # URL: https://leetcode.com/problems/subsets/discuss/27301/Python-easy-to-understand-solutions-(DFS-recursively-Bit-Manipulation-Iteratively).
  # DFS recursively
  def subsets1(self, nums):
    res = []
    self.dfs(sorted(nums), 0, [], res)
    return res

  def dfs(self, nums, index, path, res):
    res.append(path)
    for i in xrange(index, len(nums)):
      self.dfs(nums, i + 1, path + [nums[i]], res)

  # Bit Manipulation
  def subsets2(self, nums):
    res = []
    nums.sort()
    for i in xrange(1 << len(nums)):
      tmp = []
      for j in xrange(len(nums)):
        if i & 1 << j:  # if i >> j & 1:
          tmp.append(nums[j])
      res.append(tmp)
    return res
    #URL END


my = Solution()
n = [1, 2, 3]
# TODO: TOO SLOW !!!
# n = [1, 2, 3, 4, 5, 6, 7, 8, 10, 0]
ans = my.subsets(n)
print("ans", ans)

# 1[2,3] - 1,2[3] - 1,2,3[]
# [[1], [1,2], [1,2,3]]
# 2[1,3] - 2,1[3] -> break!
# [[1], [1,2], [1,2,3], [2]]
# 3[1,2] - 3,1[2] -> break!
# [[1], [1,2], [1,2,3], [2], [3], [3,1]]
