import constants
import sys


# data_solution -> dictionary of (data, datacenters_list)

def minDistance(dist, sptSet):
    minVal = sys.maxsize
    for v in range(constants.NUMBER_DATA_CENTERS):
        if dist[v] < minVal and sptSet[v] == False:
            minVal = dist[v]
            minIndex = v

    return minIndex


def dijkstra(src, src_solution):
    graph = constants.COST_TRANSMITTING_DATA
    dist = [sys.maxsize] * constants.NUMBER_DATA_CENTERS
    dist[src] = 0
    sptSet = [False] * constants.NUMBER_DATA_CENTERS

    for cout in range(constants.NUMBER_DATA_CENTERS):
        u = minDistance(dist, sptSet)
        sptSet[u] = True
        for v in range(constants.NUMBER_DATA_CENTERS):
            if graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]

    ans = 0
    for d in src_solution:
        ans += dist[d]

    return ans


def calculateNetworkCommunicationCost(data_solution):
    finalAns = 0
    for m, m_solution in data_solution.items():
        tempAns = -1
        for d in m_solution:  # Now d is my source
            tempAns = max(tempAns, dijkstra(d, m_solution))

        rate_write_requests_data_m = 0
        for i in range(constants.NUMBER_USERS):
            rate_write_requests_data_m += constants.WRITE_PATTERNS[i][m]

        tempAns *= rate_write_requests_data_m
        tempAns *= constants.DATA_GENERATED_SINGLE_WRITE_REQUEST_M[m]

        finalAns += tempAns

    return finalAns


def calculateSLACost(data_solution):
    x = 10


def calculateOperationalCost(data_solution):
    networkCost = calculateNetworkCommunicationCost(data_solution)
    slaCost = calculateSLACost(data_solution)

    return slaCost + networkCost
