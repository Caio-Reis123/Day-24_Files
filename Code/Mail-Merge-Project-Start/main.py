new_letter = []
with open('Mail-Merge-Project-Start/Input/Names/invited_names.txt') as name_list:
    names = name_list.read().split()

    for name in names:

        with open('Mail-Merge-Project-Start/Input/Letters/starting_letter.txt', mode='r') as letters:
            content = letters.readlines()
        line = content[0].replace('[name]', name)
        new_letter.append(line)

        for a in content[1:]:
            new_letter.append(a)
        print(new_letter)

        with open(name +'_letter.txt', mode='w') as textfile:

            for element in new_letter:
                textfile.write(element)
        new_letter = []
