def part_1(data: str) -> str:
    steps = 2503

    furthest = 0
    for line in data.split("\n"):
        tmp, rest_time = line.removesuffix(" seconds.").split(" seconds, but then must rest for ")
        tmp, fly_time = tmp.split(" km/s for ")
        name, fly_speed = tmp.split(" can fly ")

        rest_time = int(rest_time)
        fly_time = int(fly_time)
        fly_speed = int(fly_speed)
        
        fly_distance = fly_time * fly_speed
        cycle_time = fly_time + rest_time

        full_cycles = steps // cycle_time
        last_cycle_length = steps - cycle_time * full_cycles

        total_distance = fly_distance * full_cycles + fly_speed * min(last_cycle_length, fly_time)

        furthest = max(furthest, total_distance)

    return furthest


def part_2(data: str) -> str:
    steps = 2503

    stats = {}
    for line in data.split("\n"):
        tmp, rest_time = line.removesuffix(" seconds.").split(" seconds, but then must rest for ")
        tmp, fly_time = tmp.split(" km/s for ")
        name, fly_speed = tmp.split(" can fly ")

        rest_time = int(rest_time)
        fly_time = int(fly_time)
        fly_speed = int(fly_speed)
    
        stats[name] = {
            "rest time": rest_time,
            "fly time": fly_time,
            "fly speed": fly_speed,
            "distance": 0,
            "points": 0
        }

    for i in range(steps):
        best = float("-inf")
        for name, reindeer in stats.items():
            cycle_step = i % (reindeer["rest time"] + reindeer["fly time"])
            if cycle_step < reindeer["fly time"]:
                reindeer["distance"] += reindeer["fly speed"]
        
            if reindeer["distance"] > best:
                best = reindeer["distance"]

        for name, reindeer in stats.items():
            if reindeer["distance"] == best:
                reindeer["points"] += 1

    return max(map(lambda k: k["points"], stats.values()))
