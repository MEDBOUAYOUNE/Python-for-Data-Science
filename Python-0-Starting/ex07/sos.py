# Ref: https://en.wikipedia.org/wiki/Morse_code
import sys


def morse_code():
    NESTED_MORSE = {
        'A': '.-',    'B': '-...',  'C': '-.-.',
        'D': '-..',   'E': '.',     'F': '..-.',
        'G': '--.',   'H': '....',  'I': '..',
        'J': '.---',  'K': '-.-',   'L': '.-..',
        'M': '--',    'N': '-.',    'O': '---',
        'P': '.--.',  'Q': '--.-',  'R': '.-.',
        'S': '...',   'T': '-',     'U': '..-',
        'V': '...-',  'W': '.--',   'X': '-..-',
        'Y': '-.--',  'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.',
        ' ': '/',
    }
    morse_code_string = None

    try:

        assert len(sys.argv) == 2, "AssertionError: the arguments are bad"
        assert all(char.isalnum() or char.isspace() for char in sys.argv[1]), "AssertionError: the arguments are bad"
        morse_code_string = ' '.join(NESTED_MORSE[char.upper()] for char in sys.argv[1] if char.upper() in NESTED_MORSE)
        print(morse_code_string)
    except Exception as error:
        print(error)


if __name__ == "__main__":
    morse_code()
