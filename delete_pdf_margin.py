import fitz
format_ = '2026'
if format_=='old':
    #old format
    doc = fitz.open(r"C:\Users\kupfe\Downloads\18371_25.pdf")
    for k,page in enumerate(doc[3:]):
        # Define rectangle: (x0, y0, x1, y1)
        if k % 2 ==0:
            rect = fitz.Rect(0, 0 , 83, 700)
        else:
            rect = fitz.Rect(430, 0, 515, 700)
        page.draw_rect(rect, color=None, fill=(1, 1, 1))  # white fill
    doc.save(r"C:\Users\kupfe\Downloads\18371_25_mod.pdf")

elif format_=='new':

    #new format
    doc = fitz.open(r"C:\Users\kupfe\Downloads\18282_2026.pdf")
    for k,page in enumerate(doc[3:]):
        # Define rectangle: (x0, y0, x1, y1)
        rect1 = fitz.Rect(0, 0 , 83, 700)
        rect2 = fitz.Rect(430, 0, 515, 700)
        page.draw_rect(rect1, color=None, fill=(1, 1, 1))  # white fill
        page.draw_rect(rect2, color=None, fill=(1, 1, 1))  # white fill
    doc.save(r"C:\Users\kupfe\Downloads\18282_2026_mod.pdf")

else:

    doc = fitz.open(r"C:\Users\kupfe\Downloads\18371_2026.pdf")
    for k,page in enumerate(doc):
        # Define rectangle: (x0, y0, x1, y1)
        rect1 = fitz.Rect(0, 0 , 83, 900)
        rect2 = fitz.Rect(550, 0, 625, 900)
        page.draw_rect(rect1, color=None, fill=(1, 1, 1))  # white fill
        page.draw_rect(rect2, color=None, fill=(1, 1, 1))  # white fill
    doc.save(r"C:\Users\kupfe\Downloads\18371_2026_mod.pdf")




