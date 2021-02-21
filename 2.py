
def get_data():
    """Read & format data"""
    data = open('./data/day2.txt')
    entries = [line for line in data.read().splitlines()]
    letter = []  # Holds all letters being considered in policy
    password = []  # Holds all the passwords from Data base
    lower_bound = []  # lowest possible digits in policy
    upper_bound = []  # Highest possible digits in policy

    for line in entries:
        limits = line.split(' ')[0]
        letter.append(line.split(' ')[1])
        password.append(line.split(' ')[2])
        lower_bound.append(int(limits.split('-')[0]))
        upper_bound.append(int(limits.split('-')[1]))
    letter = [t.split(':')[0] for t in letter]
    return letter, password, lower_bound, upper_bound


def part_one(letters, passwords, lower_bounds, upper_bounds):
    """
    Check if letter in range of lower and upper bound
    """
    valid_count = 0
    for i in range(len(letters)):
        if upper_bounds[i] >= passwords[i].count(letters[i]) >= lower_bounds[i]:
            valid_count += 1
    print(valid_count)


def part_two(letters, passwords, pos1, pos2):
    """
    Check Specified positions for letter in password
    """
    valid_count = 0
    for i in range(len(letters)):
        if bool(passwords[i][pos1[i]-1] == letters[i]) != bool(passwords[i][pos2[i]-1] == letters[i]):
            valid_count += 1
    print(valid_count)

def main():
    """
    ------- Day 2: Password Philosophy ------
    Given a list of passwords and their policies, find how many
    passwords are valid according to their policies.
    """
    part_one(*get_data())
    part_two(*get_data())


if __name__ == "__main__":
    main()
