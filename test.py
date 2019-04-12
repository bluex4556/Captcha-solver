from PIL import Image
from pathlib import Path
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


datafolder = Path('captcha/')
filename= "captcha"
fileext = ".bmp"

for i in range(1,11):
    fileloc = datafolder/(filename + str(i) + fileext)

    img = Image.open(fileloc)
    pix = img.load()
    for col in range(1, img.width-2):
        for row in range(1, img.height-2):
            # print(pix[col,row], end=" ")
            if(pix[col,row]==1):
                if(pix[col-1,row] == 0 and pix[col+1,row] == 0):
                    img.putpixel((col, row), 0)
                elif(pix[col,row-1] == 0 and pix[col,row+1] == 0):
                    img.putpixel((col, row), 0)

    print(pytesseract.image_to_string(img,config="-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMONPQRSTUVWXYZ -psm 6"))


# img.save("etest.bmp")
# img1 = Image.fromarray(pix)
# img1.save("output.png")

# greyscaleimg = img.convert('1')
# greyscaleimg.save('test.bmp')
