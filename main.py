import pandas as pd

path = r"C:\Users\h\Desktop\myExcleFile.csv"
df = pd.read_csv(path)


def firstComeFirstServe():
    """
                  ================ First come first serve - FCFS - OS Scadualing Algorithm ================
    """

    # process = [1, 2, 3, 4]
    process = df["Process"].tolist()
    # time_taken_by_process = [12, 10, 5, 14]
    time_taken_by_process = df["ET"].tolist()

    waiting_time_of_process = 0
    count = 0

    print("  Process", "\t", "Execution Time")
    for j in range(len(process)):
        print("\t", process[j], "\t\t\t", time_taken_by_process[j])

    print("\n")

    for i in range(len(process)):
        print("The waiting time of process", process[i], "is =>", waiting_time_of_process, "ms")
        waiting_time_of_process = waiting_time_of_process + time_taken_by_process[i]
        print("The Execution time of process", process[i], "is =>", waiting_time_of_process, "ms", "\n")

        if i < len(process) - 1:
            count = count + waiting_time_of_process

    print("Total waiting time => ", count, "ms")
    print("Average waiting time => ", str(count) + "/" + str(len(process)), "=", count / len(process), "ms")


def shortestJobFirst():
    """
                  ================ Shortest Job First - SRF - OS Scadualing Algorithm ================
    """
    # process = [1, 2, 3, 4]
    process = df["Process"].tolist()
    # time_taken_by_process = [12, 10, 5, 14]
    time_taken_by_process = df["ET"].tolist()
    waiting_time_of_process = 0
    count = 0

    print("\nexecution time of processes Before sorting to SJF => ", time_taken_by_process, '\n')
    time_taken_by_process.sort()

    print("  Process", "\t", "Execution Time")

    for j in range(len(process)):
        print("\t", process[j], "\t\t\t", time_taken_by_process[j])

    print("\n")

    for i in range(len(process)):

        print("The waiting time of process", process[i], "is =>", waiting_time_of_process, "ms")
        waiting_time_of_process = waiting_time_of_process + time_taken_by_process[i]
        print("The Execution time of process", process[i], "is =>", waiting_time_of_process, "ms", "\n")

        if i < len(process) - 1:
            count = count + waiting_time_of_process

    print("Total waiting time => ", count, "ms")
    print("Average waiting time => ", str(count) + "/" + str(len(process)), "=", count / len(process), "ms")


def priorityAlgorithm():
    """
                  ================ Priority Algorithm - OS Scadualing Algorithm ================
    """

    # process = [1, 2, 3, 4]
    process = df["Process"].tolist()
    # time_taken_by_process = [12, 10, 5, 14]
    time_taken_by_process = df["ET"].tolist()
    # priority = [2, 1, 4, 3]
    priority = df["Priority"].tolist()

    list_after_priority = [x for _, x in sorted(zip(priority, time_taken_by_process))]

    waiting_time_of_process = 0
    count = 0

    print("\n\t\t\t\t =========================== Processes Before Assigning Priority",
          "============================ \n")

    print("  Process", "\t", "Execution Time", "\t", "Priority")

    for j in range(len(process)):
        print("\t", process[j], "\t\t\t", time_taken_by_process[j], "", "\t\t\t\t", priority[j])

    print("\n")

    print("\n\t\t\t\t ============================ Processes After Assigning Priority",
          "============================ \n")
    print("  Process", "\t", "Execution Time", "\t", "Priority")

    for j in range(len(process)):
        print("\t", priority[j], "\t\t\t", list_after_priority[j], "", "\t\t\t\t", process[j])

    print("\n")

    for i in range(len(process)):

        print("The waiting time of process", process[i], "is =>", waiting_time_of_process, "ms")
        waiting_time_of_process = waiting_time_of_process + list_after_priority[i]
        print("The Execution time of process", process[i], "is =>", waiting_time_of_process, "ms", "\n")

        if i < len(process) - 1:
            count = count + waiting_time_of_process

    print("Total waiting time => ", count, "ms")
    print("Average waiting time => ", str(count) + "/" + str(len(process)), "=", count / len(process), "ms")


def findWaitingTime(processes, numberOfProcesses, executionTime, wt, quantum):
    remainingTime = [0] * numberOfProcesses

    # Copy the burst time into rt[]
    for i in range(numberOfProcesses):
        remainingTime[i] = executionTime[i]
    currentTime = 0

    # Keep traversing processes in round-robin manner until all of them are not done.
    while 1:
        done = True

        # Traverse all processes one by
        # one repeatedly
        for i in range(numberOfProcesses):

            # If burst time of a process is greater
            # than 0 then only need to process further
            if remainingTime[i] > 0:
                done = False  # There is a pending process

                if remainingTime[i] > quantum:

                    # Increase the value of t i.e. shows
                    # how much time a process has been processed
                    currentTime = currentTime + quantum

                    # Decrease the burst_time of current
                    # process by quantum
                    remainingTime[i] -= quantum

                # If burst time is smaller than or equal
                # to quantum. Last cycle for this process
                else:

                    # Increase the value of t i.e. shows
                    # how much time a process has been processed
                    currentTime = currentTime + remainingTime[i]

                    # Waiting time is current time minus
                    # time used by this process
                    wt[i] = currentTime - executionTime[i]

                    # As the process gets fully executed
                    # make its remaining burst time = 0
                    remainingTime[i] = 0

        # If all processes are done
        if done:
            break


# Function to calculate average waiting
# and turn-around times.
def findAverageTime(processes, n, executionTime, quantum):
    waiting_time = [0] * n

    # Function to find waiting time
    # of all processes
    findWaitingTime(processes, n, executionTime,
                    waiting_time, quantum)

    # Display processes along with all details

    print("Processes Execution Time	 Waiting Time")
    total_waiting_time = 0
    total_tat = 0
    for i in range(n):
        total_waiting_time = total_waiting_time + waiting_time[i]
        print(" ", i + 1, "\t\t", executionTime[i], "", "\t\t\t\t", waiting_time[i])

    print("\nAverage waiting time = %.5f " % (total_waiting_time / n))


def roundRobin():
    """
                      ================ Round Robin - OS Scadualing Algorithm ================
    """
    # process = [1, 2, 3, 4]

    process = df["Process"].tolist()
    # time_taken_by_process = [12, 10, 5, 14]
    time_taken_by_process = df["ET"].tolist()

    n = len(process)

    # Time quantum
    quantum = 5
    findAverageTime(process, n, time_taken_by_process, quantum)


def menu():
    choose = 0

    while 1:

        print("\n\t\t\t\t ================================ MENU  ================================ \n")
        print("Press 1: for First Come first Serve Algorithm.")
        print("Press 2: for Shortest Job First Algorithm.")
        print("Press 3: for Priority Algorithm.")
        print("Press 4: for Round Robin Algorithm.")
        print("Press 5: for all Algorithms.")
        print("Press 6: Exit/Terminate.")
        print("\n\t\t\t\t ======================================================================= \n")
        choose = eval(input("Enter Your choice : "))

        if choose == 1:

            print(firstComeFirstServe.__doc__)
            firstComeFirstServe()

        elif choose == 2:

            print(shortestJobFirst.__doc__)
            shortestJobFirst()

        elif choose == 3:

            print(priorityAlgorithm.__doc__)
            priorityAlgorithm()

        elif choose == 4:

            print(roundRobin.__doc__)
            roundRobin()

        elif choose == 5:

            print(firstComeFirstServe.__doc__)
            firstComeFirstServe()

            print(shortestJobFirst.__doc__)
            shortestJobFirst()

            print(priorityAlgorithm.__doc__)
            priorityAlgorithm()

            print(roundRobin.__doc__)
            roundRobin()

        elif choose == 6:
            exit()

        else:
            print("Invalid input....")


if __name__ == "__main__":
    menu()
