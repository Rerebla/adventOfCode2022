import typing


def convertItemToPriority(item: str):
    if item.isupper():
        return int(ord(item[0])) - 38
    else:
        return int(ord(item[0]) - 96)


with open('input.txt') as f:
    # Part 1
    lines = f.readlines()
    score = 0
    for line in lines:
        firstCompartment, secondCompartment = line.strip(
        )[:len(line)//2], line.strip()[len(line)//2:]
        for character in firstCompartment:
            if character in secondCompartment:
                if character[0].isupper():
                    score += convertItemToPriority(character[0])
                    break
                else:
                    score += convertItemToPriority(character[0])
                    break
    print("Part 1: Priority Score is :", score)

with open('input.txt') as f:
    # Part 2
    counter = 0
    rucksacksTopList: typing.List[typing.List[str]] = []
    lines = f.readlines()
    elveGroup: typing.List[str] = []
    score = 0
    for line in lines:
        elveGroup.append(line.strip())
        if len(elveGroup) == 3:
            for char in elveGroup[0]:
                if char in elveGroup[1] and char in elveGroup[2]:
                    score += convertItemToPriority(char)
                    break
            elveGroup = []

    print("Part 2: Priority Score is: ", score)
