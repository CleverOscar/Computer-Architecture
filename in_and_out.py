import sys

print(sys.argv)

if len(sys.argv) < 2:
    print('Please pass in a second file name')
    sys.exit()

file_name = sys.argv[1]

try:
    with open(file_name) as file:
        for line in file:
            split_line = line.split('#')[0]
            command = split_line.strip()

            if command == '':
                continue

            num = int(command)
            print(f'{num: 8b} is {num}')


except FileNotFoundError:
    print(f'{sys.argv[0]}: {sys.argv[1]} file was not found')
    sys.exit()

# with open("print8.ls8") as file
#   for line in file:
#       print(line)
