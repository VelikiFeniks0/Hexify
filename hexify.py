# Hexify v1.0 Python3
# works on any platform

# Made by VelikiFeniks

# This project is under public domain (CC0, The Unlicense)

# How to use:
#   open your terminal, and type "python hexify.py" and as arguments put your image path, and your binary file path where the image's bytes would be written.
#   and the last argument is for displaying the bytes, if you want to display them, type "y", if not, then "n".

from time import sleep
from os import system
from datetime import date
from PIL import Image
import sys

# main function
def main() -> None:

    # initialize
    print("Initializing...")
    sleep(0.3)
    system("CLS")
    system("title Hexify v1.0")

    # constants
    IMAGE = sys.argv[1]       # image file
    RESULT = sys.argv[2]      # result .BIN file



    print(f"\x1b[95mHexify v1.0\x1b[0m\tDate: {date.today()}")
    print(f"\x1b[92mHEXIFYING \"{IMAGE}\"\x1b[0m\nResult file: \"{RESULT}\"\n")

    print("\x1b[37m[\x1b[92mLOG\x1b[37m]:\x1b[0m Accessing result file")
    print("\x1b[37m[\x1b[92mLOG\x1b[37m]:\x1b[0m Reading image file")


    # converts pixels to bytes
    bits = Image.open(IMAGE).convert("RGB").tobytes()

    # writes bytes to RESULT binary file
    with open(RESULT, "wb") as file:
        file.write(bits)
        file.close()


    print("\x1b[37m[\x1b[92mLOG\x1b[37m]:\x1b[0m Hexifying image")
    print("\x1b[37m[\x1b[95mLHEX\x1b[37m]:\x1b[0m Hexifying image [IMAGE FILE]")
    print("\x1b[37m[\x1b[95mRHEX\x1b[37m]:\x1b[0m Hexifying image [RESULT FILE]")
    print(f"\x1b[37m[\x1b[95mRESULT HEX\x1b[37m]:\x1b[0m Writing hexified image to {RESULT}")
    sleep(1)
    print("\x1b[92mDONE!\x1b[0m")
    sleep(0.3)

    # if y, display bits (bytes). if n, don't display.
    if sys.argv[3].lower() == "y":
        print(bits)

    elif sys.argv[3].lower() == "n":
        pass
    else:
        print(f"Invalid argument -> \"{sys.argv[3]}\"")

    # exit
    input("\npress enter to exit")
    exit(0)


if __name__ == "__main__":
    main()