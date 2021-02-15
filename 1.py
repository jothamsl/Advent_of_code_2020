
def get_data():
    """Get Data"""
    vals = open("./data/day1.txt").readlines()
    return [int(s.rstrip('\n')) for s in vals]


def part_one(vals):
    for i in vals:
        for j in vals:
            if i + j == 2020:
                res = i*j
    print(res)

def part_two(vals):
    for i in vals:
        for j in vals:
            for k in vals:
                if i + j + k == 2020:
                    res = i * j * k
    print(res)


def main(vals):
    """
    ------- DAY 1: Report Repair -------

    --Part one--
    Find the two entries that sum to 2020 then,
    multiply the two values to get the result.

    --Part two--
    Find the three entries that sum to 2020 then,
    multiply the three values to get the result
    """
    part_one(vals)
    part_two(vals)

if __name__ == "__main__":
    main(get_data())
