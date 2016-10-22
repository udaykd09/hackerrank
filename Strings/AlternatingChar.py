def checkA(s):
    i = 1
    count = 0
    while i < len(s):
        if s[i] == s[i-1]:
            s = s[:i-1] + s[i:]
            count += 1
            i = 1
        i += 1
    return s, count

def dChk(s):
    s1, c1 = checkA(s)
    s2, c2 = checkA(s1)
    return c1 + c2

n = int(5)
for _ in range(0,n):
    print(dChk("AAAAABABAB"))