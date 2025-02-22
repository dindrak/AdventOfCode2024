

def main():
    input_data = "2333133121414131402"

    # with open("./input.txt", "r") as fp_input:
    #     input_data = fp_input.read().strip()

    blocks_arr = []
    idn = 0

    for item_idx, item in enumerate(input_data):
        if item_idx % 2:
            # Liche cislo
            blocks_arr.append('.'*int(item))
        else:
            # Sude cislo
            blocks_arr.append(str(idn)*int(item))
            idn+=1


    blocks_str = "".join(blocks_arr)
    blocks_arr.reverse()
    blocks_str_rev = "".join(blocks_arr)
    print(blocks_str)
    print(blocks_str_rev)

    arr_final = []
    for f, b in zip(blocks_str, blocks_str_rev):
        if f == ".":
            arr_final.append(b)
        else:
            arr_final.append(f)

if __name__ == '__main__':
    main()
