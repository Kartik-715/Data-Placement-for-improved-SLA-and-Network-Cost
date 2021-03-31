import stage1
import algo1
import algo2

def run():
    x_m_j, alpha_m = stage1.run()
    G, O = algo1.run(x_m_j, alpha_m)
    totalOperationalCost, placementSolution = algo2.run(G, O)
    print(totalOperationalCost, placementSolution)
    return totalOperationalCost, placementSolution


run()