def make_string(a_list):
    new_str = ''
    for i in a_list:
        new_str += i
    return new_str


def are_palindrome(string1, string2):
    # convert to lowercase,
    # make into a list,
    # remove spaces and reverse a list
    # then compare
    string1 = string1.lower()
    string2 = string2.lower()
    list1 = list(string1)
    list2 = list(string2)
    if ' ' in list2:
        list2.remove(' ')
    if ' ' in list1:
        list1.remove(' ')

    list2.reverse()
    if make_string(list1) == make_string(list2):
        return True
    else:
        return False


print(are_palindrome('rotor', 'rot or'))
print(are_palindrome('rotor', 'rotor'))
