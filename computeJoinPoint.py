def computeJoinPoint(s1,s2):
    while s1 != s2:
        if s1 < s2:
            s1 += sum(map(int,str(s1)))
        else:
            s2 += sum(map(int,str(s2)))
    return s1
