file_name = 'file1.txt'

with open(file_name, 'r') as filename:
    contents = filename.readlines()
# print(contents)

my_dict = {}

for counter in range(0, len(contents), 2):
    key = contents[counter].strip('\n')
    value = contents[counter + 1].strip('\n')

    if key in my_dict.keys():
        my_dict[key] = my_dict[key] + '; ' + value
    else:
        my_dict[key] = value

# print(contents)


with open('output_keys.txt', 'w') as output1:
    for key in sorted(my_dict):
        output1.write('{}: {}\n'.format(key, my_dict[key]))
        # print('{}:'.format(my_dict[key]))


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
