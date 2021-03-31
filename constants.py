NUMBER_DATA_CENTERS = 4
NUMBER_USERS = 4
COUNT_DATA = 3
NUMBER_REPLICAS = 2
READ_PATTERNS = [[0, 1, 2, 1],
                 [3, 1, 1, 1],
                 [3, 1, 1, 1],
                 [0, 0, 0, 10]]
WRITE_PATTERNS = [[0, 1, 2, 1],
                  [3, 1, 1, 1],
                  [3, 1, 1, 1],
                  [0, 0, 0, 10]]
NETWORK_LATENCY = [[0, 1, 2, 1],
                   [3, 1, 1, 1],
                   [3, 1, 1, 1],
                   [0, 0, 0, 10]]  # li,j
AGREED_SLA_COST = [[5, 5, 5, 5],
                   [5, 5, 5, 5],
                   [5, 5, 5, 5],
                   [5, 5, 5, 5]]  # Qi,m
COST_TRANSMITTING_DATA = [[0, 3, 2, 0],
                          [3, 0, 0, 1],
                          [0, 2, 0, 8],
                          [10, 2, 8, 0]]  # C_e

DATA_GENERATED_SINGLE_WRITE_REQUEST_M = [3,10,2,6] #tau_m_w
GAMMA = 1
AVG_SERVICE_RATE = [2, 2, 2, 5]  # mu
AVG_ARRIVAL_RATE = [2, 2, 2, 10]  # lambda
NUM_SERVERS_EACH_DATA_CENTER = [3, 3, 3, 3]  # Nj
F = -1
prevSolution = []
