# split a rucksack into compartments
def make_rucksack(s):
    c1 = set(s[0:len(s)//2])
    c2 = set(s[len(s)//2:len(s)])
    w = c1.union(c2)
    return [c1, c2, w]

# convert a-z and A-Z to priorities from 1-52
def priority(c):
    ascii_char = ord(c)
    if ascii_char < ord('a'):
        return ascii_char - ord('A') + 1 + 26
    else:
        return ascii_char - ord('a') + 1

rucksack_common = lambda r: r[0].intersection(r[1])

def rucksack_priorities(r):
    return sum(map(priority, rucksack_common(r)))

rucksacks = [make_rucksack(line) for line in open('input').read().splitlines()]

total_priority = sum(map(rucksack_priorities, rucksacks))
print("part 1: " + str(total_priority))

total_group_priority = 0
while len(rucksacks) > 0:
    g1, g2, g3 = [rucksacks.pop(0), rucksacks.pop(0), rucksacks.pop(0)]
    total_group_priority += sum(map(priority, g1[2].intersection(g2[2]).intersection(g3[2])))
print("part 2: " + str(total_group_priority))
