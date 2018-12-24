def sort_last_name():
    """ NoneType -> NoneType
    Read from classlist.txt, and print out the lines
    sorted based on the person's last name.
    """
    class_entries = {}
    file = open("classlist.txt")
    for line in file:
        line = line.rstrip()
        (name, grade) = line.split(',')
        class_entries[name] = grade

    sorted_names = sorted(class_entries.keys(), key=lambda x: x.split()[-1])
    for name in sorted_names:
        print(name + "," + class_entries[name])

