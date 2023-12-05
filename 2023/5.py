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
    seeds = ints(sections[0].split(":")[1])
    seeds = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
    
    # good luck having enough ram + patience to do this
    seeds = [seed for pair in seeds for seed in range(pair[0], sum(pair))]

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
