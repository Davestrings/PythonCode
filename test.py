from itertools import permutations
d = {}
next = {}
r = {}
reset = []
mars = {}
for _ in range(int(input())):
    s = input()
    if s == s[::-1]:
        print("%.4f" % 0)
        continue
    for o,n in zip(sorted(list(set(s)),key=lambda x: s.count(x)),'1234'):
        s=s.replace(o,n)
    if s > s[::-1]:
        s = s[::-1]
    if s in r:
        print(r[s])
        continue
    s = tuple(s)
    pers = []
    if ''.join(sorted(s)) in mars:
        pers = mars[''.join(sorted(s))]
    else:
        pers = mars[''.join(sorted(s))] = set(permutations(s))
    pals = {e for e in pers if e == e[::-1]}
    bf = len(s)*(len(s)-1)/2
    def next_not_pal(s):
        r = []
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                s[i], s[j] = s[j], s[i]
                if tuple(s) not in pals:
                    r.append(tuple(s))
                s[i], s[j] = s[j], s[i]
        return r
    for e in pers:
        if e not in next:
            next[e] = next_not_pal(list(e))
            d[(e,1)]=(bf-len(next[e]))/bf
    
    def problem(e,m):
        if (e,m) in d:
            return d[(e,m)]
        s = sum(problem(ne,m-1) for ne in next[e])
        d[(e,m)] = s/bf
        return s/bf
        

    su = problem(s,1)
    m = 2
    lp = su
    cp = problem(s,m)
    lr = 0
    while lp == 0 or abs(cp/lp-lr)>1e-15:
        su += m*cp
        if lp != 0:
            lr = cp/lp
        lp = cp
        m+=1
        cp = problem(s,m)

    lr = cp/lp
    lsu = 0
    while su-lsu > 1e-8:
        lsu = su
        su += m*cp
        cp *= lr
        m+=1
    if "%.4f" % su not in reset:
        reset.append("%.4f" % su)
    r[''.join(s)] = "%.4f" % su
    print("%.4f" % su)
