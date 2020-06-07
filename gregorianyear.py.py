def isleapyear(year):
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def display_message(truthy_checker):
    if truthy_checker:
        print(truthy_checker, "{} is a Gregorian leap year".format(year))
    else:
        print(truthy_checker, "{} is not a Gregorian leap year".format(year))


year = input("Enter a year: ")
is_true = isleapyear(int(year))
display_message(is_true)