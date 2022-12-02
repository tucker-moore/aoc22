opponent_choice = {'A':0, 'B':1, 'C':2}
my_choice = {'X':0, 'Y':1, 'Z':2}
def line_to_rps(line):
    l,r = line.split(' ')
    return [opponent_choice[l], my_choice[r]]
strats = [line_to_rps(line) for line in open('input').read().strip().split('\n')]
losing_choice = [2, 0, 1]
winning_choice = [1, 2, 0]
outcome_score = [3, 0, 6]
choice_score = [1, 2, 3]

# in: 0 = rock, 1 = paper, 2 = scissors
# out: 0 = draw, 1 = loss, 2 = win
def outcome(a,b):
    if a == b:
        return 0
    elif (a == 0 and b == 2) or (a == 1 and b == 0) or (a == 2 and b == 1):
        return 1
    else:
        return 2

def round_score(strat):
    return choice_score[strat[1]] + outcome_score[outcome(strat[0],strat[1])]

score = sum(map(round_score, strats))
print(score)

def required_choice(strat):
    if strat[1] == 0:
        return losing_choice[strat[0]]
    elif strat[1] == 1:
        return strat[0]
    elif strat[1] == 2:
        return winning_choice[strat[0]]

def part2_score(strat):
    return round_score([strat[0], required_choice(strat)])

score = sum(map(part2_score, strats))
print(score)
