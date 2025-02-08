
def is_increasing(report: list[str]):
    prev_level = 0

    for level in report:
        level_int = int(level)
        if int(level_int) < prev_level:
            return False
        else:
            prev_level = level_int

    return True

def is_decreasing(report: list[str]):
    prev_level = 1000

    for level in report:
        level_int = int(level)
        if int(level_int) > prev_level:
            return False
        else:
            prev_level = level_int

    return True

def is_within_limit(report: list[str]):
    prev_level = 1000
    report_len = len(report)

    for idx, level in enumerate(report):
        level_int = int(level)

        if idx != report_len-1:
            next_level = report[idx + 1]
            next_level_int = int(next_level)
            if abs(level_int-next_level_int) < 1 or abs(level_int-next_level_int) > 3:
                return False

    return True

def main():
    input_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

    with open("./input.txt", "r") as fp_input:
        input_data = fp_input.read()

    safe_reports = 0

    for report in input_data.split("\n"):
        if not report:
            continue
        if not (is_increasing(report.split()) or is_decreasing(report.split())):
            continue
        if not is_within_limit(report.split()):
            continue

        safe_reports +=1

    print(f"The {safe_reports} reports are safe.")


if __name__ == '__main__':
    main()
