\* Stage_1 *\
Minimize
OBJ: 5.2 X_03 + 5.2 X_13 + 5.2 X_23
Subject To
Placement_Constraint_10: X_00 + X_01 + X_02 + X_03 <= 1
Placement_Constraint_11: X_10 + X_11 + X_12 + X_13 <= 1
Placement_Constraint_12: X_20 + X_21 + X_22 + X_23 <= 1
Placement_Constraint_20: X_00 + X_01 + X_02 + X_03 >= 1
Placement_Constraint_21: X_10 + X_11 + X_12 + X_13 >= 1
Placement_Constraint_22: X_20 + X_21 + X_22 + X_23 >= 1
Bounds
X_00 <= 1
X_01 <= 1
X_02 <= 1
X_03 <= 1
X_10 <= 1
X_11 <= 1
X_12 <= 1
X_13 <= 1
X_20 <= 1
X_21 <= 1
X_22 <= 1
X_23 <= 1
End
