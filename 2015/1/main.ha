use fmt;
use io;
use os;
use strings;

export fn main() void = {
	const handle = os::open("input")!;
	defer io::close(handle)!;
	const buf = io::drain(handle)!;
	defer free(buf);
	const sz = len(buf);

	let floor: int = 0, part2_pos: size = -1;

	for (let i: size = 0; i < sz; i += 1) {
		let char = buf[i]: rune;

		if (char == '(') {
			floor += 1;
		} else if (char == ')') {
			floor -= 1;
		};

		if (floor < 0 && part2_pos == -1) {
			part2_pos = i + 1;
		};
	};


	fmt::printfln("part 1: {}", floor)!;
	fmt::printfln("part 2: {}", part2_pos)!;
};
