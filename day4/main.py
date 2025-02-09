
def is_word_in_line(line: list[str], word: str) -> bool:
    word_len = len(word)
    for char_idx, char in enumerate(line):
        low_lim = char_idx
        up_lim = char_idx + word_len
        line_len = len(line)
        if up_lim <= line_len:
            to_test = line[low_lim:up_lim]
            to_test = "".join(to_test)
            if word in to_test:
                return True

def main():
    input_data = """..X...
.SAMX.
.A..A.
XMAS.S
.X...."""

    # with open("./input.txt", "r") as fp_input:
    #     input_data = fp_input.read()

    # List of strings
    input_data_lofs = input_data.split("\n")
    # List of lists (characters)
    input_data_lofl = []
    for string in input_data_lofs:
        temp_list = []
        for char in string:
            temp_list.append(char)
        input_data_lofl.append(temp_list)

    input_data_lofl_transposed = [list(row) for row in zip(*input_data_lofl)]

    xmas_cnt = 0
    for word in ["XMAS", "SAMX"]:
        # Match horizontally in standard matrix
        for line in input_data_lofl:
            if is_word_in_line(line, word):
                xmas_cnt += 1

        # Match horizontally in transposed matrix
        for line in input_data_lofl_transposed:
            if is_word_in_line(line, word):
                xmas_cnt += 1

    print(f"The 'XMAS' count is {xmas_cnt}.")

if __name__ == '__main__':
    main()
