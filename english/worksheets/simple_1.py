# worksheets/simple_1.py
""""
# =============================================================================
About: script for a simple ABC worksheet
# =============================================================================
"""

# ReportLab: a powerful and widely used Python library for generating PDFs programmatically
#from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, gray, Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import string
from config import *
from utils.title_utils import draw_title, draw_subtitle
from utils.line_utils import draw_dashed_guides
from utils.letter_utils import draw_letter

# ======== Options ========

is_draw_title = True
is_draw_subtitle = True
is_draw_lines = True
is_draw_letters = True


# ======== Page Geometry ========

# Convert points to inches (1 inch = 72 points)
width_in = PAGE_WIDTH / 72
height_in = PAGE_HEIGHT / 72

print(f"Page size (inches): {width_in:.2f} in x {height_in:.2f} in")
print(f"Page size (points): {PAGE_WIDTH} x {PAGE_HEIGHT}")

# Convert to inches
top_in = TOP_MARGIN / 72
bottom_in = BOTTOM_MARGIN / 72
left_in = LEFT_MARGIN / 72
right_in = RIGHT_MARGIN / 72

print("Page margins:")
print(f"  Top:    {TOP_MARGIN} pts ({top_in:.2f} in)")
print(f"  Bottom: {BOTTOM_MARGIN} pts ({bottom_in:.2f} in)")
print(f"  Left:   {LEFT_MARGIN} pts ({left_in:.2f} in)")
print(f"  Right:  {RIGHT_MARGIN} pts ({right_in:.2f} in)")

# (0, 0) at the bottom-left corner of the page
y_base = PAGE_HEIGHT - TOP_MARGIN

# ======== Title Sytle ========

title_text = "Simple Worksheet"
title_font = TITLE_FONT
title_font_size = TITLE_FONT_SIZE
title_font_color = TITLE_FONT_COLOR

title_y_base = y_base

if is_draw_title:
    y_base -= TITLE_FONT_SIZE * 1.5

subtitle_font = SUBTITLE_FONT
subtitle_font_size = SUBTITLE_FONT_SIZE
subtitle_font_color = SUBTITLE_FONT_COLOR

subtitle_y_base = y_base
subtitle_labels = ["Name", "Date", "Days"]

if is_draw_subtitle:
    y_base -= SUBTITLE_FONT_SIZE * 2.5

# ======== Line Style ========

# calculate how many grid
usable_height = y_base - BOTTOM_MARGIN
grid_height = GRID_SPACE + LINE_OFFSETS[-1]

num_grids = int((usable_height + GRID_SPACE) / grid_height)
print(f"Number of grids that fit: {num_grids}")

# ======== Letter Style ========

# Register a handwriting/tracing-style font if available
# Otherwise fallback to Helvetica
try:
    #pdfmetrics.registerFont(TTFont('Dotted', 'fonts/kg_primary_dots/KGPrimaryDots.ttf'))  # Example font
    pdfmetrics.registerFont(TTFont("Dotted", "fonts/print_clearly_font/PrintDashed.ttf"))
    letter_font = 'Dotted'
except:
    letter_font = LETTER_FONT

#letter_font = LETTER_FONT
letter_font_size = LETTER_FONT_SIZE
letter_font_color = LETTER_FONT_COLOR

letter_y_base = y_base
if is_draw_lines:
    letter_y_base -= LINE_OFFSETS[-2]

letters_per_row = LETTERS_PER_ROW
letters_lowercase = string.ascii_lowercase
letters_uppercase = string.ascii_uppercase

# -------- Drawing Lines --------


def generate_simple_1(filename="outputs/ws_simple_1.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    if is_draw_title:
        draw_title(c, title_y_base, title_text, title_font, title_font_size)
    if is_draw_subtitle:
        draw_subtitle(c, subtitle_y_base, subtitle_font, subtitle_font_size, subtitle_labels)
    if is_draw_lines:
        draw_dashed_guides(c, y_base, num_grids)
    if is_draw_letters:
        y = letter_y_base    
        for i in range(len(letters_lowercase)):
            if i % 2 == 0:
                x = LEFT_MARGIN
            else:
                x = PAGE_WIDTH / 2 + 0.75 * letter_font_size

            for _ in range(letters_per_row):
                draw_letter(c, letters_uppercase[i], x, y, letter_font, letter_font_size + 2, False)
                x += 0.95 * letter_font_size
                draw_letter(c, letters_lowercase[i], x, y, letter_font, letter_font_size + 2, False)
                x += 0.95 * letter_font_size
            if i % 2 == 1:
                y -= grid_height
    c.save()
    print(f"Worksheet saved as: {filename}")

if __name__ == "__main__":
    generate_simple_1()
