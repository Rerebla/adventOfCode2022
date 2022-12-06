import re
import copy


def extractDirections(direction: str):
    _, quantity, _, origin, _, destination = direction.split(" ")
    return int(quantity), int(origin), int(destination)


def printSolution(cargo: list[list[str]], part: str):
    solutionString = ""
    for container in cargo:
        solutionString += container[-1]
    print(f"Part {part}: The solution is: {solutionString}")


with open('input.txt') as f:
    lines = f.readlines()
    grid = lines[:8]
    cargo: list[list[str]] = [[] for i in range(9)]

    for i, line in enumerate(reversed(grid)):
        for i, match in enumerate(re.findall("\[(.*?)\]", line)):
            if match != "":
                cargo[i].append(match)

    # Part 1
    cargoPart1 = copy.deepcopy(cargo)
    directions = [line.strip() for line in lines[10:]]
    for direction in directions:
        quantity, origin, destination = extractDirections(direction)
        for i in range(0, quantity):
            cargoPart1[destination-1].append(cargoPart1[origin-1][-1])
            del cargoPart1[origin-1][-1]

    # Part 2
    cargoPart2 = copy.deepcopy(cargo)
    for direction in directions:
        quantity, origin, destination = extractDirections(direction)
        cargoPart2[destination-1].extend(cargoPart2[origin-1][-quantity:])
        del cargoPart2[origin-1][-quantity:]

    printSolution(cargo=cargoPart1, part=1)
    printSolution(cargo=cargoPart2, part=2)
