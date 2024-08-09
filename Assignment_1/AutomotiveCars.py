"""
Full Name: Youssef BENTALEB
"""

from heapq import *  # Will be used to find the MST


# A class for cars
class AutomotiveCar:

    f = open("data.txt", "r")
    numCars = int(f.readline()[:-1])
    connectivity_range = int(f.readline()[:-1])
    used_IDs = [-1]

    def __init__(self) -> None:
        tmp = AutomotiveCar.used_IDs[-1] + 1
        self.ID = tmp
        AutomotiveCar.used_IDs.append(tmp)
        self.coords = list(map(float, self.f.readline()[:-1].split()))


# Distance between two cars
def distance(a: AutomotiveCar, b: AutomotiveCar) -> float:
    x_a, y_a = a.coords
    x_b, y_b = b.coords
    return ((x_a - x_b) ** 2 + (y_a - y_b) ** 2) ** 0.5


# List of all cars
allCars = []
car = AutomotiveCar()
while car.coords:
    allCars.append(car)
    car = AutomotiveCar()
AutomotiveCar.used_IDs.pop()
del car


# Building the graph
def generateGraph() -> dict:
    return {
        c.ID: sorted(
            [
                (d.ID, distance(c, d))
                for d in allCars
                if (d.ID != c.ID and distance(c, d) <= AutomotiveCar.connectivity_range)
            ],
            key=lambda x: x[1],
        )
        for c in allCars
    }


graph = generateGraph()


# Displaying all edges
def display_all_edges() -> None:
    print("All edges:")
    visited = []
    for k, v in graph.items():
        for k_, d in v:
            if sorted(str(k) + str(k_)) not in visited:
                print((k, k_, round(d, 2)), end=" ")
                visited.append(sorted(str(k) + str(k_)))
    print()


# Displaying all adjacents vehicules to a certain input vehicule
def display_adj_vehicules(ID: int) -> None:
    print(f"All adjacents vehicules to car with ID {ID}: ", end="")
    for v, d in graph[ID]:
        print(v, end=" ")
    print()


# Moving a vehicule to a new position
def move_vehicule(ID: int, newCoords: list[int]) -> None:
    tmp = allCars[ID].coords
    allCars[ID].coords = newCoords
    print(f"Old coords: {tmp}")
    print(f"Updated coords: {allCars[ID].coords}")
    graph.update(generateGraph())


# Finding all reachables vehicules from a certain input vehicule (Depth-First Search)
def DFS(start: int) -> None:
    print(f"Reachable vehicules from car {start}: ", end="")
    reachables = []

    q = [start]
    visited = set()
    while q:
        curr = q.pop(0)
        visited.add(curr)
        for v, d in graph[curr][::-1]:
            if v not in visited:
                q.insert(0, v)
        if q and q[0] not in reachables:
            reachables.append(q[0])

    print(*reachables, "(DFS)")


# Finding all reachables vehicules from a certain input vehicule (Breadth-First Search)
def BFS(start: int) -> None:
    print(f"Reachable vehicules from car {start}: ", end="")
    reachables = []

    stck = [start]
    visited = set()
    while stck:
        curr = stck.pop()
        visited.add(curr)
        for v, d in graph[curr]:
            if v not in visited:
                if v not in reachables:
                    reachables.append(v)
                stck.append(v)

    print(*reachables, "(BFS)")


# Displaying all the edges of the Minimum Spanning Tree (MST) from a certain input vehicule
def MST() -> None:
    n = len(graph)
    mst_edges = []
    total_weight = 0
    included = [None] * n

    min_heap = [(0, 0, -1)]  # Min heap to efficiently find the min weight required
    # Also, we start can start from any vertex. I chose the vertex "0" in this case.

    # len(mst_edges) should be equal to n - 1 by the end
    while len(mst_edges) < n - 1 and min_heap:
        v, d, parent = heappop(min_heap)  # min weight and corresponding vertex

        if included[v]:
            continue
        included[v] = 1  # Now the current vertex has been included

        # Add the resulting edge
        if parent != -1:
            mst_edges.append((parent, v))
            total_weight += d

        for w, d_ in graph[v]:
            if not included[w]:
                heappush(min_heap, (w, d_, v))

    print("All the edges of the MST of the graph: ")
    print(*mst_edges)
    print(f"Total weight: {total_weight}")


# Shortest path between two vehicules, using a Dijkstra algorithm
def shortestPath(start: int, finish: int) -> None:
    inf = float("inf")
    ds = {v: inf for v in graph}
    ds[start] = 0
    src = {v: "" for v in graph}
    src[start] = start
    unvisited = set(graph.keys())

    while unvisited:
        curr = min(unvisited, key=lambda x: ds[x])
        unvisited.remove(curr)
        for v, d in graph[curr]:
            new_d = ds[curr] + d
            if ds[v] > new_d and d <= AutomotiveCar.connectivity_range:
                ds[v] = new_d
                src[v] = curr

    print(f"Shortest path between car {start} and car {finish} is: ", end="")

    def recursion(finish, path=[]):
        if finish == start:
            path.append(start)
            return path
        recursion(src[finish])
        path.append(finish)
        return path

    print(*recursion(finish), sep=" -> ")


# Execution
print("~.~.~.~.~.~.~.~.~.    Automotive Cars Menu   ~.~.~.~.~.~.~.~.~.~.")
print("1. Display all edges")
print("2. Display all adjacents vehicules to a vehicule")
print("3. Move vehicule")
print("4. Display reachable vehicules from a vehicule (DFS)")
print("5. Display reachable vehicules from a vehicule (BFS)")
print("6. Display edges of the Minimum Spanning Tree (MTS) between vehicules")
print("7. Display shortest path between two vehicules")
print("8. Quit")
print("~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.")
while True:
    check = input("Choose an operation to execute: ")
    if check == "1":
        display_all_edges()  # 1st operation
    elif check == "2":
        id = int(input("Enter vehicule ID: "))
        display_adj_vehicules(id)  # 2nd operation
    elif check == "3":
        id = int(input("Enter vehicule ID: "))
        n_coords = list(
            map(float, input("Enter the new coordinates of the vehicule: ").split())
        )
        move_vehicule(id, n_coords)  # 3rd operation
    elif check == "4":
        id = int(input("Enter vehicule ID: "))
        DFS(id)  # 4th operation
    elif check == "5":
        id = int(input("Enter vehicule ID: "))
        BFS(id)  # 5th operation
    elif check == "6":
        MST()  # 6th operation
    elif check == "7":
        id1 = int(input("Enter first vehicule ID: "))
        id2 = int(input("Enter second vehicule ID: "))
        shortestPath(id1, id2)  # 7th operation
    elif check == "8":
        print("~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.")
        break
    print("~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.")
