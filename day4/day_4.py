with open('input.txt') as f:
    lines = f.readlines()
    # Part 1
    counter = 0
    for line in lines:
        firstSection, secondSection = line.strip().split(',')
        firstSectionBeginning, firstSectionEnd = firstSection.split('-')
        secondSectionBeginning, secondSectionEnd = secondSection.split('-')
        firstSectionBeginning, firstSectionEnd = int(
            firstSectionBeginning), int(firstSectionEnd)
        secondSectionBeginning, secondSectionEnd = int(
            secondSectionBeginning), int(secondSectionEnd)
        if firstSectionBeginning <= secondSectionBeginning and firstSectionEnd >= secondSectionEnd:
            counter += 1
        elif secondSectionBeginning <= firstSectionBeginning and secondSectionEnd >= firstSectionEnd:
            counter += 1
    print("Part 1: number of occurences: ", counter)

    # Part 2
    counter = 0
    for line in lines:
        firstSection, secondSection = line.strip().split(',')
        firstSectionBeginning, firstSectionEnd = firstSection.split('-')
        secondSectionBeginning, secondSectionEnd = secondSection.split('-')
        firstSectionBeginning, firstSectionEnd = int(
            firstSectionBeginning), int(firstSectionEnd)
        secondSectionBeginning, secondSectionEnd = int(
            secondSectionBeginning), int(secondSectionEnd)
        firstList = range(firstSectionBeginning, firstSectionEnd + 1)
        secondList = range(secondSectionBeginning, secondSectionEnd+1)
        if bool(set(firstList) & set(secondList)):
            counter += 1
        # if firstSectionBeginning <= secondSectionBeginning or firstSectionEnd >= secondSectionEnd:
        #     counter += 1
        # elif secondSectionBeginning <= firstSectionBeginning or secondSectionEnd >= firstSectionEnd:
        #     counter += 1
    print("Part 2: number of occurences: ", counter)
