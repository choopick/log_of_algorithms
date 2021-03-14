def trapping_rain(buildings):
    # no rain can be trapped if less than 3 buildings exist
    if len(buildings) < 3:
        return 0

    highest = max(buildings)
    total_rain = 0

    for current_floor in range(highest, -1, -1):
        # positions of buildings, where given current_floor exists
        indices = [i for i, building_height in enumerate(buildings) if building_height >= current_floor]
        # no rain can be piled if only one building of that height exists
        if len(indices) < 2:
            continue
        else:
            _min = min(indices)
            _max = max(indices)
            number_of_buildings_between = len(indices) - 2 # minus _min and _max
            total_rain += (_max - _min - 1) - number_of_buildings_between

    return total_rain

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))