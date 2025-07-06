# config.py
"""
# Global configuration
"""

# ReportLab: a powerful and widely used Python library for generating PDFs programmatically
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import black, gray, Color

"""
# ============================================================
#                      Page Geometry
# ============================================================
"""

# letter = (612.0, 792.0)  # in points (72 points/inch)
PAGE_WIDTH, PAGE_HEIGHT = letter

TOP_MARGIN = 72.0
BOTTOM_MARGIN = 72.0
LEFT_MARGIN = 72.0
RIGHT_MARGIN = 72.0

"""
# ============================================================
#                      Title Style
# ============================================================
"""

#TITLE_FONT = "Helvetica-Bold"
TITLE_FONT = "Helvetica"
TITLE_FONT_SIZE = 16
TITLE_FONT_COLOR = Color(0., 0., 0., alpha=1.0)  # pure black, fully opaque

SUBTITLE_FONT = "Helvetica"
SUBTITLE_FONT_SIZE = 12
SUBTITLE_FONT_COLOR = Color(0., 0., 0., alpha=1.0)  # pure black, fully opaque

"""
# ============================================================
#                      Line Style
# ============================================================
"""

LINE_OFFSETS = [0, 10, 20, 30]  # base, mid, ascender, descender
GRID_SPACE = 15 # each grid contains four lines

# line color: dashed guide line Y-offsets from each writing row
LINE_COLOR = Color(0.4, 0.4, 0.4, alpha=0.4)  # semi-transparent gray

# dash line
LINE_DASH = [3, 2] # 3 on, 2 off

"""
# ============================================================
#                      Letter Style
# ============================================================
"""

LETTER_FONT = "Helvetica"
#LETTER_FONT = "Times-Roman"
LETTER_FONT_SIZE = 30
LETTER_FONT_COLOR = Color(0., 0., 0., alpha=1.0)  # pure black, fully opaque

LETTERS_PER_ROW = 4

