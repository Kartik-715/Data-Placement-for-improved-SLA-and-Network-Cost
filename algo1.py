import constants

x_m_j=[[0,0.1,0.2,0.1],
      [0.3,0.1,0.1,0],
      [0.3,0.1,0,0]]

alpha_m = [1,2,3,4]

def intersection(lst1, lst2): 
    return list(set(lst1) & set(lst2)) 

N_m = [[j for j,x in enumerate(x_m) if x > 0] for x_m in x_m_j]

O = []
G = {}

D_dash = [i for i in range(constants.COUNT_DATA)]

while len(D_dash) > 0:
    m_dash = D_dash[0]
    max_val = 1000000
    for m in D_dash:
        temp_val = alpha_m[m] / constants.AVG_ARRIVAL_RATE[m]
        if temp_val < max_val:
            max_val = temp_val
            m_dash = m
    
    O.append(m_dash)
    G[m_dash].append(m_dash)
    D_dash.remove(m_dash)

    for m in D_dash:
        P_m = N_m[m].copy()
        inter = intersection(N_m[m], N_m[m_dash])

        for i in inter:
            P_m.remove(i)
        
        similar_score = 0
        for j in P_m:
            similar_score += x_m_j[m][j]
        
        if similar_score < 0.5:
            G[m_dash].append(m)
            D_dash.remove(m)
    
    G[m_dash].append(m_dash)


    
            

            


    
