import main
import constants
import sys
from itertools import permutations


def updatePatterns():
    # update read/write patterns from constants.
    pass


def minDistance(dist, sptSet):
    minVal = sys.maxsize
    minIndex = -1
    for v in range(constants.NUMBER_DATA_CENTERS):
        if dist[v] < minVal and sptSet[v] is False:
            minVal = dist[v]
            minIndex = v

    return minIndex


def dijkstra(src):
    graph = constants.COST_TRANSMITTING_DATA
    dist = [sys.maxsize] * constants.NUMBER_DATA_CENTERS
    dist[src] = 0
    sptSet = [False] * constants.NUMBER_DATA_CENTERS

    for _ in range(constants.NUMBER_DATA_CENTERS):
        u = minDistance(dist, sptSet)
        sptSet[u] = True
        for v in range(constants.NUMBER_DATA_CENTERS):
            if graph[u][v] > 0 and sptSet[v] is False and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]

    return dist


def findRelocationCost(prevSolution, newSolution):
    totalCost = 0
    # data X data centers
    for m in range(constants.COUNT_DATA):
        src = prevSolution[m]
        dst = newSolution[m]

        srcIdx = []
        dstIdx = []
        for i, j in enumerate(src):
            if j == 1:
                srcIdx.append(i)

        for i, j in enumerate(dst):
            if j == 1:
                dstIdx.append(i)

        print("Source Index", srcIdx)
        print("Destination Index", dstIdx)

        distMatrix = {}
        for d in dstIdx:
            dstArray = dijkstra(d)
            distMatrix[d] = dstArray

        l = list(permutations(dstIdx))

        tempCost = sys.maxsize
        for perm in l:
            cost = 0
            srcIdxCopy = srcIdx.copy()
            for d in perm:
                dstArray = distMatrix[d]
                minCost = sys.maxsize
                minIdx = -1
                for srcT in srcIdxCopy:
                    if dstArray[srcT] < minCost:
                        minCost = dstArray[srcT]
                        minIdx = srcT

                cost += minCost
                srcIdxCopy.append(minIdx)

            tempCost = min(cost, tempCost)

        print("TempCost: ", tempCost)
        totalCost += tempCost

    return totalCost


def relocate():
    pass


x = [[0, 0, 1, 1],
     [0, 0, 1, 1],
     [0, 1, 0, 1],
     [0, 0, 1, 1]]

y = [[1, 0, 0, 1],
     [1, 0, 0, 1],
     [1, 0, 1, 0],
     [0, 1, 1, 0]]

print("Cost", findRelocationCost(x, y))


def run():
    if constants.F == -1:
        constants.F, constants.prevSolution = main.run()
        return

    updatePatterns()
    F_dash, newSolution = main.run()
    relocationCost = findRelocationCost(constants.prevSolution, newSolution)
    if constants.F <= F_dash + relocationCost:
        relocate()  # Feasible relocation
