from math import floor


def calculate_fuel(mass: int):
    fuel = floor(int(mass) // 3) - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + calculate_fuel(fuel)


if __name__ == '__main__':
    total_fuel = 0
    for mass in open('day1/input.txt', 'r'):
        total_fuel += calculate_fuel(int(mass))

    print(total_fuel)
