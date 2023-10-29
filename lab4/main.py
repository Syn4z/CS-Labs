from data import expansion_table, s_boxes, p_table


def des_round(Li_minus_1, Ri_minus_1, subkey):
    # Expand the 32-bit input to 48 bits
    expanded_Ri_minus_1 = [Ri_minus_1[i - 1] for i in expansion_table]

    # XOR with the subkey
    xor_result = [int(expanded_Ri_minus_1[i]) ^ int(subkey[i]) for i in range(48)]

    # Pass the result through S-boxes
    s_box_output = []
    for i in range(8):
        s_box_input = xor_result[i * 6:(i + 1) * 6]
        row = int(str(s_box_input[0]) + str(s_box_input[5]), 2)
        col = int(''.join(map(str, s_box_input[1:5])), 2)
        s_box_value = s_boxes[i][row][col]
        s_box_output.extend([int(bit) for bit in format(s_box_value, '04b')])

    # Permute the result using P-table
    permuted_result = [s_box_output[i - 1] for i in p_table]

    # XOR with Li_minus_1 to get Ri
    Ri = [int(permuted_result[i]) ^ int(Li_minus_1[i]) for i in range(32)]

    return Ri


Li_minus_1 = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1,
              1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1]

Ri_minus_1 = [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1,
              0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1]

subkey = [1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1,
          0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0,
          0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1]

Ri = des_round(Li_minus_1, Ri_minus_1, subkey)
print("Ri:", Ri)
