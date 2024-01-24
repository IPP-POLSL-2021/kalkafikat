special_symbols = [" ", ",", ".", "\n", "\t", ";", ":"]


def fill_p(pattern):
    p = {"*": -1}

    for i, letter in enumerate(pattern):
        p[letter] = i

    return p


def boyer_moore(string: str, pattern: str):
    l = len(pattern) - 1
    p = fill_p(pattern)

    i = l
    j = 0

    count = 0
    while i < len(string):
        letter = string[i]
        match = True
        p_letter = "*"

        for current_index, pattern_letter in enumerate(reversed(pattern)):
            if pattern_letter == letter:
                j = l - current_index
                letter = string[i - current_index - 1]
                p_letter = pattern_letter

                if not match:
                    break
            else:
                match = False

        if match:
            if (string[i + 1] in special_symbols):
                count += 1

        i = i + l - min((j, 1 + p[p_letter]))

    print(" W zdaniu:'", string, "' słowo ", pattern,
          " wsytępuje dokładnie", count, "razy ")

    return count


boyer_moore("Pies goni kot, a kot ucieka przed innymi kotami", "kot")
