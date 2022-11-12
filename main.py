
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
    time_taken_by_process = [12, 10, 5, 14]
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
    time_taken_by_process = [12, 10, 5, 14]

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

def roundRobin():
    """
                      ================ Round Robin - OS Scadualing Algorithm ================
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
