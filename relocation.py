import main
import constants

def updatePatterns():
    # update read/write patterns from constants.
    pass

def findRelocationCost(prevSolution, newSolution):
    # Some graph algorithm
    return 3485

def relocate():
    pass

def run():
    if constants.F == -1:
        constants.F, constants.prevSolution = main.run()
        return

    updatePatterns()
    F_dash, newSolution = main.run()
    relocationCost = findRelocationCost(constants.prevSolution, newSolution)
    if constants.F <= F_dash + relocationCost:
        relocate()  # Feasible relocation
