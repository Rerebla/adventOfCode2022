def cal_each_elve(lines: list[str]):
    counter = 0
    totals: list[int] = []
    for line in lines:
        if line == '\n':
            totals.append(counter)
            counter = 0
            continue
        counter += int(line)
    return totals


with open('input.txt') as f:
    totals = cal_each_elve(f.readlines())
    # Part 1

    # highest_calories, counter = 0, 0
    # lines = f.readlines()
    # for line in lines:
    #     if line == "\n" and counter > highest_calories:
    #         highest_calories, counter = counter, 0
    #         continue
    #     if line == "\n":
    #         counter = 0
    #         continue
    #     counter += int(line)

    print('Part 1: Highest calorie amount is:', max(totals), '\n')

    # Part 2

    top_three = sorted(totals)[-3:]
    print('Part 2: Top three elves carry each: ', top_three)
    print('Part 2: Combined: ', sum(top_three))
