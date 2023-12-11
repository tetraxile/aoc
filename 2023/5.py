from util import *


def part_1(data: str) -> str:
    sections = data.split("\n\n")
    seeds = ints(sections[0].split(":")[1])

    for section in sections[1:]:
        lines = section.split("\n")
        src_name, _, dst_name = lines[0].removesuffix(" map:").split("-")
        lines = list(map(ints, lines[1:]))

        for i, seed in enumerate(seeds):
            for dst_start, src_start, length in lines:
                if src_start <= seed < src_start + length:
                    seeds[i] = dst_start + (seed - src_start)
                    break

    return min(seeds)



def part_2(data: str) -> str:
    sections = data.split("\n\n")
    tmp = ints(sections[0].split(":")[1])
    ranges = [range(pair[0], sum(pair)) for pair in chunks(tmp, 2)]

    for j, section in enumerate(sections[1:]):
        lines = section.split("\n")
        src_name, _, dst_name = lines[0].removesuffix(" map:").split("-")
        lines = [(range(src_start, src_start+length), range(dst_start, dst_start+length)) for dst_start, src_start, length in sorted(map(ints, lines[1:]), key=lambda k: k[1])]

        new_ranges = []
        for i, rng in enumerate(ranges):
            entered_src_range = None
            left_src_range = False

            for src_range, dst_range in lines:
                difference = dst_range.start - src_range.start

                if rng.start in src_range:
                    entered_src_range = rng.start
                if (rng.stop - 1) in src_range or src_range.start >= rng.stop:
                    left_src_range = True

                if entered_src_range is None:
                    continue

                if left_src_range:
                    entered_src_range = max(entered_src_range, src_range.start)
                    new_ranges.append(range(entered_src_range + difference, rng.stop + difference))
                    break
                else:
                    new_ranges.append(range(max(rng.start + difference, dst_range.start), min(rng.stop + difference, dst_range.stop)))

            if entered_src_range is None:
                new_ranges.append(rng)
            elif not left_src_range:
                new_ranges.append(range(src_range.stop, rng.stop))

        ranges = new_ranges

    min_location = float("inf")
    for rng in ranges:
        min_location = min(rng.start, min_location)

    return min_location
