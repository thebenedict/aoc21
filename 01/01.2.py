def main():
    vals = []

    with open("input.txt") as infile:
        for line in infile:
            vals.append(int(line.strip()))    

    count = 0
    for i, val in enumerate(vals[:-3]):
        if sum(vals[i + 1:i + 4]) > sum(vals[i:i + 3]):
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()