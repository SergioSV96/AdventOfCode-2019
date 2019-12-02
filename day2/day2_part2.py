from typing import List


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


def gravity_assist(max: int, intcode: List[int]):
    for i in range(max):
        for j in range(max):
            noun = i + 1
            verb = j + 1

            if try_noun_verb(intcode.copy(), noun, verb) == 19690720:
                return noun, verb


def try_noun_verb(intcode: List[int], noun: int, verb: int):
    intcode[1] = noun
    intcode[2] = verb

    return(intcode_computer(intcode)[0])


if __name__ == "__main__":
    intcode_raw = open('day2/input.txt', 'r').readlines()[0]
    intcode = intcode_raw.split(',')
    intcode = list(map(int, intcode))

    noun, verb = gravity_assist(99, intcode)

    print(100 * noun + verb)
