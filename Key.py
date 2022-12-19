from Util import Util


class Key:

  @staticmethod
  def generate(key):
    # --hex to binary
    key = Util.hexadecimal_to_binary(key)
    
    # --parity bit drop table
    keyp = [
      57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35,
      27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38,
      30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
    ]
    
    # getting 56 bit key from 64 bit using the parity bits
    key = Util.permute(key, keyp, 56)
    
    # Number of bit shifts
    shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    
    # Key- Compression Table : Compression of key from 56 bits to 48 bits
    key_comp = [
      14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27,
      20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56,
      34, 53, 46, 42, 50, 36, 29, 32
    ]
    
    # Splitting
    left = key[0:28]
    right = key[28:56]
    
    rkb = [] # rkb for RoundKeys in binary
    rk = [] # rk for RoundKeys in hexadecimal
    for i in range(0, 16):
      # Shifting the bits by nth shifts by checking from shift table
      left = Util.shift_left(left, shift_table[i])
      right = Util.shift_left(right, shift_table[i])
    
      # Combination of left and right string
      combine_str = left + right
    
      # Compression of key from 56 to 48 bits
      round_key = Util.permute(combine_str, key_comp, 48)
    
      rkb.append(round_key)
      rk.append(Util.binary_to_hexadecimal(round_key))

    return rk, rkb