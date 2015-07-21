__author__ = "Tom Sherman"
__version__ = "0.1"

"""
    Script to handle OCR from game screenshots.
"""


import hashdict
import solver
from PIL import Image
import tkinter as tk
from tkinter import filedialog


def main():
    img = loadimg


def loadimg():
    """

    :return:
    """

    root = tk.Tk()
    root.withdraw()

    try:
        path = filedialog.askopenfilename()
        return Image.open(path)
    except (FileNotFoundError, OSError) as e:
        print(e)


def readletters(img):
    pass


if __name__ == '__main__':
    main()
