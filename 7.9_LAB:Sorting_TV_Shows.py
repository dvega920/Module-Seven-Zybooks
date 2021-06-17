file_name = 'file1.txt' # hardcoded value as to not have to keep typing in user_input.
# TODO Need to FIX code to pass all unit test in zybooks. Errors about removing preceding zeros and spacing and newline


# opens the file and copies the contents to a variable called 'contents'
with open(file_name, 'r') as filename:
    contents = filename.readlines()
# print(contents)

# empty dictionary to store the seasons as keys and the show titles as values
my_dict = {}

# loop to iterate through the contents of the file that was stored in variable contents.
# loop then assigns show season to variable key and show titles to variable value
# IF statement is to check for multiple shows that utilize the same key (e.g. - ShowA and ShowB both have 20 seasons so show A and B should be concatenated and separated values by a semi-colon in the shared key. (e.g. - 20: ShowA ; ShowB)
#ElSE the single value is just set to the key.
for counter in range(0, len(contents), 2):
    key = contents[counter].strip('\n')
    value = contents[counter + 1].strip('\n')

    if key in my_dict.keys():
        my_dict[key] = my_dict[key] + '; ' + value
    else:
        my_dict[key] = value

# print(contents)

# Below opens the output_keys.txt file in write mode. If it doesn't exist it will create the file.
# Then iterates through the dictionary that was created and filled with key values. The dictionary is sorted here and
# output to the created output_keys.txt file
with open('output_keys.txt', 'w') as output1:
    for key in sorted(my_dict):
        output1.write('{}: {}\n'.format(key, my_dict[key]))
        # print('{}:'.format(my_dict[key]))

# Below opens the output_titles.txt file in write mode. If it doesn't exist it will create the file.
# Then iterates through dictionary values ONLY and extracts the titles and outputs them to output_titles.txt file.
with open('output_titles.txt', 'w') as output2:
    for val in sorted(my_dict.values()):
        # print(val)
        if ';' in val.strip():
            # split_val = ''
            split_val = val.strip().split(';')
            for value in split_val:
                output2.write('{}\n'.format(value).strip() + '\n')
        else:
            output2.write('{}\n'.format(val))
