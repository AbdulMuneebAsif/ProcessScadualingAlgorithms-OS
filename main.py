
def firstComeFirstServe():

    """
                  ================ First come first serve - FCFS - OS Scadualing Algorithm ================
    """
    process = [1, 2, 3, 4]
    time_taken_by_process = [12, 10, 5, 14]
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
    process = [1, 2, 3, 4]
    time_taken_by_process = [21, 3, 6, 2]
    waiting_time_of_process = 0
    count = 0

    print("\nexecution time of processes Before sorting to SJF => ", time_taken_by_process,'\n')
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
    process = [1, 2, 3, 4]
    priority = [2, 1, 4, 3]
    time_taken_by_process = [21, 3, 6, 2]

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


if __name__ == "__main__":
    priorityAlgorithm()
