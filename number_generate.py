import numpy as np
import random

# print("Enter Number of Data Centers")
NUMBER_DATA_CENTERS = 4
print("NUMBER_DATA_CENTERS =", NUMBER_DATA_CENTERS)

# print("Enter Number of Users")
NUMBER_USERS = 3
print("NUMBER_USERS =", NUMBER_USERS)

# print("Enter Total Count of Data")
COUNT_DATA = 4
print("COUNT_DATA =", COUNT_DATA)

# print("Enter Total Number of Replicas")
NUMBER_REPLICAS = 3
print("NUMBER_REPLICAS =", NUMBER_REPLICAS)

print("READ_PATTERNS = [", end="")
for i in range(NUMBER_USERS):
    print("[", end="")
    for j in range(COUNT_DATA):
        if j == COUNT_DATA-1:
            if i == NUMBER_USERS-1:
                print(random.randint(1,20), "]]", sep="")
            else:
                print(random.randint(1,20), "],", sep="")
        else:
            print(random.randint(1,20), ",", end=" ", sep="")

print("WRITE_PATTERNS = [", end="")
for i in range(NUMBER_USERS):
    print("[", end="")
    for j in range(COUNT_DATA):
        if j == COUNT_DATA-1:
            if i == NUMBER_USERS-1:
                print(random.randint(1,20), "]]", sep="")
            else:
                print(random.randint(1,20), "],", sep="")
        else:
            print(random.randint(1,20), ",", end=" ", sep="")

print("NETWORK_LATENCY = [", end="")
for i in range(NUMBER_USERS):
    print("[", end="")
    for j in range(NUMBER_DATA_CENTERS):
        if j == NUMBER_DATA_CENTERS-1:
            if i == NUMBER_USERS-1:
                print(random.randint(1,20), "]]", sep="")
            else:
                print(random.randint(1,20), "],", sep="")
        else:
            print(random.randint(1,20), ",", end=" ", sep="")

print("AGREED_SLA_COST = [", end="")
for i in range(NUMBER_USERS):
    print("[", end="")
    for j in range(COUNT_DATA):
        if j == COUNT_DATA-1:
            if i == NUMBER_USERS-1:
                print(random.randint(1,60), "]]", sep="")
            else:
                print(random.randint(1,60), "],", sep="")
        else:
            print(random.randint(1,60), ",", end=" ", sep="")

print("COST_TRANSMITTING_DATA = [", end="")
for i in range(NUMBER_DATA_CENTERS):
    print("[", end="")
    for j in range(NUMBER_DATA_CENTERS):
        if j == NUMBER_DATA_CENTERS-1:
            if i == NUMBER_DATA_CENTERS-1:
                print(random.randint(1,10), "]]", sep="")
            else:
                print(random.randint(1,10), "],", sep="")
        else:
            print(random.randint(1,10), ",", end=" ", sep="")

print("DATA_GENERATED_SINGLE_WRITE_REQUEST_M = [", end="")
for i in range(COUNT_DATA):
    if i == COUNT_DATA-1:
        print(random.randint(1, 10), end="")
        print("]")
    else:
        print(random.randint(1,10), ",", end=" ", sep="")

print("GAMMA =", 1)

print("AVG_SERVICE_RATE = [", end="")
for i in range(NUMBER_DATA_CENTERS):
    if i == NUMBER_DATA_CENTERS-1:
        print(random.randint(1, 10), end="")
        print("]")
    else:
        print(random.randint(1,10), ",", end=" ", sep="")

print("AVG_ARRIVAL_RATE = [", end="")
for i in range(NUMBER_DATA_CENTERS):
    if i == NUMBER_DATA_CENTERS-1:
        print(random.randint(1, 10), end="")
        print("]")
    else:
        print(random.randint(1,10), ",", end=" ", sep="")

print("NUM_SERVERS_EACH_DATA_CENTER = [", end="")
x = random.randint(100,200)
for i in range(NUMBER_DATA_CENTERS):
    if i == NUMBER_DATA_CENTERS-1:
        print(x, end="")
        print("]")
    else:
        print(x, ",", end=" ", sep="")

print("F = -1")
print("prevSolution = []")
