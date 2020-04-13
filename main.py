from typing import List


class Solution:

  def convertListToSortKeyStr(self, items: List[str]):
    sortedList = list(set(items))
    sortedList.sort()
    return '/'.join([item for item in sortedList])

  def findBFS(self, nums: List[str], path: List[str], arrAns: List[List[str]],
              dictAns: dict):

    for i in range(len(nums)):
      newNums = nums[:i] + nums[i + 1:]
      newPath = path + [nums[i]]

      arrAns.append(newPath)
      keyStr = self.convertListToSortKeyStr(newPath)

      if keyStr not in dictAns:
        self.calcCount += 1
        dictAns[keyStr] = newPath
        self.findBFS(newNums, newPath, arrAns, dictAns)
      else:
        self.breakCount += 1

  def subsets(self, nums: List[int]) -> List[List[str]]:
    arrAns = []
    dictAns = {}
    self.calcCount = 0
    self.breakCount = 0
    strNums = [str(item) for item in nums]
    self.findBFS(strNums, [], arrAns, dictAns)

    arrAns = list(dictAns.values())

    print('Calc! %d' % self.calcCount)
    print('BREAK! %d' % self.breakCount)

    return list(dictAns.values()) + [[]]


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
