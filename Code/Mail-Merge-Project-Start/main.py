PLACEHOLDER = '[name]'

# CREATE LETTER LIST
new_letter = []

# OPEN 'INVITED_NAMES' FILE AND SPLIT IT
with open('./Mail-Merge-Project-Start/Input/Names/invited_names.txt') as name_list:
    names = name_list.read().split()

# LOOP THROUGH NAMES, OPEN 'STARTING_LETTER' FILE
    for name in names:
        with open('./Mail-Merge-Project-Start/Input/Letters/starting_letter.txt', mode='r') as letters:
            content = letters.readlines()

# SEPARATE 1ST LINE AND REPLACE THE NAMES, THEN APPEND IT TO NEW_LETTER      
        line = content[0].replace(PLACEHOLDER, name)
        new_letter.append(line)

# APPEND THE REMANING LINES OF LETTER TO NEW_LETTER
        for i in content[1:]:
            new_letter.append(i)

# CREATE A NEW FILE FOR EACH NAME AND RESET NEW_LETTER 
        with open(name +'_letter.txt', mode='w') as textfile:
            for element in new_letter:
                textfile.write(element)
        new_letter = []



