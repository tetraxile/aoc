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

    with open(f"{CONFIG_DIR}/adventofcode/session") as f:
        session_token = f.read().rstrip()

    with open(f"{CONFIG_DIR}/adventofcode/last-request") as f:
        last_request_timestamp = int(f.read().rstrip())
        seconds_since_last_request = int(time.time()) - last_request_timestamp
        time_to_wait = 15*60 - seconds_since_last_request
        print("last request was at {}".format(datetime.fromtimestamp(last_request_timestamp)))
        if time_to_wait > 0:
            print(f"rate limit exceeded; wait {time_to_wait} seconds", file=sys.stderr)
            sys.exit(1)

    if len(sys.argv) != 3:
        print("expected 3 arguments, got {}".format(len(sys.argv)), file=sys.stderr)
        sys.exit(1)

    year, day = sys.argv[1:3]

    if year not in map(str, range(2015, 2024)):
        print(f"invalid year: {year}", file=sys.stderr)
        sys.exit(1)

    if day not in map(str, range(1, 26)):
        print(f"invalid day: {day}", file=sys.stderr)
        sys.exit(1)

    try:
        os.makedirs(f"{AOC_DIR}/{year}")
    except FileExistsError:
        print(f"directory {year} already exists, continuing")

    template_file = f"{AOC_DIR}/template.py"
    new_file = f"{AOC_DIR}/{year}/{day}.py"
    input_file = f"{AOC_DIR}/input/{year}-{day}"
    if os.path.isfile(new_file):
        print(f"{new_file} already exists, exiting", file=sys.stderr)
        sys.exit(1)
    
    shutil.copy2(template_file, new_file)

    if os.path.isfile(input_file):
        print(f"{input_file} already exists, exiting", file=sys.stderr)
        sys.exit(1)
    
    responded, puzzle_input = get_input(year, day, session_token)
    # responded, puzzle_input = False, "hi"

    with open(f"{AOC_DIR}/input/{year}-{day}", "w") as f:
        f.write(puzzle_input)
        print("received input ({} bytes)".format(len(puzzle_input)))
    
    f = open(f"{AOC_DIR}/example", "w")
    f.close()

    if (not responded):
        print("no response from server", file=sys.stderr)
        sys.exit(1)

    with open(f"{CONFIG_DIR}/adventofcode/last-request", "w") as f:
        request_timestamp = int(time.time())
        f.write(str(request_timestamp))
        print("request sent at {}".format(datetime.fromtimestamp(request_timestamp)))



if __name__ == "__main__":
    main()
