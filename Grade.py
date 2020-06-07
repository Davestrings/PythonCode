def write_file(file_name):
    count = 0
    # file_name = input("Enter file name with appropriate extension: ")
    while True:
        grade_fil = open(file_name, 'a')
        output_text = input("Enter text to file:")
        print(output_text, file=grade_fil)
        count += 1
        if count == 6:
            break


def weighted_grade(score_list, weight_tuple=(0.3, 0.3, 0.4)):
    """  Expects 3 elements in score_list. Multiplies each grade by its weight. Returns sum  """
    grade_float = (score_list[0] * weight_tuple[0]) + \
                  (score_list[1] * weight_tuple[1]) + \
                  (score_list[2] * weight_tuple[2])
    return grade_float


def parse_line(line_str):
    """Expects a line of form last, first, exam1, exam2, final.
    returns a  tuple containing first, + last and list of scores."""
    field_list = line_str.strip().split(', ')
    name_str = field_list[1] + ' ' + field_list[0]
    score_list = []
    for element in field_list[2:]:
        score_list.append(int(element))
    return name_str, score_list  # a tuple is returned


def main():
    file_name = input('open what file: ')
    try:
        grade_file = open(file_name, 'r')  # read file if it exist
        print("{:>13s}  {:>15s}".format('Name', 'Grade'))
        print('=' * 30)
        for line_str in grade_file:
            name_str, score_list = parse_line(line_str)
            grade_float = weighted_grade(score_list)
            print("{:>15s}  {:14.2f}".format(name_str, grade_float))
    except IOError:
        print("writing and creating file")
        write_file(file_name)
        grade_file = open(file_name, 'r')
        print("{:>13s}  {:>15s}".format('Name', 'Grade'))
        print('=' * 30)
        for line_str in grade_file:
            name_str, score_list = parse_line(line_str)
            grade_float = weighted_grade(score_list)
            print("{:>15s}  {:14.2f}".format(name_str, grade_float))


main()
