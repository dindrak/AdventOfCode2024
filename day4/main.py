
def get_horiz_cnt(in_matrix: list[list[str]], kwds_full_list: list):
    kwds_cnt = 0

    for word in kwds_full_list:
        word_len = len(word)
        # Standard matrix
        for row_idx, row in enumerate(in_matrix):
            row_idx_min = row_idx
            row_idx_max = row_idx + word_len
            matrix_height = len(in_matrix)
            for col_idx, col in enumerate(row):
                col_idx_min = col_idx
                col_idx_max = col_idx + word_len
                matrix_width = len(row)

                # Match horizontally
                if col_idx_max <= matrix_width:
                    to_test = row[col_idx_min:col_idx_max]
                    to_test = "".join(to_test)
                    if word in to_test:
                        kwds_cnt += 1

    return kwds_cnt

def get_diag_cnt(in_matrix: list[list[str]], kwds_full_list: list):
    kwds_cnt = 0

    for word in kwds_full_list:
        word_len = len(word)
        # Standard matrix
        for row_idx, row in enumerate(in_matrix):
            row_idx_min = row_idx
            row_idx_max = row_idx + word_len
            matrix_height = len(in_matrix)
            for col_idx, col in enumerate(row):
                col_idx_min = col_idx
                col_idx_max = col_idx + word_len
                matrix_width = len(row)

                # Match diagonally
                if col_idx_max <= matrix_width and row_idx_max <= matrix_height:
                    to_test = [in_matrix[row_idx_min + t][col_idx_min + t] for t in range(word_len)]
                    if word in "".join(to_test):
                        kwds_cnt += 1

                # Match reverse diagonally
                if col_idx_min >= word_len-1 and row_idx_max <= matrix_height:
                    to_test = [in_matrix[row_idx_min + t][col_idx_min - t] for t in range(word_len)]
                    if word in "".join(to_test):
                        kwds_cnt += 1

    return kwds_cnt

def get_word_appearance_cnt(in_matrix: list[list[str]], words: list):
    kwds_full_list = []
    for kwd in words:
        kwds_full_list.append(kwd)
        kwds_full_list.append(kwd[::-1])

    horiz_cnt = get_horiz_cnt(in_matrix, kwds_full_list)
    in_matrix_transposed = [list(row) for row in zip(*in_matrix)]
    vert_cnt = get_horiz_cnt(in_matrix_transposed, kwds_full_list)
    diag_cnt = get_diag_cnt(in_matrix, kwds_full_list)


    return horiz_cnt + vert_cnt + diag_cnt


def main():
    input_data = """..X...
.SAMX.
.A..AS
XMASAS
.X.M..
..X..."""

    # with open("./input.txt", "r") as fp_input:
    #     input_data = fp_input.read()

    # List of lists (characters)
    in_matrix = [[char for char in string] for string in input_data.split("\n")]
    in_matrix_transposed = [list(row) for row in zip(*in_matrix)]

    kwds_cnt = 0
    kwds_to_search = ["XMAS"]
    kwd_appearance = get_word_appearance_cnt(in_matrix, kwds_to_search)

    print(f"The 'XMAS' count is {kwd_appearance}.")

if __name__ == '__main__':
    main()
