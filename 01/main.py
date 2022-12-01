from heapq import heapify, heappop

elves = [[int(x) for x in elf.split('\n') if x != ''] for elf in open('input').read().split('\n\n')]

total_calories = [sum(elf_calories) for elf_calories in elves] # total per elf
most_calories = max(total_calories)
print("part 1: " + str(most_calories))

top_total_calories = [x * -1 for x in total_calories] # heapq is a minheap...
heapify(top_total_calories)
top3sum = sum([x * -1 for x in [heappop(top_total_calories), heappop(top_total_calories), heappop(top_total_calories)]])
print("part 2: " + str(top3sum))
