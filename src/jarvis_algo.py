import numpy as np
import matplotlib.pyplot as plt


def random_points():
    x = []
    y = []
    for i in range(30):
        x.append(np.random.randint(30))
        y.append(np.random.randint(30))
    return x, y


def jarvis_algo(x, y, n):
    convex_hull_x = []
    convex_hull_y = []
    left_pt = find_lowest_y(x, y)
    p = left_pt
    while True:
        convex_hull_x.append(x[p])
        convex_hull_y.append(y[p])
        q = (p + 1) % n
        for i in range(n):
            if orientation(p, i, q) == 2:
                q = i
        p = q
        if x[p] == x[left_pt]:
            convex_hull_x.append(x[left_pt])
            convex_hull_y.append(y[left_pt])
            break
    return convex_hull_x, convex_hull_y


def find_lowest_y(x, y):
    index = 0
    for i in range(len(x)):
        if y[index] > y[i]:
            index = i
        elif y[i] == y[index]:
            if x[i] < x[index]:
                index = i
    return index


def orientation(p, q, r):
    orient_value = (y[q] - y[p]) * (x[r] - x[q]) - (x[q] - x[p]) * (y[r] - y[q])
    if orient_value == 0:
        return 0
    elif orient_value > 0:
        return 1
    else:
        return 2


if __name__ == '__main__':
    x, y = random_points()
    output_x, output_y = jarvis_algo(x, y, len(x))
    plt.plot(x, y, 'o', output_x, output_y, 'o-')
    plt.show()
