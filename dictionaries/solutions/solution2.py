def sort_grade():
    """ NoneType -> NoneType
    Read from classlist.txt, and print out the lines
    sorted based on the person's grade.
    """
    grade_values = {"F": 0, "F+": 1, "D-": 2, "D": 3,
                    "D+": 4, "C-": 5, "C": 6, "C+": 7,
                    "B-": 8, "B": 9, "B+": 10, "A-": 11,
                    "A": 12}

    class_entries = {}
    file = open("classlist.txt")
    for line in file:
        line = line.rstrip()
        (name, grade) = line.split(',')
        if grade not in class_entries:
            class_entries[grade] = []
        class_entries[grade].append(name)

    sorted_grades = sorted(class_entries.keys(), key=lambda x: grade_values[x])
    for grade in sorted_grades:
        for name in class_entries[grade]:
            print(name + "," + grade)

