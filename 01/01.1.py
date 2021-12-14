def main():
    vals = []

    with open("input.txt") as infile:
        for line in infile:
            vals.append(int(line.strip()))    

    count = 0
    for i, val in enumerate(vals[:-1]):
        if vals[i + 1] > vals[i]:
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()