class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def create(self, arr):
        root = self
        for n in arr:
            newN = Node(n)
            self.next = newN
            self = self.next
        return root

    def printll(self):
        root = self
        while self is not None:
            print self.value
            self = self.next
        return root

    def reverse(self):
        current = self
        last = None
        while current:
            next = current.next
            current.next = last
            last = current
            current = next
        return last


root = Node(1)
root.create([2,3,4,5,6])
root = root.printll()
root_r = root.reverse()
#root_r = root.reverse_recursive()
root_r = root_r.printll()