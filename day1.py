def read_input():
    left_list = []
    right_list = []
    with open("day1.txt") as f:
        text = f.read().split("\n")[:-1] # skip empty last cell
        for pair in text:
            pair = pair.split()
            left_list.append(int(pair[0]))
            right_list.append(int(pair[1]))
    return left_list, right_list

def part1():
    left_list, right_list = read_input()
    left_list.sort()
    right_list.sort()
    tot_distance = 0
    for left_id, right_id in zip(left_list, right_list):
        tot_distance += abs(left_id-right_id)
    print(f"Answer day 1 part 1:\n\tTotal distance: {tot_distance}")

def part2():
    left_list, right_list = read_input()
    dict = {}
    for key in right_list:
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1
    sim_score = 0
    for key in left_list:
        if key in dict:
            sim_score += key*dict[key]

    print(f"Answer day 1 part 2:\n\tSimiliarity Score: {sim_score}")

if __name__ == "__main__":
    part1()
    part2()