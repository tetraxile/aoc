class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self._size = size
    
    def size(self):
        return self._size
    
    def print(self, indent):
        print("  "*indent + "-", self.name, f"(file, size={self._size})")


class Dir:
    def __init__(self, name: str, parent: "Dir" = None):
        self.name: str = name
        self.parent: "Dir" = parent
        self.entries: list[File | "Dir"] = []
    
    def __getitem__(self, name: str):
        # print(name)
        for child in self.entries:
            if child.name == name:
                return child
        
        raise ValueError("child not found")
    
    def size(self):
        return sum(child.size() for child in self.entries)
    
    def get_dirs(self):
        dirs = []
        for child in self.entries:
            if isinstance(child, Dir):
                dirs.append(child)
                dirs.extend(child.get_dirs())
        
        return dirs
    
    def print(self, indent=0):
        print("  "*indent + "-", self.name, f"(dir, size={self.size()})")
        for child in self.entries:
            child.print(indent=indent+1)
    
    def under_100k(self):
        total = 0
        if (size := self.size()) < 100000:
            total += size
        for child in self.entries:
            if isinstance(child, Dir):
                total += child.under_100k()

        return total
                
    
def parse(l: list[str]):
    root = Dir("/")
    cur = None

    i = 0
    while i < len(l):
        line = l[i]
        
        command = line.strip().removeprefix("$ ").split()
        if command[0] == "cd":
            dir = command[1]
            if dir == "/":
                cur = root
            elif dir == "..":
                cur = cur.parent
            else:
                cur = cur[dir]
        
        elif command[0] == "ls":
            while i < len(l) - 1:
                i += 1
                entry = l[i].strip().split()
                if entry[0].startswith("$"):
                    i -= 1
                    break

                if entry[0] == "dir":
                    cur.entries.append(Dir(entry[1], cur))
                else:
                    cur.entries.append(File(entry[1], int(entry[0])))
        
        i += 1
    
    return root


def part_2(root):
    required = root.size() - 40_000_000

    for dir in sorted(root.get_dirs(), key=lambda k: k.size()):
        size = dir.size()
        if size >= required:
            return size



with open("input") as f:
    l = f.read().strip().split("\n")
    root = parse(l)


print("part 1:", root.under_100k())
print("part 2:", part_2(root))
