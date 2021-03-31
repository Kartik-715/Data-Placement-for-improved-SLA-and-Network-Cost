print("Running Cluster Based Data Placement")
print("Inputs: O, G")

def calculateOperationalCost():
    return 1

def run(O, G):
    cluster_centers = O
    clusters = G
    for m_dash in cluster_centers:
        cluster = clusters[m_dash]
