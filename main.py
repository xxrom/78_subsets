from typing import List

class Solution:
  def convertListToStr(self, items: List[str]):
      sortedList = list(set(items))
      sortedList.sort()
      return '/'.join([item for item in sortedList])

  def findBFS(self, nums: List[str], path: List[str], ans: List[List[str]] ):

    for i in range(len(nums)):
      newNums = nums[:i] + nums[i+1:]
      newPath = path + [nums[i]]
      print(newPath)
      ans.append(newPath)
      self.findBFS(newNums, newPath, ans)



  def subsets(self, nums: List[int]) -> List[List[str]]:
    ans = []
    strNums = [str(item) for item in nums]
    print(strNums)
    self.findBFS(strNums, [], ans)



    newAns = list(set([self.convertListToStr(itemList) for itemList in ans]))
    print(newAns)

    ans = [[int(innerItem) for innerItem in item.split('/')] for item in newAns]
    ans.append([])
    print(ans)

    return ans


my = Solution()
n = [1,2,3]
# TODO: TOO SLOW !!!
# n = [1,2,3,4,5,6,7,8,10,0]
ans = my.subsets(n)
# print("ans", ans)
