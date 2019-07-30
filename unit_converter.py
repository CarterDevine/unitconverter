# converts unit from one unit to another
# user input an integer

# FT TO M

u = [0.01, 0.1, 100, 1000, 10000, 3.281]


def converter(n):
    newunit = n * u[5]
    return newunit


unit = int(input())
retValue = converter(unit)

print(retValue)
