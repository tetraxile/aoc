from itertools import permutations

def part_1(data: str) -> str:
    routes = {}
    stops = set()
    for line in data.split("\n"):
        tmp, distance = line.split(" = ")
        distance = int(distance)
        src, dst = tmp.split(" to ")
        if src not in routes:
            routes[src] = {}
        if dst not in routes:
            routes[dst] = {}
        routes[src][dst] = distance
        routes[dst][src] = distance
        
        stops.add(src)
        stops.add(dst)

    shortest = float("inf")
    for perm in permutations(stops):
        prev_stop = perm[0]
        total_dist = 0
        for stop in perm[1:]:
            total_dist += routes[prev_stop][stop]
            prev_stop = stop
        shortest = min(shortest, total_dist)

    return shortest



def part_2(data: str) -> str:
    routes = {}
    stops = set()
    for line in data.split("\n"):
        tmp, distance = line.split(" = ")
        distance = int(distance)
        src, dst = tmp.split(" to ")
        if src not in routes:
            routes[src] = {}
        if dst not in routes:
            routes[dst] = {}
        routes[src][dst] = distance
        routes[dst][src] = distance
        
        stops.add(src)
        stops.add(dst)

    longest = 0
    for perm in permutations(stops):
        prev_stop = perm[0]
        total_dist = 0
        for stop in perm[1:]:
            total_dist += routes[prev_stop][stop]
            prev_stop = stop
        longest = max(longest, total_dist)

    return longest
