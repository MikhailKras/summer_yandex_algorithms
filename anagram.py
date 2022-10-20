def check_anagram(word1, word2):
    if len(word1) != len(word2):
        return 'NO'

    dict_one = dict()
    dict_two = dict()
    for s1, s2 in zip(word1, word2):
        dict_one[s1] = dict_one.get(s1, 0) + 1
        dict_two[s2] = dict_two.get(s2, 0) + 1

    if dict_one == dict_two:
        return 'YES'
    return 'NO'
    pass


if __name__ == '__main__':
    word1_ = input()
    word2_ = input()
    print(check_anagram(word1_, word2_))
