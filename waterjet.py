def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def can_reach_target(current_state, target):
    return current_state[0] == target or current_state[1] == target

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    if target % gcd(jug1_capacity, jug2_capacity) != 0:
        print("Target cannot be achieved with given jug capacities.")
        return
   
    jug1_current = 0
    jug2_current = 0
    steps = []
   
    while not can_reach_target((jug1_current, jug2_current), target):
        if jug1_current == 0:
            jug1_current = jug1_capacity
            steps.append((jug1_current, jug2_current))
        elif jug2_current == jug2_capacity:
            jug2_current = 0
            steps.append((jug1_current, jug2_current))
        else:
            transfer_amount = min(jug1_current, jug2_capacity - jug2_current)
            jug1_current -= transfer_amount
            jug2_current += transfer_amount
            steps.append((jug1_current, jug2_current))
   
    steps.append((jug1_current, jug2_current))
   
    return steps

def main():
    jug1_capacity = int(input("Enter the capacity of the first jug: "))
    jug2_capacity = int(input("Enter the capacity of the second jug: "))
    target = int(input("Enter the target water level: "))
   
    steps = water_jug_problem(jug1_capacity, jug2_capacity, target)
   
    if steps:
        print("Steps to reach the target:")
        for step in steps:
            print(f"Jug 1: {step[0]} | Jug 2: {step[1]}")
    else:
        print("No solution exists for the given inputs.")
main()
