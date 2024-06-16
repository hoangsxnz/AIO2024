def word_count(file_path):
    reader = open(file_path, 'r')
    content = reader.read().strip()
    lst_words = [word.lower() for word in content.split()]

    freq = dict()
    for word in lst_words:
        freq[word] = freq.get(word, 0) + 1

    sorted_freq = dict(sorted(freq.items()))
    print(sorted_freq)


word_count('Module1\Week2\P1_data.txt')
