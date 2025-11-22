from tkinter import *
from PIL import Image, ImageTk, ImageDraw
import pandas as pd
from io import BytesIO



df = pd.read_excel("LimbsConditionalTest.xlsx")


names = df['Name'].values
types = df['Type'].values
charges = df['Charges'].values
type1 = df['Effect 1 Type'].values
type2 = df['Effect 2 Type'].values
type3 = df['Effect 3 Type'].values
title1 = df['Effect 1 Title'].values
title2 = df['Effect 2 Title'].values
title3 = df['Effect 3 Title'].values
effect1 = df['Effect 1'].values
effect2 = df['Effect 2'].values
effect3 = df['Effect 3'].values

numcards = len(names)

root = Tk()
root.title("Test Card")
cv = Canvas(root, width = 750, height = 1050, bg = "white")
cv.pack()


pil_image = Image.open("Images/Templates/LimbBorderV4.png")
tk_image = ImageTk.PhotoImage(pil_image)
cv.create_image(0,0,anchor=NW,image=tk_image)

cv.bind()


cv.update()

#cv.postscript(file="file_name.ps", colormode='color')
ps = cv.postscript(colormode='color')
im = Image.open(BytesIO(bytes(ps,'ascii')))
im.save('Output/testCard.png')

root.mainloop()

