def removeMulti(s):
    i = 1
    n = 0
    while i < len(s):
        if s[i] == s[i-1]:
            s = s.replace(s[i], "")
            n += 1
            i = 1
        else: i += 1
    return s, n

def twoC(s):
    sR, n = removeMulti(s)
    if n == 1:
        print(len(sR))
    else:
        check(sR)
