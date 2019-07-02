le = int(input())
gs = list(map(int,input().split()))
re = []
for i in range(len(g)):
    if g.count(gs[i]) > 1:
        if gs[i] not in re:
            re.append(gs[i])
re.sort()
if len(re)==0:
    print("unique")
else:
    print(" ".join([str(elem) for elem in r]))
