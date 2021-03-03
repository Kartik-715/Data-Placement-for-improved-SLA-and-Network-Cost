import pulp as p
import numpy as np
import constants

N_j = np.asarray(constants.NUM_SERVERS_EACH_DATA_CENTER)
u_j = np.asarray(constants.AVG_SERVICE_RATE)
lambda_j = np.asarray(constants.AVG_ARRIVAL_RATE)
l_i_j = np.asarray(constants.NETWORK_LATENCY)
Q_i_m = np.asarray(constants.AGREED_SLA_COST)

L_i_j = np.zeros((constants.NUMBER_USERS, constants.NUMBER_DATA_CENTERS))  # 1 / (np.dot(N_j, u_j) - lambda_j) + l_i_j

for i in range(0, constants.NUMBER_USERS):
    for j in range(0, constants.NUMBER_DATA_CENTERS):
        L_i_j[i][j] = 1 / ((N_j[j] * u_j[j]) - lambda_j[j]) + l_i_j[i][j]

L_m_j = np.zeros((constants.COUNT_DATA, constants.NUMBER_DATA_CENTERS))
print(L_m_j.shape)

for m in range(0, constants.COUNT_DATA):
    for j in range(0, constants.NUMBER_DATA_CENTERS):
        for i in range(0, constants.NUMBER_USERS):
            L_m_j[m][j] += max(0, L_i_j[i][j] - Q_i_m[i][m])
        L_m_j[m][j] *= constants.GAMMA

variable_names = [str(j) + str(i) for j in range(0, constants.COUNT_DATA) for i in
                  range(0, constants.NUMBER_DATA_CENTERS)]
variable_names.sort()

model = p.LpProblem("Stage_1", p.LpMinimize)
DV_variables = p.LpVariable.matrix("X", variable_names, lowBound=0, upBound=1)
allocation = np.array(DV_variables).reshape(constants.COUNT_DATA, constants.NUMBER_DATA_CENTERS)  # 3 * 4

obj_func = p.lpSum(L_m_j * allocation)
model += obj_func

for m in range(constants.COUNT_DATA):
    model += p.lpSum(
        allocation[m][j] for j in range(constants.NUMBER_DATA_CENTERS)) <= 1, "Placement Constraint 1" + str(m)
    model += p.lpSum(
        allocation[m][j] for j in range(constants.NUMBER_DATA_CENTERS)) >= 1, "Placement Constraint 2" + str(m)

print(model)
model.writeLP("Stage_1.lp")
model.solve(p.PULP_CBC_CMD())
status = p.LpStatus[model.status]
print(status)

print("Total Cost:", model.objective.value())

# Decision Variables

for v in model.variables():
    try:
        print(v.name, "=", v.value())
    except:
        print("error couldnt find value")


dual_variable_names = [str(0) + str(j) for j in range(constants.COUNT_DATA)]
dual_variable_names.sort()
DP_variables = p.LpVariable.matrix("Alpha", dual_variable_names, lowBound=0)
dual_model = p.LpProblem("Stage_1_Dual", p.LpMaximize)
alpha_star = np.array(DP_variables).reshape(1,constants.COUNT_DATA)
dual_obj_func = p.lpSum(alpha_star)

dual_model += dual_obj_func
for m in range(0,constants.COUNT_DATA):
    for j in range(0,constants.NUMBER_DATA_CENTERS):
        dual_model += p.lpSum(alpha_star[0][m]) <= L_m_j[m][j], "Dual Constraint_" + str(m) + str(j)

print(dual_model)
dual_model.writeLP("Stage_1_dual.lp")

dual_model.solve(p.PULP_CBC_CMD())
dual_status = p.LpStatus[model.status]
print(dual_status)

print("Dual Total Cost:", dual_model.objective.value())

# Decision Variables

for v in dual_model.variables():
    try:
        print(v.name, "=", v.value())
    except:
        print("error couldnt find value")
