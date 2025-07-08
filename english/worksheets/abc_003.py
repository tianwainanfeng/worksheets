# worksheets/abc_003.py
"""
About: Worksheet showing each uppercase letter with a word (A for Apple, B for Ball, etc.)
"""

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import gray, black
from reportlab.lib.units import inch
import string
from config import *
from utils.title_utils import draw_title, draw_subtitle
from utils.line_utils import draw_dashed_guides
from utils.letter_utils import draw_letter

# ========== Worksheet Configuration ==========

title_text = "ABC Word Worksheet"
subtitle_labels = ["Name", "Date", "Day"]
output_path = "outputs/ws_abc_003.pdf"

grid_spacing = 65   # spacing between each 4-line block
line_offsets = [0, 15, 30, 45]  # 4 lines
letter_font_size = 50
letters_per_row = 3

letter_font_size = 48
word_font_size = 48

# A–Z with common words
abc_words = {
    'A': "Apple",    'B': "Ball",     'C': "Cat",     'D': "Dog",
    'E': "Egg",      'F': "Fish",     'G': "Giraffe", 'H': "Hat",
    'I': "Ice",      'J': "Juice",    'K': "Kite",    'L': "Lion",
    'M': "Monkey",   'N': "Nest",     'O': "Orange",  'P': "Panda",
    'Q': "Queen",    'R': "Rabbit",   'S': "Sun",     'T': "Tiger",
    'U': "Umbrella", 'V': "Violin",   'W': "Whale",   'X': "Xylophone",
    'Y': "Yarn",     'Z': "Zebra"
}

# Register font
try:
    pdfmetrics.registerFont(TTFont("Dotted", "fonts/print_clearly_font/PrintDashed.ttf"))
    word_font = "Dotted"

    pdfmetrics.registerFont(TTFont("PrintClearly", "fonts/print_clearly_font/PrintClearly.ttf"))
    letter_font = "PrintClearly"
except:
    letter_font = LETTER_FONT
    word_font = "Helvetica"


def generate_abc_003(filename=output_path):
    c = canvas.Canvas(filename, pagesize=letter)

    # Title and subtitle
    y = PAGE_HEIGHT - TOP_MARGIN
    draw_title(c, y, title_text, TITLE_FONT, TITLE_FONT_SIZE)
    y -= TITLE_FONT_SIZE * 1.5
    draw_subtitle(c, y, SUBTITLE_FONT, SUBTITLE_FONT_SIZE, subtitle_labels)
    y -= SUBTITLE_FONT_SIZE * 2.5

    usable_height = y - BOTTOM_MARGIN
    block_height = grid_spacing
    num_blocks = int((usable_height + GRID_SPACE) / block_height)

    letters = list(abc_words.keys())
    y_base = y - line_offsets[2]

    i = 0
    for block in range(num_blocks):
        if i >= len(letters):
            break

        base_y = y - block * grid_spacing

        # Draw 4-line dashed guides
        for offset in line_offsets:
            y_line = base_y - offset
            c.setStrokeColor(gray)
            c.setLineWidth(1)
            c.setDash(1, 3)
            c.line(LEFT_MARGIN, y_line, PAGE_WIDTH - RIGHT_MARGIN, y_line)

        x = LEFT_MARGIN
        for col in range(letters_per_row):
            if i >= len(letters):
                break

            char = letters[i]
            word = abc_words[char]
            y_letter = base_y - line_offsets[2]

            # Draw the uppercase letter
            draw_letter(c, char, x, y_letter, letter_font, letter_font_size, align_center=False)

            # Draw the word to the right
            c.setFont(word_font, word_font_size)
            c.setFillColor(black)
            c.drawString(x + 0.6 * letter_font_size, y_letter, f"{word}")

            i += 1
            if col == 1:
                x -= 0.2 * inch
            x += PAGE_WIDTH / letters_per_row - 0.55 * inch

    c.save()
    print(f"Worksheet saved as: {filename}")

if __name__ == "__main__":
    generate_abc_003()
