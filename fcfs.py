print("FIRST COME FIRST SERVE SCHEDULLING")
n = int(input("Enter number of processes : "))
d = dict()

for i in range(n):
    key = "P"+str(i+1)
    # print(key)
    a = int(input("Enter arrival time of process"+str(i+1)+": "))
    b = int(input("Enter burst time of process"+str(i+1)+": "))
    l = []
    l.append(a)
    l.append(b)
    d[key] = l
    # print(d[key])
    # print(l)

# print(d.items())        # here d.items() is converted into list
"""def key(item):
    return item[1][0]
d = sorted(d.items(),key=key)    OR"""

d = sorted(d.items(), key=lambda item: item[1][0])
"""if item[0][0] so they will sort according to key of dictionary items
if item[1][0] so they will sort according to value of dictionary items
if item[0][1] so they will sort according to value of dictionary items
if item[1][1] so result is hard to detect on what basis they sort"""
print(d)        # here d is converted into list
# print(len(d))

CT = []
for i in range(len(d)):
    if(i == 0):
        # print(d[i][1][1])
        CT.append(d[i][1][1])
    else:
        CT.append(CT[i-1]+d[i][1][1])   #CT[1]+d[2][1][1]
# if process takes ideal time for the execution of process in theoretical then 
# this CT code does not take ideal time while calculation of CT.
TAT = []
for i in range(len(d)):
    TAT.append(CT[i]-d[i][1][0])

WT = []
for i in range(len(d)):
    WT.append(TAT[i] - d[i][1][1])

avg_WT = 0
for i in WT:
    avg_WT += i  #OR avg_WT = avg_Wt + i
avg_WT = (avg_WT/n)

avg_TAT = 0
for i in TAT:
    avg_TAT += i
avg_TAT = (avg_TAT/n)

print(" Process | Arrival Time |  Burst Time  |     CT    |   TAT   |   WT   |")
for i in range(n):
    print("  ", d[i][0], "   |    ", d[i][1][0], "       |     ", d[i][1][1], "      |    ", CT[i], "   |    ", TAT[i], "   |  ", WT[i], "  |   ")
print("Average Waiting Time: ", avg_WT)
print("Average Turn Over Time: ", avg_TAT)

