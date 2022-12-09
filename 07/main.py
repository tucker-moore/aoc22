def parse_directories(filename):
    lines = open(filename).read().splitlines()
    root = {}
    root['..'] = root
    cd = None
    while len(lines) > 0:
        words = lines.pop(0).split(' ')
        assert len(words) > 0 and words[0] == '$'
        cmd = words[1]
        if cmd == 'cd':
            arg = words[2]
            if arg == '/':
                cd = root
            else:
                cd = cd[arg]
        elif cmd == 'ls':
            while len(lines) > 0 and not lines[0].startswith('$'):
                size, name = lines.pop(0).split(' ')
                if size == 'dir':
                    cd[name] = { '..': cd }
                else:
                    cd[name] = int(size)
    return root

def dir_sizes_rec(tree, current_dir, current_sizes):
    if type(tree) == int:
        return 0
    total_size = 0
    for d in tree:
        if d == '..':
            continue
        if type(tree[d]) == int:
            total_size += tree[d]
        else:
            next_dir = current_dir + d if current_dir == '/' else current_dir + '/' + d
            total_size += dir_sizes_rec(tree[d], next_dir, current_sizes)
    current_sizes += [[current_dir, total_size]]
    return total_size

# Calculate the sizes of every directory, returning path-size pairs (e.g. [['/', 1234], ['/a', 30]])
def dir_sizes(tree):
    current_sizes = []
    total_size = dir_sizes_rec(tree, '/', current_sizes)
    return current_sizes

tree = parse_directories('input')
sizes = dir_sizes(tree)
small_enough_sizes = filter(lambda s: s[1] <= 100000, sizes)
print("part 1: " + str(sum(map(lambda s: s[1], small_enough_sizes))))

total_fs_size = 70000000
unused_space_needed = 30000000
currently_used = list(filter(lambda s: s[0] == '/', sizes))[0][1]
delete_candidates = list(filter(lambda s: total_fs_size - (currently_used - s[1]) >= unused_space_needed, sizes))
best_delete_candidate = min(delete_candidates, key=lambda s: s[1])
print("part 2: " + str(best_delete_candidate[1]))
