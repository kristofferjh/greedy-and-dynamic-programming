import random


def printJobScheduling(arr, t):
    n = len(arr)

    # Sort all jobs according to
    # decreasing order of profit
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    result = [False] * t

    job = ['-1'] * t

    # Iterate through all given jobs
    for i in range(len(arr)):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):

            # Free slot found
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break

    # print the sequence
    print(job)


def generateArray():
    Arr = []
    numberOfJobs = 50

    for i in range(0, numberOfJobs):
        job = ['', 0, 0]
        for j in range(0, len(job)):
            profit = random.randint(1, 100)
            deadline = random.randint(1, 40)
            job[0] = i
            job[1] = deadline
            job[2] = profit

        Arr.append(job)
    return Arr


if __name__ == '__main__':
    jobs = generateArray()
    print(jobs)

    print("The maximum profit under the constraints of the deadlines for all jobs")

    printJobScheduling(jobs, 10)
