
def part_one(left_list: list[str], right_list: list[str]) -> None:
    """
    Sum the difference between same numbers from the left and right list
    :param left_list: List of sorted numbers
    :param right_list: List of sorted numbers
    :return: None
    """
    diff_list = list()
    cum_sum = 0

    for a, b in zip(left_list, right_list):
        summary = abs(int(a) - int(b))
        diff_list.append(summary)
        cum_sum += summary

    print(f"The sum is {cum_sum}")

def part_two(left_list: list[str], right_list: list[str]) -> None:
    """
    Sum the multiplying of tho lists. Right list contains the count of given number. Number from left list is multiplied
    by the corresponding number count.
    :param left_list: List of sorted numbers
    :param right_list: List of sorted numbers
    :return: None
    """
    numbers_cnt = dict()
    result = 0

    for b in right_list:
        if not b in numbers_cnt.keys():
            numbers_cnt.setdefault(b, 1)
        else:
            numbers_cnt[b] +=1

    for a in left_list:
        cnt = 0
        if a in numbers_cnt.keys():
            cnt = numbers_cnt[a]
        result += int(a) * cnt

    print(f"The sum of multiplying is {result}")

def main():
    example_list = """3   4
    4   3
    2   5
    1   3
    3   9
    3   3"""

    with open("./input.txt", "r") as fp_input:
        example_list = fp_input.read()

    my_list = example_list.split("\n")
    left_list = list()
    right_list = list()


    for item in my_list:
        if not item:
            continue
        split_items = item.split()
        left_list.append(split_items[0])
        right_list.append(split_items[1])
    left_list.sort()
    right_list.sort()

    if not len(left_list) == len(right_list):
        print("Lists are not the same!")
        return

    part_one(left_list, right_list)
    part_two(left_list, right_list)


if __name__ == '__main__':
    main()
