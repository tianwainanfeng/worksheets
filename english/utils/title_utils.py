#utils/title_utils.py
"""
# Function to add title
"""

import config as cfg


def draw_title(canvas, y_base, title_text, font="Helvetica-Bold", font_size=16):
    """
    Draws a centered title at the top of the page.

    Parameters:
    - canvas: ReportLab canvas object
    - y_base: starting y-coordinate for title
    - title_text: The string to display
    - font: Font name (default: Helvetica-Bold)
    - font_size: Font size (default: 16)
    """
    canvas.setFont(font, font_size)
    canvas.setFillColor(cfg.TITLE_FONT_COLOR)
    text_width = canvas.stringWidth(title_text, font, font_size) # measure the width (in points)

    x = cfg.PAGE_WIDTH / 2 - text_width / 2
    #y = cfg.PAGE_HEIGHT - cfg.TOP_MARGIN + (font_size / 2)
    y = y_base + (font_size / 2)

    canvas.drawString(x, y, title_text)


def draw_subtitle(canvas, y_base, font="Helvetica", font_size=12, labels = ["Name", "Date", "Days"], desired_field_width=100, min_field_width=60):
    """
    Draws a subtitle line with fields for Name, Date, and Days.

    Parameters:
    - canvas: ReportLab canvas object
    - y_base: starting y-coordinate for subtitle
    - font: font name
    - font_size: font size
    - labels: some info
    - desired_field_width: width of each underline field in points
    - min_field_width: minimum allowed field width before raising error
    """
    canvas.setFont(font, font_size)
    canvas.setFillColor(cfg.SUBTITLE_FONT_COLOR)
    
    label_strings = [f"{label}:" for label in labels]
    n_fields = len(labels)
    
    # Measure widths
    label_widths = [canvas.stringWidth(label + ":", font, font_size) for label in labels]
    total_label_width = round(sum(label_widths))

    # Remaining space for spacing between label-field pairs
    usable_width = cfg.PAGE_WIDTH - cfg.LEFT_MARGIN - cfg.RIGHT_MARGIN
    
    # Initial assumption: desired field width and even spacing
    total_spacing = usable_width - total_label_width - (n_fields * desired_field_width)
     
    if total_spacing < 0:
        # Adjust field width proportionally to make it fit
        shrink_ratio = usable_width / (total_label_width + n_fields * desired_field_width)
        field_width = max(desired_field_width * shrink_ratio, min_field_width)

        if field_width < min_field_width:
            raise ValueError("Cannot fit subtitle line within margins — too narrow.")
        total_spacing = usable_width - total_label_width - (n_fields * field_width)
    else:
        field_width = desired_field_width

    # Final spacing between fields
    spacing = int(total_spacing / (n_fields - 1)) if n_fields > 1 else 0

    # Starting x
    x = cfg.LEFT_MARGIN
    
    for label, label_width in zip(labels, label_widths):
        canvas.drawString(x, y_base, f"{label}:")
        x += label_width + 5  # 5pt gap between label and line
        canvas.line(x, y_base - font_size/2 + 2, x + field_width, y_base - font_size/2 + 2) 
        x += field_width + spacing - 5
