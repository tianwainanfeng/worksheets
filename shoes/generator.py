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
pdf_path = "outputs/shoes_table.pdf"

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
shoes_data = [
    ("Ballet flats", "芭蕾平底鞋", "ballet_flats.jpeg", "女士平底鞋，舒适轻便"),
    ("Dress shoes", "正装鞋 / 皮鞋", "dress.jpeg", "搭配西装、礼服"),
    ("Loafers", "乐福鞋", "loafers.jpeg", "一脚蹬便鞋"),
    ("Slippers", "拖鞋", "slippers.jpeg", "室内穿着"),
    ("Basketball shoes", "篮球鞋", "basketball.jpeg", "支撑脚踝，适合篮球运动"),
    ("Flip-flops", "人字拖", "flip-flops.jpeg", "夏日、沙滩穿着"),
    ("Running shoes", "跑鞋", "running.jpeg", "跑步缓震透气"),
    ("Sneakers", "运动鞋", "sneakers.jpeg", "日常运动或休闲"),
    ("Boots", "靴子", "boots.jpeg", "短靴、中靴或高筒靴"),
    ("Golf shoes", "高尔夫鞋", "golf.jpeg", "草地防滑钉底"),
    ("Sandals", "凉鞋", "sandals.jpeg", "夏季透气鞋款"),
    ("Soccer cleats", "足球鞋", "soccer.jpeg", "鞋底有钉，适合草地"),
    ("Climbing shoes", "攀岩鞋", "climbing.jpeg", "紧贴脚型，增加摩擦力"),
    ("High heels", "高跟鞋", "high_heel.jpeg", "女士常用高跟设计"),
    ("Skating shoes", "滑冰鞋", "skating.jpeg", "冰上或轮滑运动"),
    ("Swimming shoes", "游泳鞋 / 溯溪鞋", "swimming.jpeg", "水中或湿滑环境防护")
]

# header
table_data = [["English Name", "中文名称", "示例图片", "备注"]]

# images
image_folder = "images"

# 遍历鞋子数据前，先按英文名排序
shoes_data_sorted = sorted(shoes_data, key=lambda x: x[0])

# 遍历鞋子数据
for eng, chi, img_file, remark in shoes_data_sorted:
    img_path = os.path.join(image_folder, img_file)
    if os.path.exists(img_path):
        processed_buffer = process_image(img_path)
        img = Image(processed_buffer, width=40, height=38)
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
    Paragraph("常见鞋子类别中英文名字表", style_title), # 标题
    table,
    Paragraph("注：示例图片均来自网络。", style_note)
]

doc.build(story)

print(f"PDF 已生成: {pdf_path}")

