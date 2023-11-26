def part_1(data: str) -> str:
    total = 0
    for code_chars in data.split("\n"):
        cursor = 0
        memory_chars = ""
        while cursor < len(code_chars):
            char = code_chars[cursor]
            cursor += 1

            if char == '\\':
                char = code_chars[cursor]
                cursor += 1

                if char in ('\\', '"'):
                    memory_chars += char
                elif char == 'x':
                    memory_chars += chr(int(code_chars[cursor:cursor+2], 16))
                    cursor += 2
            elif char != '"':
                memory_chars += char

        total += len(code_chars) - len(memory_chars)

    return total


def part_2(data: str) -> str:
    total = 0
    for code_chars in data.split("\n"):
        cursor = 0
        encoded_chars = "\""
        while cursor < len(code_chars):
            char = code_chars[cursor]
            cursor += 1
            
            if char == '"':
                encoded_chars += "\\\""
            elif char == '\\':
                encoded_chars += "\\\\"
            else:
                encoded_chars += char

        encoded_chars += "\""

        total += len(encoded_chars) - len(code_chars)

    return total
