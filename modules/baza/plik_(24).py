# zadanie 1
# tylko dla angielskich znaków

chars = 256

def last(string, size):
    lastChar = [-1] * chars
    for i in range(size):
        lastChar[ord(string[i])] = i
    return lastChar


def boyerMoore(text, pattern):
    m = len(pattern)
    n = len(text)
    howMany = 0
    lastChar = last(pattern, m)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            howMany += 1
            s += (m - lastChar[ord(text[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - lastChar[ord(text[s + j])])
    return howMany


def main():
    text = input("Enter text: ").lower()
    patterntern = input("Enter what to find: ").lower()
    print("Pattern occurs in text " + str(boyerMoore(text, patterntern)) + " times.")


if __name__ == '__main__':
    main()