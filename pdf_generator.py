#Noah McGehee 11/24/2023
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import utils

def create_pdf(file_path, content, image_path=None):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica", 12)

    if image_path:
        try:
            img = utils.ImageReader(image_path)
            img_width, img_height = img.getSize()

            if img_height > 0.2 * height:
                scale_factor = 0.2 * height / img_height
                img_width *= scale_factor
                img_height *= scale_factor

            x = (width - img_width) / 2
            y = height - img_height - 150
            c.drawInlineImage(image_path, x, y, width=img_width, height=img_height)
        except Exception as e:
            messagebox.showwarning("Image Error", f"Failed to load image: {e}")
    else:
        x, y = 100, height - 100

    text_object = c.beginText(x, y - 20)
    text_object.textLines(content)
    c.drawText(text_object)

    c.save()
