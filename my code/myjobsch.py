jobs = input('Enter jobs: ').split()
profits = [int(x) for x in input('Enter profit numbers: ').split()]
deadline = [int(x) for x in input('Enter deadline numbers: ').split()]

profitNjobs = list(zip(profits, jobs, deadline))
profitNjobs = sorted(profitNjobs, key= lambda x: x[0], reverse = True)

slot = []
for _ in range(len(jobs)):
    slot.append(0)

tprofit = 0

ans = []
for _ in range(len(jobs)):
    ans.append('null')
    
for i in range(len(jobs)):
    job = profitNjobs[i]
    for j in range(job[2], 0, -1):
        if slot[j] == 0:
            ans[j] = job[1]
            tprofit += job[0]
            slot[j] = 1
            break

print('Jobs Scheduled: ', ans[1:])
print(trpofit)
