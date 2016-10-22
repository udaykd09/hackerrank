def findFunny(s):
    i = 1
    n = len(s)
    r = s[::-1]
    while i <= int(n/2):
        if((ord(s[i])-ord(s[i-1])) != (ord(r[i])-ord(r[i-1]))):
            return "Not Funny"
        else: return "Funny"


findFunny()