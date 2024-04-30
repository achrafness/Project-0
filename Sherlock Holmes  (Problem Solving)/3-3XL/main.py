# output : j 4567
def transform_condition (a,b,condition):
    if condition == "<":
        return a < b
    elif condition == "<=":
        return a <= b
    elif condition == ">":
        return a > b
    elif condition == ">=":
        return a >= b
    elif condition == "==":
        return a == b
    elif condition == "!=":
        return a != b
    else:
        return False

def transform_instruction(instruction):
    parts = instruction.split()
    register = parts[0]
    operation = 1 if parts[1] == "inc" else -1
    value = int(parts[2])
    condition_register = parts[4]
    condition_operator = parts[5]
    condition_value = int(parts[6])
    return (register, operation, value, condition_register, condition_operator, condition_value)

def open_file(file_name):
    file_instructions = []
    with open("input.txt", "r") as file:
        for line in file:
            file_instructions.append(line.strip())
    return file_instructions

def main():
    file_instructions = open_file("input.txt")
    modified_instructions = []
    for file_instruction in file_instructions:
        modified_instructions.append(transform_instruction(file_instruction))

    registers = {}

    for modified_instruction in modified_instructions:
        register, operation, value, condition_register, condition_operator, condition_value = modified_instruction
        if register not in registers:
            registers[register] = 0

    for modified_instruction in modified_instructions:
        register, operation, value, condition_register, condition_operator, condition_value = modified_instruction
        if transform_condition(registers[condition_register], condition_value, condition_operator):
            registers[register] += operation * value

    max_name = None
    max_value = None
    for register, value in registers.items():
        if max_value is None or value > max_value:
            max_name = register
            max_value = value
    print(max_name, max_value)

if __name__ == "__main__":
    main()