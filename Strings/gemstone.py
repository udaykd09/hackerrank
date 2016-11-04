class Solution(object):
    elements = []
    gems = 0
    def prepare_elements(self, s):
        for s1 in s:
            if s1 not in self.elements:
                self.elements.append(s1)
        print "elements", self.elements

    def check_gems(self, s):
        temp = []
        for s1 in s:
            if s1 in self.elements and s1 not in temp:
                temp.append(s1)
        print "temp", temp
        return temp

    def start(self):
        for i in range(0, int(raw_input())):
            if i == 0:
                self.prepare_elements(raw_input())
            else:
                self.elements = self.check_gems(raw_input())
                if not self.elements:
                    return 0
        return len(self.elements)

mySol = Solution()
print(mySol.start())



