def cc(gS):
    s = gS.strip()
    n = 0
    for s1 in s:
        if s1.istitle(): n += 1

    return n+1

cc("sdfsdSAsssfSAFsf")