import constants
import sys
import numpy as np
import stage1

print("Running Cluster Based Data Placement")
print("Inputs: O, G")


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
    finalCost = 0

    for m in range(constants.COUNT_DATA):
        tempCost = -1
        m_solution = []
        for j in range(constants.NUMBER_DATA_CENTERS):
            if data_solution[m][j] == 1:
                m_solution.append(j)

        for d in m_solution:
            tempCost = max(tempCost, dijkstra(d, m_solution))

        rate_write_requests_data_m = 0
        for i in range(constants.NUMBER_USERS):
            rate_write_requests_data_m += constants.WRITE_PATTERNS[i][m]

        tempCost *= rate_write_requests_data_m
        tempCost *= constants.DATA_GENERATED_SINGLE_WRITE_REQUEST_M[m]

        finalCost += tempCost

    return finalCost


def calculateSLACost(data_solution):
    finalCost = 0
    for m in constants.COUNT_DATA:
        for j in constants.NUMBER_DATA_CENTERS:
            finalCost += (stage1.L_m_j[m][j] * data_solution[m][j])
    return finalCost


def calculateOperationalCost(data_solution):
    networkCost = calculateNetworkCommunicationCost(data_solution)
    slaCost = calculateSLACost(data_solution)

    return slaCost + networkCost


def run(G, O):
    cluster_centers = O
    clusters = G
    operationalCost = 0
    placementSolution = np.zeros((constants.COUNT_DATA, constants.NUMBER_DATA_CENTERS))

    for m_dash in cluster_centers:
        cluster = clusters[m_dash]
        N_m_dash = []
        for j in placementSolution[m_dash]:
            if placementSolution[m_dash][j] > 0:
                N_m_dash.append(j)

        tempOperationalCostArr = []
        for j in N_m_dash:
            tempPlacementSolution = placementSolution
            for m in cluster:
                tempPlacementSolution[m][j] = 1
            operationalCost = calculateOperationalCost(tempPlacementSolution)
            tempOperationalCostArr.append((operationalCost, j))

        tempOperationalCostArr.sort()

        for j in N_m_dash:
            while not cluster:
                data = cluster[0]
                cluster.pop(0)
                placementSolution[data][j] = 1

                possibleDataCenters = []
                for j_dash in range(constants.NUMBER_DATA_CENTERS):
                    if j_dash == j:
                        continue
                    possibleDataCenters.append(j_dash)

                for k in range(constants.NUMBER_REPLICAS - 1):
                    minIncreaseCost = sys.maxsize
                    for j_dash in possibleDataCenters:
                        tempPlacementSolution = placementSolution
                        tempPlacementSolution[data][j_dash] = 1
                        operationalCost = calculateOperationalCost(tempPlacementSolution)

                        if operationalCost < minIncreaseCost:
                            minIncreaseCost = operationalCost
                            jBest = j_dash

                    placementSolution[data][jBest] = 1
                    possibleDataCenters.remove(jBest)

        return calculateOperationalCost(placementSolution), placementSolution
