
def get_data():
    """Get Data"""
    vals = open("./data/day1.txt").readlines()
    return [int(s.rstrip('\n')) for s in vals]


def main(vals):
    """
    ------- DAY 1: Report Repair -------
    Find the two entries that sum to 2020 then,
    multiply the two values to get the answer.
    """
    for i in vals:
        for j in vals:
            if i + j == 2020:
                res = i*j
    print(res)


if __name__ == "__main__":
    main(get_data())
