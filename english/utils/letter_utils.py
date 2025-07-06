# utils/letter_utils.py
"""
# Functions to draw letters
"""

import config as cfg
from reportlab.pdfbase.ttfonts import TTFont


def draw_letter(canvas, letter, x, y, font="Helvetica", font_size=48, align_center=True):
    """
    Draws a single letter at the specified (x, y) position on the canvas.

    Parameters:
    - canvas: reportlab canvas object
    - letter: the character to draw (usually a single letter)
    - x: x-coordinate
    - y: baseline y-coordinate
    - font: font name
    - font_size: font size in points
    - align_center: if True, centers letter horizontally on x
    """
    canvas.setFont(font, font_size)
    canvas.setFillColor(cfg.TITLE_FONT_COLOR)

    if align_center:
        letter_width = canvas.stringWidth(letter, font, font_size)
        x = x - letter_width / 2

    canvas.drawString(x, y, letter)

