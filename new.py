import argparse
from datetime import datetime
import os
import requests
import shutil
import sys
import time


def get_input(year: str, day: str, session_token: str) -> (bool, str):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {"Cookie": f"session={session_token}"}
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        return True, r.text
    else:
        print(f"error! {r.status_code}: {r.reason}\n{r.content}", file=sys.stderr)
        sys.exit(1)


def main():
    AOC_DIR = "/home/tetra/dev/aoc"
    CONFIG_DIR = "/home/tetra/.config"

    parser = argparse.ArgumentParser()
    parser.add_argument("year", choices=list(map(str, range(2015, 2024))))
    parser.add_argument("day", choices=list(map(str, range(1, 26))))

    args = parser.parse_args()

    with open(f"{CONFIG_DIR}/adventofcode/session") as f:
        session_token = f.read().rstrip()

    try:
        os.makedirs(f"{AOC_DIR}/{args.year}")
    except FileExistsError:
        print(f"directory {args.year} already exists, continuing")

    template_file = f"{AOC_DIR}/template.py"
    new_file      = f"{AOC_DIR}/{args.year}/{args.day}.py"
    input_file    = f"{AOC_DIR}/input/{args.year}-{args.day}"
    example_file  = f"{AOC_DIR}/example"

    if os.path.isfile(new_file):
        print(f"{new_file} already exists, exiting", file=sys.stderr)
        sys.exit(1)
    
    shutil.copy2(template_file, new_file)

    if os.path.isfile(input_file):
        print(f"{input_file} already exists, exiting", file=sys.stderr)
        sys.exit(1)
    
    with open(f"{CONFIG_DIR}/adventofcode/last-request") as f:
        last_request_timestamp = int(f.read().rstrip())
        seconds_since_last_request = int(time.time()) - last_request_timestamp
        time_to_wait = 15*60 - seconds_since_last_request
        print("last request was at {}".format(datetime.fromtimestamp(last_request_timestamp)))
        if time_to_wait > 0:
            print(f"rate limit exceeded; wait {time_to_wait} seconds", file=sys.stderr)
            sys.exit(1)
    
    responded, puzzle_input = get_input(year, day, session_token)
    # responded, puzzle_input = False, "hi"

    with open(input_file, "w") as f:
        f.write(puzzle_input)
        print("received input ({} bytes)".format(len(puzzle_input)))
    
    open(example_file, "w").close()

    if (not responded):
        print("no response from server", file=sys.stderr)
        sys.exit(1)

    with open(f"{CONFIG_DIR}/adventofcode/last-request", "w") as f:
        request_timestamp = int(time.time())
        f.write(str(request_timestamp))
        print("request sent at {}".format(datetime.fromtimestamp(request_timestamp)))


if __name__ == "__main__":
    main()
