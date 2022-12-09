from functools import reduce
from math import inf

trees = [[int(c) for c in line] for line in open('input').read().splitlines()]

def in_bounds(trees, x, y):
    return x >= 0 and x < len(trees[0]) and y >= 0 and y < len(trees)

def visible(trees, x, y, dx, dy):
    lowest = -1
    seen = set()
    while in_bounds(trees, x, y):
        if trees[y][x] > lowest:
            seen.add((x,y))
            lowest = trees[y][x]
        x += dx
        y += dy
    return seen

def all_visible(trees):
    seen = []
    for y in range(len(trees)):
        seen += visible(trees, 0, y, 1, 0)
        seen += visible(trees, len(trees[0])-1, y, -1, 0)
    for x in range(len(trees[0])):
        seen += visible(trees, x, 0, 0, 1)
        seen += visible(trees, x, len(trees)-1, 0, -1)
    return set(seen)

def visible_from_height(trees, x, y, dx, dy, height):
    seen = set()
    while in_bounds(trees, x, y) and trees[y][x] < height:
        seen.add((x,y))
        x += dx
        y += dy
    if in_bounds(trees, x, y):
        seen.add((x,y))
    return seen

def scenic_score(trees, x, y):
    max_height = trees[y][x]
    up = len(visible_from_height(trees, x, y-1, 0, -1, max_height))
    down = len(visible_from_height(trees, x, y+1, 0, 1, max_height))
    left = len(visible_from_height(trees, x-1, y, -1, 0, max_height))
    right = len(visible_from_height(trees, x+1, y, 1, 0, max_height))
    #print({ 'coord': (x,y), 'up': up, 'down': down, 'left': left, 'right': right })
    return up * down * left * right

def highest_scenic_score(trees):
    all_coords = [(x,y) for y in range(len(trees)) for x in range(len(trees[0]))]
    return max(map(lambda c: scenic_score(trees, c[0], c[1]), all_coords))

print("part 1: " + str(len(all_visible(trees))))
print("part 2: " + str(highest_scenic_score(trees)))
