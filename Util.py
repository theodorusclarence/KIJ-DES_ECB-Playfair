class Util:

  @staticmethod
  def hexadecimal_to_binary(hexadecimal):
    mapping = {
      "0": "0000",
      "1": "0001",
      "2": "0010",
      "3": "0011",
      "4": "0100",
      "5": "0101",
      "6": "0110",
      "7": "0111",
      "8": "1000",
      "9": "1001",
      "A": "1010",
      "B": "1011",
      "C": "1100",
      "D": "1101",
      "E": "1110",
      "F": "1111",
    }
    binary = ""
    for i in range(len(hexadecimal)):
      binary = binary + mapping[hexadecimal[i]]
    return binary

  @staticmethod
  def binary_to_hexadecimal(binary):
    mapping = {
      "0000": "0",
      "0001": "1",
      "0010": "2",
      "0011": "3",
      "0100": "4",
      "0101": "5",
      "0110": "6",
      "0111": "7",
      "1000": "8",
      "1001": "9",
      "1010": "A",
      "1011": "B",
      "1100": "C",
      "1101": "D",
      "1110": "E",
      "1111": "F",
    }
    hexadecimal = ""
    for i in range(0, len(binary), 4):
      ch = ""
      ch = ch + binary[i]
      ch = ch + binary[i + 1]
      ch = ch + binary[i + 2]
      ch = ch + binary[i + 3]
      hexadecimal = hexadecimal + mapping[ch]

    return hexadecimal

  @staticmethod
  def binary_to_decimal(binary):
    decimal, i, n = 0, 0, 0
    while binary != 0:
      dec = binary % 10
      decimal = decimal + dec * pow(2, i)
      binary = binary // 10
      i += 1
    return decimal

  @staticmethod
  def decimal_to_binary(num):
    res = bin(num).replace("0b", "")
    if len(res) % 4 != 0:
      div = len(res) / 4
      div = int(div)
      counter = (4 * (div + 1)) - len(res)
      for i in range(0, counter):
        res = "0" + res
    return res

  @staticmethod
  def dec2bin(num):
    res = bin(num).replace("0b", "")
    if len(res) % 4 != 0:
      div = len(res) / 4
      div = int(div)
      counter = (4 * (div + 1)) - len(res)
      for i in range(0, counter):
        res = "0" + res
    return res

  # Permute function to rearrange the bits
  @staticmethod
  def permute(k, arr, n):
    permutation = ""
    for i in range(0, n):
      permutation = permutation + k[arr[i] - 1]
    return permutation

  # shifting the bits towards left by nth shifts
  @staticmethod
  def shift_left(k, nth_shifts):
    s = ""
    for i in range(nth_shifts):
      for j in range(1, len(k)):
        s = s + k[j]
      s = s + k[0]
      k = s
      s = ""
    return k

  # calculating xor of two strings of binary number a and b
  @staticmethod
  def xor(a, b):
    ans = ""
    for i in range(len(a)):
      if a[i] == b[i]:
        ans = ans + "0"
      else:
        ans = ans + "1"
    return ans
