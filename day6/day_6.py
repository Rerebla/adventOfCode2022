def searchForPacket(window_size, line):
    for i in range(len(line) - window_size + 1):
        window = line[i: i + window_size]
        if len(window) == len(set(window)):
            return i + window_size


with open('input.txt') as f:
    line = f.readline().strip()
    print(f"Part 1: Found after: {searchForPacket(4,line)}")
    print(f"Part 2: Found after: {searchForPacket(14,line)}")
