from rename_camera_files import rename_files

print('Enter the file path')
while True:
    input_string = input()
    if input_string == "":
        print('Input cannot be empty')
        continue
    else:
        break
print('Verbose or not? y/n')
while True:
    input_action = input()
    if input_action == "y":
        rename_files(input_string, verbose=True)
        break
    elif input_action == "n":
        rename_files(input_string, verbose=False)
        print('Successfully renamed.')
        break
    else:
        print('Wrong input')
        continue