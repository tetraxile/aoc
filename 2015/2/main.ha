use fmt;
use io;
use os;
use strconv;
use strings;

export fn main() void = {
	const handle = os::open("input")!;
	defer io::close(handle)!;
	const buf = io::drain(handle)!;
	defer free(buf);
	const sz = len(buf);
	const input = strings::fromutf8(buf)!;
	const input = strings::rtrim(input);
	const lines = strings::split(input, "\n");

	let total = 0;
	let total2 = 0;

	for (let i: size = 0; i < len(lines); i += 1) {
		const dimensions = strings::split(lines[i], "x");
		const length = strconv::stoi(dimensions[0])!;
		const width = strconv::stoi(dimensions[1])!;
		const height = strconv::stoi(dimensions[2])!;

		const face1 = length * width;
		const face2 = length * height;
		const face3 = width * height;

		let slack = face1;
		if (face2 < slack) slack = face2;
		if (face3 < slack) slack = face3;

		const area = 2 * (face1 + face2 + face3) + slack;
		total += area;

		const perim1 = 2 * (length + width);
		const perim2 = 2 * (length + height);
		const perim3 = 2 * (width + height);

		let ribbon = perim1;
		if (perim2 < ribbon) ribbon = perim2;
		if (perim3 < ribbon) ribbon = perim3;

		const volume = length * width * height;

		total2 += ribbon + volume;
	};

	fmt::printfln("part 1: {}", total)!;
	fmt::printfln("part 2: {}", total2)!;
};
