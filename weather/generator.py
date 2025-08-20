# generator.py

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
import os

from PIL import Image as PILImage, ImageEnhance, ImageOps
import io

def process_image(img_path):
    with PILImage.open(img_path) as im:
        im = im.convert("RGB")  # 确保是 RGB
        # 示例：降低饱和度
        enhancer = ImageEnhance.Color(im)
        im = enhancer.enhance(0.3)  # 0=黑白, 1=原始颜色
        # 提亮
        enhancer = ImageEnhance.Brightness(im)
        im = enhancer.enhance(1.1)
        # 可以加别的效果，比如加浅灰蒙版
        overlay = PILImage.new('RGB', im.size, (230, 230, 230))
        im = PILImage.blend(im, overlay, 0.1)

        # 保存到内存缓冲区
        img_buffer = io.BytesIO()
        im.save(img_buffer, format="JPEG")
        img_buffer.seek(0)
        return img_buffer

# font
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))

# output
pdf_path = "outputs/weather_table.pdf"

# ===== Page geometry (adjust margins here) =====
LEFT_MARGIN = 50
RIGHT_MARGIN = 50
TOP_MARGIN = 20
BOTTOM_MARGIN = 20
# ==============================================

# styles
styles = getSampleStyleSheet()
style_normal = styles["Normal"]
style_normal = ParagraphStyle(
    'English',
    parent=style_normal,
    fontSize=9,
    leading=10
)
style_chinese = ParagraphStyle(
    'Chinese',
    parent=style_normal,
    fontName='STSong-Light',
    fontSize=9,
    alignment=1,  # 居中
    leading = 10
)
style_title = ParagraphStyle(
    'TitleChinese',
    parent=styles["Title"],
    fontName='STSong-Light',
    fontSize=16,
    alignment=1,  # 居中
    spaceAfter=10
)

# 表格下方的说明文字样式（小号、灰色）
style_note = ParagraphStyle(
    'Note',
    parent=style_normal,
    fontName='STSong-Light',
    fontSize=6,
    leading=7,
    textColor=colors.grey,
    spaceBefore=4,
    alignment=1  
)

# data（英文名, 中文名, 图片文件名, 备注）
weather_data = [
    ("Sunny", "晴天", "sunny.jpeg", "晴朗"),
    ("Cloudy", "多云", "cloudy.jpeg", "有很多云，晴阴之间"),
    ("Overcast", "阴天", "overcast.jpeg", "厚云层，可能会下雨"),
    ("Rainy", "下雨", "rainy.jpeg", "小雨/中雨/大雨"),
    ("Drizzle", "毛毛雨", "drizzle.jpeg", "小而密集的雨点"),
    ("Shower", "阵雨", "shower.jpeg", "短时雨"),
    ("Thunderstorm", "雷雨", "thunderstorm.jpeg", "雷声闪电伴随大雨"),
    ("Snowy", "下雪", "snowy.jpeg", "雪花飘落"),
    ("Blizzard", "暴风雪", "blizzard.jpeg", "大雪+大风"),
    ("Sleet", "雨夹雪", "sleet.jpeg", "雨和雪同时降落"),
    ("Hail", "冰雹", "hail.jpeg", "冰块随雨降落"),
    ("Foggy", "有雾", "foggy.jpeg", "有雾气，视线模糊"),
    ("Misty", "薄雾", "misty.jpeg", "较轻微的雾气"),
    ("Frost", "霜冻", "frost.jpeg", "低温下地面结晶"),
    ("Windy", "大风", "windy.jpeg", "风力较强"),
    ("Sandstorm", "沙尘暴", "sandstorm.jpeg", "风扬起大量沙尘"),
    ("Lightning", "闪电", "lightning.jpeg", "电流放电现象"),
    ("Hurricane", "飓风", "hurricane.jpeg", "大西洋/东太平洋强气旋"),
    ("Typhoon", "台风", "typhoon.jpeg", "西太平洋强气旋"),
    ("Tornado", "龙卷风", "tornado.jpeg", "旋转空气柱，漏斗状"),
]

# header
table_data = [["English Name", "中文名称", "示例图片", "备注"]]

# images
image_folder = "images"

# 遍历数据前，先按英文名排序
weather_data_sorted = sorted(weather_data, key=lambda x: x[0])

# 遍历鞋子数据
for eng, chi, img_file, remark in weather_data_sorted:
    img_path = os.path.join(image_folder, img_file)
    if os.path.exists(img_path):
        processed_buffer = process_image(img_path)
        img = Image(processed_buffer, width=40, height=30)
    else:
        img = Paragraph("No Image", style_normal)
    table_data.append([
        Paragraph(eng, style_normal),
        Paragraph(chi, style_chinese),
        img,
        Paragraph(remark, style_chinese)
    ])

# 创建表格
table = Table(table_data, colWidths=[100, 100, 80, 180])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('TOPPADDING', (0, 0), (-1, -1), 2),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 2),

    ('FONTNAME', (1, 0), (1, -1), 'STSong-Light'),
    ('FONTNAME', (2, 0), (2, -1), 'STSong-Light'),
    ('FONTNAME', (3, 0), (3, -1), 'STSong-Light'),

]))

# 生成 PDF
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=LEFT_MARGIN,
    rightMargin=RIGHT_MARGIN,
    topMargin=TOP_MARGIN,
    bottomMargin=BOTTOM_MARGIN
)

story = [
    Paragraph("常见天气中英文对照表", style_title), # 标题
    table,
    Paragraph("注：示例图片均来自网络。", style_note)
]

doc.build(story)

print(f"PDF 已生成: {pdf_path}")

