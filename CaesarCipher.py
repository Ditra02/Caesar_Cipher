import os

os.system('cls')        # clear terminal
os.system('color b')    # change terminal font color

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(text, shift, direction):
    """This function apply caesar cipher

    Args:
        text (string): text that want to encode or decode
        shift (int): how many shift you want to apply to each letter in your text
        direction (string): You can choose encode mode or decode mode
    """
    
    result = ""  # keep the encoded or decoded text

    alpha_len = len(alphabet) - 1

    if shift >= alpha_len:                   # check what if the shift number is bigger than the length of the alpha list
        reset = shift // alpha_len           # Dividing shift number with no remain
        shift = shift - (reset * alpha_len)  # Calculate number that approach the shift number so as the shift number reduced by, the number inside range index of alpa_list obtained

    if direction == 'decode':   # decide to shift forward (encode) or backward(decode)
        shift *= -1

    for letter in text:
        idx_alpa = alphabet.index(letter)   # keep letter index based on alpha list
        shifted_idx = idx_alpa + shift      # shifting letter index

        after_shift = alphabet[shifted_idx] # found letter with shifted index
        result += after_shift               # keep the letter

    print(f"Here's the {direction}d result : {result}")


caesar(text=text, shift=shift, direction=direction)
