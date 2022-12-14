if __name__ == '__main__':
    # Python program for implementation of RR Scheduling
    total_p_no = int(input("Enter Total Process Number: "))
    total_time = 0 
    completion_time = 0

    # proc is process list
    proc = []
    wait_time = 0
    turnaround_time = 0
    for _ in range(total_p_no):
        # Getting the input for process
        print("Enter process arrival_time  and burst_time : ",end="") 
        input_info = list(map(int, input().split(" ")))
        arrival_time, burst_time, remaining_time = input_info[0], input_info[1], input_info[1]

        # processes are appended to the proc list in following format
        proc.append([arrival_time, burst_time, remaining_time, 0])

        # total_time gets incremented with burst_time time of each process
        total_time += burst_time
        # print(total_time)

    time_quantum = int(input("Enter time quantum: "))
    # print(proc)

    # Keep traversing in round robin manner until the total_time == 0
    while total_time != 0:
        # traverse all the processes
        for i in range(len(proc)):
            # proc[i][2] here refers to remaining_time for each process i.e "i"
            if proc[i][2] <= time_quantum and proc[i][2] >= 0:
                completion_time += proc[i][2]
                total_time -= proc[i][2]
                # the process has completely ended here thus setting it's remaining time to 0.
                proc[i][2] = 0 
            elif proc[i][2] > 0:
                # if process has not finished, decrementing it's remaining time by time_quantum
                proc[i][2] -= time_quantum
                total_time -= time_quantum
                completion_time += time_quantum
            if proc[i][2] == 0 and proc[i][3] != 1:
                # if remaining time of process is 0
                # and 
                # individual waiting time of process has not been calculated i.e flag
                turnaround_time += completion_time - proc[i][0]
                wait_time += completion_time - proc[i][0] - proc[i][1]
                # flag is set to 1 once wait time is calculated
                proc[i][3] = 1 

    print("\nAvg Waiting Time is ", wait_time  / total_p_no)
    print("Avg Turnaround Time is ", turnaround_time  / total_p_no)
    