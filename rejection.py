def get_right_materials(first_type, materials):
    vowel_set = {'a', 'e', 'i', 'o', 'u'}

    def mat_replace(word):
        univ_word = list(word)
        for j in range(len(word)):
            if word[j].lower() in vowel_set:
                univ_word[j] = '#'
        return ''.join(univ_word).lower()

    first_type_set = set(first_type)
    ans = []

    dict_two = dict()
    for mat in first_type:
        mat_key = mat.lower()
        if not dict_two.get(mat_key):
            dict_two[mat_key] = mat

    dict_three = dict()
    for mat in first_type:
        mat_key = mat_replace(mat)
        if not dict_three.get(mat_key):
            dict_three[mat_key] = mat

    for mat in materials:
        if mat in first_type_set:
            ans.append(mat)
        elif mat.lower() in dict_two:
            ans.append(dict_two[mat.lower()])
        elif mat_replace(mat) in dict_three:
            ans.append(dict_three[mat_replace(mat)])
        else:
            ans.append('')
    return ' '.join(ans)


if __name__ == '__main__':
    n1 = input()
    first_type1 = input().split()
    n2 = input()
    materials1 = input().split()
    print(get_right_materials(first_type1, materials1))
