sequence = open('input').read().strip()

# Find a marker that is n characters long (substring of n distinct chars)
def find_marker(s, n):
    i = 0
    j = 0
    seen = {}
    while j < n:
        seen[s[j]] = seen.get(s[j], 0) + 1
        j += 1
    while len(seen.keys()) != n:
        seen[s[i]] = seen[s[i]] - 1
        if seen[s[i]] == 0:
            del seen[s[i]]
        i += 1
        seen[s[j]] = seen.get(s[j], 0) + 1
        j += 1
    return j

print("part 1: " + str(find_marker(sequence, 4)))
print("part 2: " + str(find_marker(sequence, 14)))
