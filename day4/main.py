
def main():
    input_data = """..X...
.SAMX.
.A..A.
XMAS.S
.X...."""

    # with open("./input.txt", "r") as fp_input:
    #     input_data = fp_input.read()

    # List of lists (characters)
    in_matrix = [[char for char in string] for string in input_data.split("\n")]
    in_matrix_transposed = [list(row) for row in zip(*in_matrix)]

    kwds_cnt = 0
    kwds_to_search = ["XMAS"]
    kwds_full_list = []
    for kwd in kwds_to_search:
        kwds_full_list.append(kwd)
        kwds_full_list.append(kwd[::-1])

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

                # Match diagonally
                if col_idx_max <= matrix_width and row_idx_max <= matrix_height:
                    to_test = [in_matrix[row_idx_min + t][col_idx_min + t] for t in range(word_len)]
                    if word in "".join(to_test):
                        kwds_cnt += 1

        # Transposed matrix - match horizontally
        for row in in_matrix_transposed:
            for col_idx, col in enumerate(row):
                col_idx_min = col_idx
                row_idx_max = col_idx + word_len
                matrix_height = len(row)
                if row_idx_max <= matrix_height:
                    to_test = row[col_idx_min:row_idx_max]
                    to_test = "".join(to_test)
                    if word in to_test:
                        kwds_cnt += 1

    print(f"The 'XMAS' count is {kwds_cnt}.")

if __name__ == '__main__':
    main()
