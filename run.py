def replace_character(input_string, c1, c2):
    # TODO: Replace all occurrences of character `c1` in `input_string` with `c2`
    result = []
    for char in input_string:
        if char == c1:
            result.append(c2)
        else:
            result.append(char)
    return ''.join(result)

print(replace_character("hello, world", "o", "a"))  # Output: "hella, warld"
