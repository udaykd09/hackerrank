def checkP(s):
    s = s.lower()
    d = {}
    for k in s:
        if k==" ":
            continue
        elif k not in d:
            d[k] = 1
        else: d[k] += 1

    return "pangram" if len(d)>=26 else "not pangram"

print(checkP("afsdfsdf"))