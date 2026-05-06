def job_scheduling(jobs):
    # jobs = [(name, deadline, profit)]
    jobs.sort(key=lambda x: -x[2])  # sort by profit desc
    max_deadline = max(j[1] for j in jobs)
    slots = [None] * (max_deadline + 1)
    total_profit = 0

    for name, deadline, profit in jobs:
        for t in range(deadline, 0, -1):
            if slots[t] is None:
                slots[t] = name
                total_profit += profit
                break

    scheduled = [s for s in slots if s]
    return scheduled, total_profit

jobs = [('J1',2,100),('J2',1,50),('J3',2,60),('J4',1,40)]
selected_jobs,profit=job_scheduling(jobs)
print("Selected Jobs:", selected_jobs)
print("Total Profit:", profit)