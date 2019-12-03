from typing import List, Tuple
import math

def calculate_wire_coordinates(instructions: List[str]):
    wires_coordinates = set()
    current_position = (0, 0)

    for instruction in instructions:
        direction = instruction[0]
        instruction = int(instruction[1:])
        if direction == 'R':
            for i in range(instruction):
                coordinate = (current_position[0] + 1, current_position[1])
                wires_coordinates.add(coordinate)
                current_position = coordinate
        elif direction == 'L':
            for i in range(instruction):
                coordinate = (current_position[0] - 1, current_position[1])
                wires_coordinates.add(coordinate)
                current_position = coordinate
        elif direction == 'U':
            for i in range(instruction):
                coordinate = (current_position[0], current_position[1] + 1)
                wires_coordinates.add(coordinate)
                current_position = coordinate
        elif direction == 'D':
            for i in range(instruction):
                coordinate = (current_position[0], current_position[1] - 1)
                wires_coordinates.add(coordinate)
                current_position = coordinate

    return wires_coordinates

def wires_cross_locations(wires_coordinates):
    return set(wires_coordinates[0]).intersection(*wires_coordinates)


def manhattan_distance(starting_coordinate, coordinates):
    closest_distance = math.inf

    for coordinate in coordinates:
        distance = int(abs(starting_coordinate[0] - coordinate[0]) + abs(starting_coordinate[1] - coordinate[1]))
        if distance < closest_distance:
            closest_distance = distance
    
    return closest_distance


if __name__ == "__main__":
    wires_coordinates = []
    for wire in open('day3/input.txt', 'r'):
        wire = wire.strip().split(',')
        wires_coordinates.append(calculate_wire_coordinates(wire))

    cross_locations = wires_cross_locations(wires_coordinates)
    
    print(manhattan_distance((0, 0), cross_locations))
