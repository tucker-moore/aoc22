instructions = [line.split(' ') for line in open('input').read().splitlines()]

# Sample x at clock cycles based on the input instructions
# Samples give the value of X during that cycle.
def x_samples(instructions):
    clock = 0
    x = 1
    samples = [(0,x)]
    for insn in instructions:
        match insn[0]:
            case 'addx':
                clock += 2
                x += int(insn[1])
                samples.append((clock+1,x))
            case 'noop':
                clock += 1
    return samples

def signal_strength(samples, cycle):
    for i in range(1, len(samples)):
        if samples[i][0] > cycle:
            return cycle * samples[i-1][1]
    return cycle * samples[len(samples)-1][1]

samples = x_samples(instructions)
strengths = map(lambda s: signal_strength(samples, s), [20, 60, 100, 140, 180, 220])
print("part 1: " + str(sum(strengths)))

def draw_chars(samples):
    for y in range(6):
        for x in range(40):
            cycle = y*40 + x + 1
            mid_sprite = signal_strength(samples, cycle) // cycle
            if abs(mid_sprite - x) <= 1:
                print('#', end='')
            else:
                print('.', end='')
        print()

print("part 2:")
draw_chars(samples)
