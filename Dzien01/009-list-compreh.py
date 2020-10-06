import time

"""
Wyrażenia listotwórcze
"""
LOOP = 10_000

ts1 = time.time()
for _ in range(LOOP):
    result = []
    for x in range(1,101):
        if x%3==0:
            result.append( x**2 )
ts2 = time.time()
ts_loop = ts2-ts1
print(ts_loop)
#print(result)

# "A" if x>10 else "B"
# ("B","A")[x>10]

ts1 = time.time()
[ [x**2 for x in range(1,101) if x%3==0] for _ in range(LOOP)]
ts2 = time.time()
ts_comp = ts2-ts1
print(ts_comp)
print("COMP vs LOOP: ", ts_comp/ts_loop*100)