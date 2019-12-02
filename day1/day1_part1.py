from math import floor

total_fuel = 0
for mass in open('day1/input.txt', 'r'):
    fuel = floor(int(mass) // 3) - 2
    total_fuel += fuel

print(total_fuel)