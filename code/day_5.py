# %% PART 1 --------------------------------------------------------------------
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
        x1 = vent[0][0]
        x2 = vent[1][0]
        y1 = vent[0][1]
        y2 = vent[1][1]
        # Vertical Lines
        if x1 == x2:
            min_y, max_y = min(y1, y2), max(y1, y2)
            for number in range(min_y, max_y + 1):
                points.append([x1, number])
        # Horizontal Lines
        else:
            y1 == y2
            min_x, max_x = min(x1, x2), max(x1, x2)
            for number in range(min_x, max_x + 1):
                points.append([number, y1])
    return points


def create_grid(vents):
    grid_max = 0
    for vent in vents:
        for point in vent:
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
    print(f"{danger_zones} Danger Zones.")


if __name__ == "__main__":
    main()

# %% PART 2 --------------------------------------------------------------------
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
            vent.append([int(point.split(",")[0]), int(point.split(",")[1])])
        vents.append(vent)
    return vents


def extract_all_points(vents):
    points = []
    for vent in vents:
        # Make sure point has lowest x number in first coordinate
        if vent[0][0] > vent[1][0]:
            vent.reverse()
        x1 = vent[0][0]
        x2 = vent[1][0]
        y1 = vent[0][1]
        y2 = vent[1][1]
        # Horizontal Lines
        if x1 == x2:
            min_y, max_y = min(y1, y2), max(y1, y2)
            for number in range(min_y, max_y + 1):
                points.append([x1, number])
        # Vertical Lines
        elif y1 == y2:
            min_x, max_x = min(x1, x2), max(x1, x2)
            for number in range(min_x, max_x + 1):
                points.append([number, y1])
        # Diagonal Up to the Right
        elif y1 < y2:
            min_x, max_x = min(x1, x2), max(x1, x2)
            y = y1
            for number in range(min_x, max_x + 1):
                points.append([number, y])
                y += 1
        # Diagonal Down to the Right
        else:
            min_x, max_x = min(x1, x2), max(x1, x2)
            y = y1
            for number in range(min_x, max_x + 1):
                points.append([number, y])
                y -= 1

    return points


def create_grid(vents):
    grid_max = 0
    for vent in vents:
        for point in vent:
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
    print(f"{danger_zones} Danger Zones.")


if __name__ == "__main__":
    main()

# %%
