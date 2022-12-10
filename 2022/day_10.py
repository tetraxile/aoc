class CPU:
    CYCLES = {"addx": 2, "noop": 1}

    def __init__(self):
        self.code: list[tuple] = []
        self.reset()
    
    def reset(self):
        self.X = 1
        self.cycles = 0
        self.pc = 0
        self.total_signal_strength = 0
        self.state = [None, 0]
    
    def parse(self, filename: str):
        f = open(filename)
        for line in f.read().strip().split("\n"):
            inst = line.split()
            if inst[0] == "addx":
                inst[1] = int(inst[1])
            
            self.code.append(inst)
        
        f.close()

    def update_signal_strength(self):
        if (self.cycles + 20) % 40 == 0:
            signal_strength = self.cycles * self.X
            self.total_signal_strength += signal_strength
    
    def fetch(self) -> bool:
        if self.pc >= len(self.code):
            return False
        
        inst = self.code[self.pc]
        self.pc += 1
        self.state = [inst, CPU.CYCLES[inst[0]]]

        return True

    def execute(self):
        if self.state[1] == 0:
            inst = self.state[0]
            if inst[0] == "addx":
                self.X += inst[1]
            elif inst[0] == "noop":
                pass

    def tick(self) -> bool:
        r = True
        if not self.state[0] or self.state[1] == 0:
            r = self.fetch()
        
        self.cycles += 1
        self.state[1] -= 1
        return r

    def run(self, blank_char: str = " "):
        self.reset()
        crt = ""

        while self.tick():
            beam = (self.cycles - 1) % 40
            crt += (blank_char + "#")[abs(self.X - beam) < 2]            
            if beam == 39:
                crt += "\n"

            self.update_signal_strength()
            self.execute()
        
        print(f"total signal strength: {self.total_signal_strength}\n")
        print(crt)
    

def main():
    cpu = CPU()
    cpu.parse("input")
    cpu.run(blank_char=".")


if __name__ == "__main__":
    main()
