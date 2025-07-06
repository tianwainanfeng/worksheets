# worksheets/abc_001.py
"""
About: Worksheet with 4-line grids, large dashed/dotted letters, repeated twice
"""

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import string
from config import *
from utils.title_utils import draw_title, draw_subtitle
from utils.line_utils import draw_dashed_guides
from utils.letter_utils import draw_letter

# ========== Worksheet Configuration ==========

title_text = "ABC Practice Sheet"
subtitle_labels = ["Name", "Date", "Day"]
output_path = "outputs/ws_abc_001.pdf"

# Larger layout
grid_spacing = 80   # spacing between each 4-line block
line_offsets = [0, 15, 30, 45]  # 4 lines
letter_font_size = 50
letters_per_row = 4

# Register dashed font
try:
    pdfmetrics.registerFont(TTFont("Dotted", "fonts/print_clearly_font/PrintDashed.ttf"))
    letter_font = "Dotted"
except:
    letter_font = LETTER_FONT

def generate_abc_001(filename=output_path):
    c = canvas.Canvas(filename, pagesize=letter)

    # Draw title and subtitle
    y = PAGE_HEIGHT - TOP_MARGIN
    draw_title(c, y, title_text, TITLE_FONT, TITLE_FONT_SIZE)
    y -= TITLE_FONT_SIZE * 1.5
    draw_subtitle(c, y, SUBTITLE_FONT, SUBTITLE_FONT_SIZE, subtitle_labels)
    y -= SUBTITLE_FONT_SIZE * 2.5

    usable_height = y - BOTTOM_MARGIN
    block_height = grid_spacing
    num_blocks = int((usable_height + GRID_SPACE) / block_height)

    # Draw dashed guide lines for 4-line grids
    for i in range(num_blocks):
        base_y = y - i * grid_spacing
        for offset in line_offsets:
            y_line = base_y - offset
            c.setStrokeColor(gray)
            c.setLineWidth(1)
            c.setDash(1, 3)  # dashed
            c.line(LEFT_MARGIN, y_line, PAGE_WIDTH - RIGHT_MARGIN, y_line)

    # Draw letters (A–Z, each repeated twice per grid)
    letters = string.ascii_uppercase
    y_base = y - line_offsets[2]  # place letters between 2nd and 3rd line
    c.setFont(letter_font, letter_font_size)

    i = 0
    for block in range(num_blocks):
        x = LEFT_MARGIN
        y_letter = y - block * grid_spacing - line_offsets[2]
        for col in range(letters_per_row):
            if i >= len(letters):
                break
            for _ in range(2):  # repeat each letter twice
                draw_letter(c, letters[i], x, y_letter, letter_font, letter_font_size, False)
                x += 1.15 * letter_font_size
            x += 0.3 * letter_font_size  # extra space between letters
            i += 1

    c.save()
    print(f"Worksheet saved as: {filename}")

if __name__ == "__main__":
    generate_abc_001()
