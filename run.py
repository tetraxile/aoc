import argparse
import importlib
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("year", choices=list(map(str, range(2015, 2024))))
    parser.add_argument("day", choices=list(map(str, range(1, 26))))
    parser.add_argument("-x", "--example", help="use example file", action="store_true")

    args = parser.parse_args()
    
    try:
        day_module = importlib.import_module(f"{args.year}.{args.day}")
    except ModuleNotFoundError:
        print("", file=sys.stderr)
        sys.exit(1)

    file_path = "example" if args.example else f"input/{args.year}-{args.day}"
    with open(file_path) as f:
        data = f.read().rstrip()

    print("part 1:", day_module.part_1(data))
    print("part 2:", day_module.part_2(data))

if __name__ == "__main__":
    main()
