import re

def do_mul(command: str) -> int:
    mul = command.strip("mul()")
    num_a, num_b = mul.split(",")
    return int(num_a) * int(num_b)

def main():
    input_data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))" # part one
    with open("./input.txt", "r") as fp_input:
        input_data = fp_input.read()


    # Match first mul(X,Y) enabled by default
    match = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input_data) # type: list[str] | None


    if not (match or match):
        print("No 'mul(X,Y)' were found in the corrupted memory.")
        return

    cum_sum = 0

    for cmd in match:
        cum_sum += do_mul(cmd)

    print(f"The sum of all multiplication is {cum_sum}.")

if __name__ == '__main__':
    main()
