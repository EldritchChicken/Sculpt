from tkinter import Canvas, Tk
from PIL import Image, ImageTk
import pandas as pd


df = pd.read_excel("Limbs.xlsx")

#print the column names
print (df.columns)

#get the values for a given column
values = df['Effect 1'].values
print(values)
#get a data frame with selected columns
allcards = ['Col_1', 'Col_2', 'Col_3']
df_selected = df[FORMAT]


tkInstance = Tk()
canvas = Canvas(tkInstance, width = 640, height = 890, bg = "white")
canvas.pack()
canvas.bind()
tkInstance.mainloop()