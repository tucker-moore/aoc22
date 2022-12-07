def make_range(p):
    return [int(x) for x in p.split('-')]

ranges = [list(map(make_range, s.split(','))) for s in open('input').read().splitlines()]

def do_ranges_contain(r1, r2):
    return (r1[0] <= r2[0] and r1[1] >= r2[1]) or (r2[0] <= r1[0] and r2[1] >= r1[1])

containing_pairs = list(filter(lambda p: do_ranges_contain(p[0], p[1]), ranges))
print("part 1: " + str(len(containing_pairs)))


def do_ranges_overlap(r1, r2):
    return (r1[0] <= r2[0] and r1[1] >= r2[0]) or (r2[0] <= r1[0] and r2[1] >= r1[0])

overlapping_pairs = list(filter(lambda p: do_ranges_overlap(p[0], p[1]), ranges))
print("part 2: " + str(len(overlapping_pairs)))
