class Solution(object):
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    def findFunny(self, s):
        i = 1
        n = len(s)
        r = s[::-1]
        while i < int(n / 2):
            if (ord(s[i]) - ord(s[i - 1])) != (ord(r[i]) - ord(r[i - 1])):
                return "Not Funny"
            else:
                i += 1
        return "Funny"

    def start(self):
        n = int(raw_input())
        for _ in range(n):
            print self.findFunny(raw_input())



mySol = Solution()
mySol.start