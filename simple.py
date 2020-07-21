# Practice
PRINT_OSCAR = 0b01
HALT = 0b10  # 2
PRINT_NUM = 0b11  # opcode 3
SAVE = 0b100  # opcode 4
PRINT_REG = 0b101  # opcode 5
ADD = 0b110  # opcode 6

# save the number 99 into R2
# print

memory = [
    PRINT_OSCAR,
    PRINT_OSCAR,
    PRINT_OSCAR,
    PRINT_NUM,
    42,
    SAVE,
    2,
    99,
    SAVE,
    3,
    1,
    ADD,
    HALT,
]

# Registers

registers = [0] * 8

# program count
pc = 0

running = True

while(running):
    command = memory[pc]

    if command == PRINT_OSCAR:
        print('Hello Oscar')

    if command == PRINT_NUM:
        num_to_print = memory[pc + 1]

    if command == HALT:
        running = False
        print('Break')

    if command == SAVE:
        reg = memory[pc + 1]
        num_to_save = memory[pc + 2]
        registers[reg] = num_to_save

        pc += 2

    if command == PRINT_REG:
        reg_index =


    pc += 1
