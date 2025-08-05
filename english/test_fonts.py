# test_fonts.py

import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# Constants
FONT_DIR = "fonts"
OUTPUT_DIR = "outputs"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "test_fonts.pdf")

# Font paths
FONTS = {
    "Emoji": os.path.join(FONT_DIR, "NotoColorEmoji.ttf"),
    "Roboto": os.path.join(FONT_DIR, "Roboto-Regular.ttf"),
}

# Track font registration status
registered_fonts = {}

def register_font(name, path):
    try:
        pdfmetrics.registerFont(TTFont(name, path))
        registered_fonts[name] = True
        print(f"✅ {name} font registered successfully")
    except Exception as e:
        registered_fonts[name] = False
        print(f"❌ Failed to register '{name}' font: {e}")
        if name == "Emoji":
            print("ℹ️  NotoColorEmoji.ttf is an OpenType color font and not supported by ReportLab.")

def create_pdf(output_path):
    c = canvas.Canvas(output_path, pagesize=A4)
    
    if registered_fonts.get("Roboto"):
        c.setFont("Roboto", 20)
        c.drawString(100, 750, "Hello Roboto")

    if registered_fonts.get("Emoji"):
        c.setFont("Emoji", 20)
        c.drawString(100, 700, "Emoji test: 🍎 🐱 🚀")

    c.save()
    print(f"📄 PDF saved at: {output_path}")

def main():
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Register fonts
    for font_name, font_path in FONTS.items():
        register_font(font_name, font_path)

    # Generate PDF
    create_pdf(OUTPUT_FILE)

if __name__ == "__main__":
    main()

