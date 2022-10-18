def get_broke_palindrome(s):
    if len(s) == 1:
        return ''
    res = list(s)
    for i in range(len(s)):
        if s[i] != 'a':
            res[i] = 'a'
            break
        elif i == len(s) - 1:
            res[i] = 'b'
    if set(res) == {'a'}:
        return s[:-1] + 'b'

    return ''.join(res)


my_str = 'aaabaaa'
print(get_broke_palindrome(my_str))
