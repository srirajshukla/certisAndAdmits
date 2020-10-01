import numpy as np
import pandas as pd
import qrcode
import cv2 as cv
import os

data = pd.read_excel('data.xlsx', header=0)
print(cv.__version__)

# creating the certificate
font = cv.FONT_HERSHEY_SIMPLEX
names = data['Name']
for name in names:
    # reading the format from the given location, change this as per need
    format = cv.imread('./format/certifFormat.png')
    # place the required text, here 2 is the size of the font, (0, 255, 0) is the color
    # (400, 380) is the starting coordinate of written text.
    cv.putText(format, name, (400, 380), font, 2, (0, 255, 0), 2, cv.LINE_AA)
    cv.imwrite('./gencert/'+name+'.png', format)


# creating the admit cards
for index, row in data.iterrows():
    format = cv.imread('./format/admitformat.png')
    cv.putText(format, str(row['UID']), (170, 80), font, 1, (0, 0, 0), 3, cv.LINE_AA)
    cv.putText(format, row['Name'], (410, 45), font, 1, (0, 0, 0), 1, cv.LINE_AA)
    cv.putText(format, row['Branch'], (420, 85), font, 1, (0, 0, 0), 1, cv.LINE_AA)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=7,
        border=2,
    )
    qr.add_data(row['Transaction Id'])
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(str(index)+".png")
    i = cv.imread(str(index)+".png")
    format[190:190+175, 975:975+175] = i
    os.remove(str(index)+".png")
    cv.imwrite('./genadmit/' + row['Name'] + '.png', format)

