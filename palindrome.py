number = "Madam I'm  Adam"
transform_number = number.upper()
new_name = ''
for c in transform_number:
    if c != "'" and c != ' ':
        new_name += c
print(new_name)
print(new_name == new_name[::-1])

    

