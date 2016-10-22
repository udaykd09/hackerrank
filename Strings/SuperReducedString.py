def srs(s):
    i = 1
    while i < len(s):
        if s[i] == s[i-1]:
            s = s[:i-1] + s[i+1:]
            i = 1
        else:
            i += 1
    if len(s) > 0:
        print(s)
    else:
        print("Empty String")

srs('baab')