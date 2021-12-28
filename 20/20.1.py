#!/usr/bin/env python3

PADDING = 6

def main():
    with open("input.txt") as infile:
        algo = infile.readline().strip()
        infile.readline()

        image_raw = []
        for line in infile.readlines():
            image_raw.append(list(line.strip()))

    image = pad_image(image_raw, PADDING)
    tmp = run_algo(image, algo)
    out = run_algo(tmp, algo)
    
    light_px = 0
    for line in out:
        light_px += line.count("#")
    print(light_px)

def run_algo(image, algo):
    out = [["."] * len(image[0]) for line in range(len(image))]
    for i, line in enumerate(image):
        for j, char in enumerate(line):
            neighbor_str = get_neighbor_str(image, i, j)
            neighbor_str = neighbor_str.replace(".", "0")
            neighbor_str = neighbor_str.replace("#", "1")
            idx = int(neighbor_str, 2)
            out[i][j] = algo[idx]
    return out

def get_neighbor_str(image, line, char):
    out = []
    for nline in [-1, 0, 1]:
        for nchar in [-1, 0, 1]:
            try:
                out.append(image[line + nline][char + nchar])
            except IndexError:
                out.append(".")
    return "".join(out)

def pad_image(image_raw, pad_size):
    out = []
    image_width = len(image_raw[0])
    for _ in range(pad_size):
        out.append(["."] * (image_width + pad_size * 2))
    for row in image_raw:
        out.append(["."] * pad_size + row + ["."] * pad_size)
    for _ in range(pad_size):
        out.append(["."] * (image_width + pad_size * 2))
    return out

if __name__ == "__main__":
    main()