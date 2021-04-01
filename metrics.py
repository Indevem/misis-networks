def compute_euclidean_distance(point, rect):

    def point_point(pt):
        return ((point[0] - pt[0]) ** 2) + ((point[1] - pt[1]) ** 2)

    def segment_point(segment):
        x1, y1, x2, y2 = segment
        x, y = point

        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1

        if y1 == y2:
            if x >= x1 and x <= x2:
                return abs(y - y1)
            else:
                return min(point_point((x1, y1)), point_point((x2, y2)))
        elif x1 == x2:
            if y >= y1 and y <= y2:
                return abs(x - x1)
            else:
                return min(point_point((x1, y1)), point_point((x2, y2)))

        raise ValueError("CAN rectangle error")


    x1, y1, x2, y2 = rect
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    if x1 <= point[0] and point[0] <= x2 and y1 <= point[1] and point[1] <= y2:
        return 0

    return min(segment_point((x1, y1, x1, y2)), segment_point((x1, y2, x2, y2)),
               segment_point((x2, y2, x2, y1)), segment_point((x2, y1, x1, y1)))


def compute_distance(point, rect):
    distance = 2.0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            distance = min(distance, compute_euclidean_distance((point[0] + i, point[1] + j), rect))
    return distance


def find_center(rect):
    return (rect[0] + rect[2]) / 2, (rect[1] + rect[3]) / 2
