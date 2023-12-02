from functools import reduce
from math import *
import operator
import sys


class Vec2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f"<{self.x}, {self.y}>"

    def tuple(self) -> tuple[int, int]:
        return (self.x, self.y)

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vec2(self.x * scalar, self.y * scalar)

    def mag(self) -> float:
        return math.sqrt(self.dot(self))

    def dot(self, other) -> int:
        return self.x * other.x + self.y * other.y


class Vec3:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def __repr__(self) -> str:
        return f"<{self.x}, {self.y}, {self.z}>"

    def tuple(self) -> tuple[int, int]:
        return (self.x, self.y, self.z)

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)

    def mag(self) -> float:
        return math.sqrt(self.dot(self))

    def dot(self, other) -> int:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vec3(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x
        )



def parse_fmt_string(fmt: str) -> list:
    tokens = []
    cur_token = ""
    inside_specifier = False
    i = 0
    while i < len(fmt):
        c = fmt[i]
        if c == "{":
            if i == len(fmt) - 1:
                raise ValueError(f"string ended before format specifier (index {i})")

            elif fmt[i+1] == "{":
                cur_token += "{"
                i += 1

            else:
                if inside_specifier:
                    raise ValueError("cannot nest specifiers")

                if len(cur_token):
                    tokens.append((False, cur_token))

                cur_token = ""
                inside_specifier = True

        elif c == "}":
            if inside_specifier or i == len(fmt) - 1:
                tokens.append((True, cur_token))
                cur_token = ""
                inside_specifier = False

            elif fmt[i+1] == "}":
                cur_token += "}"
                i += 1

            else:
                raise ValueError("invalid position for closing brace")

        else:
            cur_token += c
            if i == len(fmt) - 1:
                if inside_specifier:
                    raise ValueError("specifier must end")

                tokens.append((False, cur_token))
       
        i += 1

    return tokens


def parse_string(tokens: list[tuple[bool, str]], string: str) -> list[str | int]:
    string_idx = 0
    token_start = 0
    parts = {}
    string += "\x00"

    for is_specifier, token in tokens:
        token_start = string_idx
        if is_specifier:
            part_name, token_type = token.split(":")
            if token_type == "i" or token_type == "int":
                if string[string_idx] == "-":
                    string_idx += 1

                while string[string_idx].isnumeric():
                    string_idx += 1

                if token_start == string_idx:
                    preview = string[token_start:token_start+10]
                    raise ValueError(f"no int found in string: {preview!r}")

                parts[part_name] = int(string[token_start:string_idx])

            elif token_type == "a" or token_type == "alpha":
                while string[string_idx].isalpha():
                    string_idx += 1

                if token_start == string_idx:
                    preview = string[token_start:token_start+10]
                    raise ValueError(f"no alpha found in string: {preview!r}")

                parts[part_name] = string[token_start:string_idx]

            elif token_type == "l" or token_type == "alnum":
                while string[string_idx].isalnum():
                    string_idx += 1

                if token_start == string_idx:
                    preview = string[token_start:token_start+10]
                    raise ValueError(f"no alnum found in string: {preview!r}")

                parts[part_name] = string[token_start:string_idx]

            else:
                raise ValueError(f"unimplemented specifier `{token_type}`")

        else:
            token_end = token_start + len(token)
            if token_end > len(string):
                raise ValueError("input string is too short to match format string")

            test_token = string[token_start:token_end]
            if token != test_token:
                raise ValueError(f"input string does not match format:\n\t{token!r}\n\t{test_token!r}")
                sys.exit(1)

            string_idx += len(token)

    if string_idx != len(string) - 1:
        raise ValueError("didn't parse entire input string")

    return parts


def product(it) -> int | float:
    return reduce(operator.mul, it, 1)
