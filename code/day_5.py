# %%
def get_file(filepath):
    with open(filepath) as f:
        data = f.readlines()
        data = [x.rstrip() for x in data]
    return data


def parse_vents(data):
    vents = []
    for row in data:
        vent = []
        for point in row.split(" -> "):
            vent.append(tuple((int(point.split(",")[0]), int(point.split(",")[1]))))
        if vent[0][0] == vent[1][0] or vent[0][1] == vent[1][1]:
            vents.append(vent)
    return vents


def extract_all_points(vents):
    points = []
    for vent in vents:
        if vent[0][0] == vent[1][0]:
            min_y, max_y = min(vent[0][1], vent[1][1]), max(vent[0][1], vent[1][1])
            for number in range(min_y, max_y + 1):
                points.append([vent[0][0], number])
        elif vent[0][1] == vent[1][1]:
            min_x, max_x = min(vent[0][0], vent[1][0]), max(vent[0][0], vent[1][0])
            for number in range(min_x, max_x + 1):
                points.append([number, vent[0][1]])
    return points


def create_grid(vents):
    grid_max = 0
    for i in range(len(vents)):
        for point in vents[i]:
            for number in point:
                if number > grid_max:
                    grid_max = number
    grid = [[0] * grid_max for i in range(grid_max)]
    return grid


def mark_grid(grid, points):
    for point in points:
        grid[point[0] - 1][point[1] - 1] += 1

    return grid


def main():
    data = get_file("../data/day_5_data.txt")
    vents = parse_vents(data)
    points = extract_all_points(vents)
    grid = create_grid(vents)
    grid = mark_grid(grid, points)
    danger_zones = 0
    for row in grid:
        for val in row:
            if val > 1:
                danger_zones += 1
    print(danger_zones)


if __name__ == "__main__":
    main()
# %%
