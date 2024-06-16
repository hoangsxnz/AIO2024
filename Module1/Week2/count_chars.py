def count_chars(s: str):
    freq = dict()
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    sorted_freq = dict(sorted(freq.items()))
    print(sorted_freq)


if __name__ == "__main__":
    string = 'Happiness'
    count_chars(string)
