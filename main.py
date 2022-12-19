from Key import Key
from DES import DES, BLOCK_SIZE
from Util import Util

if __name__ == "__main__":
  round_keys_dec, round_keys_binary = Key.generate("AABB09182736CCDD")
  plain_text_dec = "123456789ABCDEF"
  plain_text = Util.hexadecimal_to_binary(plain_text_dec)
  print(f"Plain Text: {plain_text_dec}")

  # Normal DES
  # cipher_text = DES.encrypt(plain_text, round_keys_binary, round_keys_dec)
  # print("Cipher Text: ", Util.binary_to_hexadecimal(cipher_text))

  # ECB Encryption & Decryption
  print("\n\n=============== Encryption ==================")
  cipher_text = ''
  for i in range(0, len(plain_text), BLOCK_SIZE):
    plain_text_block = plain_text[i:i + BLOCK_SIZE].ljust(BLOCK_SIZE, '0')
    print("\nCurrent block : ", plain_text_block)
    cipher_text += Util.binary_to_hexadecimal(
      DES.encrypt(plain_text_block, round_keys_binary, round_keys_dec))
  print("Cipher Text : ", cipher_text)

  print("\n\n=============== Decryption ==================")
  decrypted_text = ""
  for i in range(0, len(cipher_text), BLOCK_SIZE):
    cipher_text_block = cipher_text[i:i + BLOCK_SIZE]
    print("Current block : ", cipher_text_block)
    decrypted_text += Util.binary_to_hexadecimal(
      DES.decrypt(cipher_text_block, round_keys_binary, round_keys_dec))

  # remove padding
  decrypted_text_dec = Util.binary_to_hexadecimal(decrypted_text)
  decrypted_text_dec = decrypted_text_dec[:len(plain_text_dec)]
  print("Plain Text : ", decrypted_text_dec)
