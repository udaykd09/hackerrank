class Solution(object):

    def getIndex(self, v):
        _ = int(raw_input())
        arr = map(int, raw_input().split(" "))
        return arr.index(v)

mySol = Solution()
print(mySol.getIndex(int(raw_input())))