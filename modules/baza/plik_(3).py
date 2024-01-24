def bayer_moore(text: str, key: str) -> int:
    text = text.lower()
    key = key.lower()

    tab = {letter: index for index, letter in enumerate(key)}

    key_len = len(key)
    i = key_len - 1
    j = key_len - 1

    count = 0

    while i < len(text):
        while text[i] == key[j]:
            i -= 1
            j -= 1

        punctuation = [".", ",", "!", "?", " "] # possibly more

        has_leading_whitespace = i >= 0 and text[i] == " "
        has_trailing_whitespace = i + key_len + 1 < len(text) and (text[i+key_len+1] == " " or text[i+key_len+1] in punctuation)
        is_first_word = i == -1
        is_last_word = i + key_len + 1 >= len(text)
        if j == -1 and (has_leading_whitespace or is_first_word) and (has_trailing_whitespace or is_last_word):
            count += 1
            i += key_len - min(j, 1 + tab.get(text[i], -1))
            j = key_len - 1
        else:
            i += key_len - min(j, 1 + tab.get(text[i], -1))
            j = key_len - 1

    return count

# test class to use with pytest
class TestBayerMoore:
    def test_1(self):
        text = "Pies goni kota, a kot ucieka"
        key = "kot"
        count = bayer_moore(text, key)
        assert count == 1

    def test_2(self):
        text = "Pies goni kota, a ten kot ma na imię akot"
        key = "kot"
        count = bayer_moore(text, key)
        assert count == 1

    def test_3(self):
        text = "Duży kot to kot, mały kot to kot, wszystkie koty to koty, a psy to akoty."
        key = "kot"
        count = bayer_moore(text, key)
        assert count == 4

    def test_4(self):
        text = "Mam w domu 2 koty. Pierwsza (starsza) to Flora, a druga (młodsza) to Mrówcia."
        key = "kot"
        count = bayer_moore(text, key)
        assert count == 0

    def test_5(self):
        text = "KOT – KOCHAM CIĘ KOTAŚNY"
        key = "kot"
        count = bayer_moore(text, key)
        assert count == 1


if __name__ == "__main__":
    text = input("Podaj tekst do przeszukania: ")
    key = input("Podaj szukany wzorzec: ")
    print(f'Liczba znalezionych wystąpień: {bayer_moore(text, key)}')
