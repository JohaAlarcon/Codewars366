def accum(s):
    result = ""

    for i, char in enumerate(s):
        result += char.upper()

        result += char.lower() * i

        if i < len(s) -1:
            result += "-"
    return result
