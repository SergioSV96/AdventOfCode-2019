from typing import List


def restore_gravity(intcode: List[int]):
    intcode[1] = 12
    intcode[2] = 2

    return intcode


def intcode_computer(intcode: List[int]):
    return intcode_computer_recursive(intcode, 0)


def intcode_computer_recursive(intcode: List[int], start_position: int):
    value_1_position = intcode[start_position + 1]
    value_2_position = intcode[start_position + 2]
    store_position = intcode[start_position + 3]

    if intcode[start_position] == 1:
        intcode[store_position] = intcode[value_1_position] \
            + intcode[value_2_position]
    elif intcode[start_position] == 2:
        intcode[store_position] = intcode[value_1_position] \
            * intcode[value_2_position]
    else:
        return intcode

    if len(intcode) >= (start_position + 4):
        return intcode_computer_recursive(intcode, start_position + 4)
    else:
        return intcode


if __name__ == "__main__":
    intcode_raw = open('day2/input.txt', 'r').readlines()[0]
    intcode = intcode_raw.split(',')
    intcode = list(map(int, intcode))

    intcode = restore_gravity(intcode)
    intcode = intcode_computer(intcode)

    print(intcode[0])
