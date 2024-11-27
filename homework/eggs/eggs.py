def eggs_solution(breaks):
    step = 14
    current_floor = 0

    while current_floor + step <= 100:
        current_floor += step
        if breaks(current_floor):
            current_floor -= step
            break
        step -= 1

    for floor in range(current_floor + 1, current_floor + step + 1):
        if breaks(floor):
            return floor - 1
    return 100

#juhu