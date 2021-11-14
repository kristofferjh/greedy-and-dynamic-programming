import sys, csv
from problem_1_1 import get_distance


def read_csv():
    A = []
    with open('data/worldcities.csv', encoding="utf8", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['country'] == 'Norway':
                A.append(row)

    return A


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def minimum_key(self, key, mstSet):

        # Initialize min value
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def prims_mst(self):

        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        parent = [None] * self.V  # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1  # First node is always the root of

        for _ in range(self.V):
            u = self.minimum_key(key, mstSet)

            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)


if __name__ == '__main__':
    nor_cities = read_csv()
    all_city_distances = get_distance(nor_cities)

    g = Graph(len(nor_cities))
    g.graph = all_city_distances

    g.prims_mst()

