"""
Question 1

Given an array taskMemory of n positive integers representing memory required for each task, an array taskType of n positive integers representing task types, and an integer maxMemory, find the minimum time required to process all tasks. Each task takes 1 unit of time. The server can process at most two tasks in parallel only if they are the same type and together require no more than maxMemory units.


Example
Suppose n = 4, taskMemory = [7, 2, 3, 9], taskType = [1, 2, 1, 3], and maxMemory = 10.


Tasks O and 2 are processed concurrently, but the other two must be processed separately due to their memory requirements and because they are not the same type. The minimum amount of time required to process all the tasks is 3 units.


Example 2

taskMemory = [1, 2, 3, 4, 2]
taskType =   [1, 2, 1, 2, 3]
maxMemory = 4


Sample Output
4
Explanation
maxMemory = 4
The first and the third tasks are processed in parallel. The other three tasks need to be processed individually. The second and fourth use too much memory together, and the fifth is a unique type.

"""


def getMinTime(taskMemory, taskType, maxMemory):
    tasks = []
    n = len(taskMemory)
    for i in range(n):
        tasks.append({"id": i, "memory": taskMemory[i], "type": taskType[i]})
    tasks.sort(key=lambda x: x["memory"], reverse=True)

    time = 0
    processed = [False] * n

    for i in range(n):
        if processed[i]:
            continue
        time += 1
        processed[i] = True
        current_task_type = tasks[i]["type"]
        current_task_memory = tasks[i]["memory"]

        found_pair = False

        for j in range(i + 1, n):
            if (
                not processed[j]
                and tasks[j]["type"] == current_task_type
                and current_task_memory + tasks[j]["memory"] <= maxMemory
            ):
                print("Found")
                processed[j] = True
                found_pair = True
                break

    return time


taskMemory = [1, 2, 3, 4, 2]
taskType = [1, 2, 1, 2, 3]
maxMemory = 4

print(getMinTime(taskMemory, taskType, maxMemory))
