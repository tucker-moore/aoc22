from copy import deepcopy

def filter_n(l,n):
    return list(map(lambda p: p[1], filter(lambda p: p[0] % 2 == n, enumerate(l))))

def filter_even(l):
    return filter_n(l, 0)

def filter_odd(l):
    return filter_n(l, 1)

def parse_stack_line(l):
    return filter_even(filter_odd(l))

lines = open('input').read().splitlines()

# Build stacks
tab_end = lines.index('')
table = lines[0:tab_end][::-1]
num_stacks = len(parse_stack_line(table[0]))
initial_stacks = [[] for _ in range(num_stacks)]
for line in table[1:]:
    line = parse_stack_line(line)
    for i,c in enumerate(line):
        if c != ' ':
            initial_stacks[i] += [c]

def parse_move(l):
    ns = [int(s) for s in filter_odd(l.split(' '))]
    return [ns[0], ns[1]-1, ns[2]-1]

moves = [parse_move(l) for l in lines[tab_end+1:]]

# Move n boxes from stack 'f' to stack 't' one at a time
def stack_move_fn(stacks, n, f, t):
    while n != 0:
        c = stacks[f].pop()
        stacks[t].append(c)
        n -= 1

# Move n boxes from stack 'f' to stack 't' all at once, preserving order
def full_move_fn(stacks, n, f, t):
    offset = len(stacks[f])-n
    boxes = stacks[f][offset:]
    stacks[f] = stacks[f][:offset]
    stacks[t] += boxes

def solve(stacks, move_fn):
    for m in moves:
        move_fn(stacks, m[0], m[1], m[2])

    tops = ''.join(list(map(lambda s: s[len(s)-1], stacks)))
    return tops

part1 = solve(deepcopy(initial_stacks), stack_move_fn)
print("part 1: " + part1)
part2 = solve(deepcopy(initial_stacks), full_move_fn)
print("part 2: " + part2)
