import csv
from math import radians, cos, sin, asin, sqrt
from sys import maxsize
from itertools import permutations


def read_csv():
    A = []
    with open('data/worldcities.csv', encoding="utf8", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if len(A) > 12:
                return A
            elif row['country'] == 'Norway':
                A.append(row)

    return A


def get_distance(A):
    all_distances = []

    for i in A:
        single_distance = []
        for j in A:
            x = haversine_formula(float(i['lat']), float(i['lng']), float(j['lat']), float(j['lng']))
            single_distance.append(x)
        all_distances.append(single_distance)

    return all_distances


def haversine_formula(lat1, lon1, lat2, lon2):
    R = 6371  # radius of earth in KM

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return R * c


if __name__ == '__main__':
    nor_cities = read_csv()
    all_city_distances = get_distance(nor_cities)


    def path_length(path):
        return sum(all_city_distances[i][j] for i, j in zip(path, path[1:]))

    to_visit = set(range(0, len(all_city_distances)))

    state = {(i, frozenset([0, i])): [0, i] for i in range(1, len(all_city_distances[0]))}

    for _ in range(0, len(all_city_distances) - 2):
        next_state = {}
        for position, path in state.items():
            current_node, visited = position

            # Here we check all the nodes that have not yet been visited
            for node in to_visit - visited:
                new_path = path + [node]
                new_pos = (node, frozenset(new_path))

                # Update if (current node, visited) is not in next state or we found shorter path
                #
                if new_pos not in next_state or path_length(new_path) < path_length(next_state[new_pos]):
                    next_state[new_pos] = new_path

        state = next_state

    # Find the shortest path from possible candidates
    shortest = min((path + [0] for path in state.values()), key=path_length)
    print('path: {0}, length: {1}'.format(shortest, path_length(shortest)))
