with open('input.txt') as f:
    line = f.readline().strip()
    window_size = 4

    for i in range(len(line) - window_size + 1):
        window = line[i: i + window_size]
        if len(window) == len(set(window)):
            print(window)
            print(i + window_size)
            break

    window_size = 14
    for i in range(len(line) - window_size + 1):
        window = line[i: i + window_size]
        if len(window) == len(set(window)):
            print(window)
            print(i + window_size)
            break
