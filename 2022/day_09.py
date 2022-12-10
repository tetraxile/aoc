from dataclasses import dataclass

@dataclass
class Vector2:
    x: int
    y: int

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __abs__(self):
        return Vector2(abs(self.x), abs(self.y))
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"<{self.x}, {self.y}>"

    def length(self): # manhattan distance
        return abs(self.x) + abs(self.y)

    def tuple(self):
        return (self.x, self.y)


def tail_positions(n: int):
    movements = {"U": Vector2(0, -1), "D": Vector2(0, 1), "L": Vector2(-1, 0), "R": Vector2(1, 0)}
    knots = [Vector2(0, 0) for _ in range(n)]
    unique = set()

    for direction, distance in instructions:
        for _ in range(distance):
            knots[0] += movements[direction]
            for i in range(1, len(knots)):

                pull = knots[i-1] - knots[i]
                if pull.length() > 1 and not abs(pull) == Vector2(1, 1):
                    if pull.x > 0:
                        knots[i].x += 1
                    elif pull.x < 0:
                        knots[i].x -= 1
                    if pull.y > 0:
                        knots[i].y += 1
                    elif pull.y < 0:
                        knots[i].y -= 1
        
            unique.add(knots[-1].tuple())
            
    return len(unique)


with open("input") as f:
    l = f.read().strip().split("\n")
    instructions = [((s := line.strip().split())[0], int(s[1])) for line in l]

print("part 1:", tail_positions(2))
print("part 2:", tail_positions(10))
