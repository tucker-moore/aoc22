from math import sqrt

class Vec2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return hash(self) == hash(other) and (self.x == other.x and self.y == other.y)

    def __hash__(self):
        return self.x * 1000 + self.y

    def magnitude(self):
        return sqrt(self.x**2 + self.y**2)

def parse_move(line):
    direction, num = line.split(' ')
    num = int(num)
    match direction:
        case 'R':
            return Vec2(num, 0)
        case 'L':
            return Vec2(-num, 0)
        case 'U':
            return Vec2(0, num)
        case 'D':
            return Vec2(0, -num)
    return Vec2(0,0)

moves = [parse_move(line) for line in open('input').read().splitlines()]

# Move the head by the given amount, returning the new head, tail, and positions the tail visited
def do_move(head, tail):
    delta = head - tail
    visited = []
    while delta.magnitude() >= 2:
        dx = delta.x//abs(delta.x) if abs(delta.x) > 0 else 0
        dy = delta.y//abs(delta.y) if abs(delta.y) > 0 else 0
        step = Vec2(dx, dy)
        tail += step
        visited.append(tail)
        delta = head - tail
    return tail, visited

def do_moves(moves, num_tails=1):
    knots = [Vec2(0,0)] + [Vec2(0,0) for _ in range(num_tails)]
    visited = [[knots[0]] for _ in range(num_tails)]

    #def pretty_print_point(p):
    #    i = knots.index(p)
    #    return 'H' if i == 0 else str(i)

    for move in moves:
        dx = move.x//abs(move.x) if abs(move.x) > 0 else 0
        dy = move.y//abs(move.y) if abs(move.y) > 0 else 0
        step = Vec2(dx, dy)
        stepped = Vec2(0,0)
        while stepped != move:
            knots[0] += step
            for i in range(1, num_tails+1):
                tail, newly_visited = do_move(knots[i-1], knots[i])
                knots[i] = tail
                visited[i-1] += newly_visited
            stepped += step

    return [set(v) for v in visited]

def print_points(points, point_to_char_fn=None):
    xs = list(map(lambda p: p.x, points))
    ys = list(map(lambda p: p.y, points))
    tlx = min(xs)
    tly = max(ys)
    brx = max(xs)
    bry = min(ys)

    if point_to_char_fn == None:
        point_to_char_fn = lambda _: '#'

    v = {}
    for p in points:
        v[(p.x, p.y)] = p

    for y in range(tly, bry-1, -1):
        for x in range(tlx, brx+1):
            if x == 0 and y == 0:
                print('s', end='')
            elif (x,y) in v:
                p = v[(x,y)]
                print(point_to_char_fn(p), end='')
            else:
                print('.', end='')
        print()

visited = do_moves(moves)
print("part 1: " + str(len(visited[0])))

visited = do_moves(moves, num_tails=9)
#print_points(visited[8])
print("part 2: " + str(len(visited[8])))
