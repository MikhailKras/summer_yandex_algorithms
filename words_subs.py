def get_short_text(dct, words):
    for i, word in enumerate(words):
        short_word = ''
        for let in word:
            short_word += let
            if short_word in dct:
                words[i] = short_word
                break
    print(' '.join(words))


if __name__ == '__main__':
    dct1 = set(input().split())
    words1 = input().split()
    get_short_text(dct1, words1)
