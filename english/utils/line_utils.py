# utils/line_utils.py
"""
# Functions to draw lines
"""

import config as cfg


def draw_dashed_guides(canvas, y_base, n_grids):
    """
    Draws dashed guide lines for handwriting grids.

    Parameters:
    - canvas: reportlab canvas object: (0, 0) at the bottom-left corner of the page
    - y_base: starting y-coordinate for the first grid
    - n_grids: number of grid rows to draw
    """
    for i in range(n_grids):
        grid_y_base = y_base - i * (cfg.GRID_SPACE + cfg.LINE_OFFSETS[-1] - cfg.LINE_OFFSETS[0])
        for offset in cfg.LINE_OFFSETS:
            y = grid_y_base - offset
            canvas.setStrokeColor(cfg.LINE_COLOR)
            canvas.setDash(cfg.LINE_DASH)
            canvas.line(cfg.LEFT_MARGIN, y, cfg.PAGE_WIDTH - cfg.RIGHT_MARGIN, y)
    canvas.setDash()  # Reset dash style
