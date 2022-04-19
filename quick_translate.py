"""
This code allows to edit a text copied from pdf (copied to a .txt file) with
the FillTheNewLines class and translate it into Turkish.

Created by AKE - 19.04.22
"""

from googletrans import Translator
from class_fill_the_new_lines import FillTheNewLines as ftnl #For install: https://github.com/Akerdogmus/Fill-The-New-Lines


def get_raw_text(file_name):
    """
    This function takes the text file to be translated.
    """
    raw_text = ftnl(file_name).main()
    print("EN -> ", raw_text)
    print("------------------------------------------------------")
    translate_text(raw_text)


def translate_text(text):
    """
    This function translates the text to TR from the raw text file.
    """
    translator = Translator()
    translated_text = translator.translate(text, dest="tr")
    print("TR -> ", translated_text.text)


get_raw_text("text.txt")
