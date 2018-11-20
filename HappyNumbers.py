def happyNums(n):
    result = [1]
    hN = [1]
    uHN = []
    c = 2
    while len(hN) < n:
        l = happy(c, hN, uHN, [])
        c += 1
        if len(l) is 1:
            continue
        if l[-1]:
            hN.append(x for x in l[:-1])
            result.append(l[0])
        else:
            uHN.append(x for x in l[:-1])
    return result

def happy(i, hN, uhN, l):
    if i in hN:
        l.append(True)
        return l
    elif i in uhN or i in l:
        l.append(False)
        return l
    l.append(i)
    n = 0
    for s in str(i):
        n += int(s)**2
    return happy(n, hN, uhN, l)