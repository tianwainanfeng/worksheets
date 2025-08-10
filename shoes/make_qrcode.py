from PIL import Image, ImageDraw, ImageFont
import qrcode

url = "https://mybreathtaking.com/view.php?dir=worksheets&file=shoes_table.pdf"

# --- 生成不带文字的二维码 ---
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
img.save("outputs/shoes_table_qr.png")  # 保存不带文字的二维码

# --- 生成带文字的二维码 ---
draw = ImageDraw.Draw(img)
text = "扫码下载 PDF文件"
font_size = 40

try:
    font = ImageFont.truetype("/System/Library/Fonts/STHeiti Medium.ttc", font_size)
except Exception as e:
    print("加载字体失败，使用默认字体", e)
    font = ImageFont.load_default()

bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

new_img_height = img.height + text_height + 20
new_img = Image.new("RGB", (img.width, new_img_height), "white")
new_img.paste(img, (0, 0))

draw = ImageDraw.Draw(new_img)
text_x = (img.width - text_width) // 2
text_y = img.height + 10
draw.text((text_x, text_y), text, fill="black", font=font)

new_img.save("outputs/shoes_table_qr_with_text.png")  # 保存带文字的二维码

