#import tkinter which is the standard GUI library in python
from tkinter import *

#importing the calendar module
import calendar

#initializing tkinter
root = Tk()

#Title of GUI
root.title('My calendar!')

#Year of the calendar to be shown
year = 2021

#Sorting 2021 calendar inside myCal
myCal = calendar.calendar(2021)

#Showing calendar data using label widget
cal_year = Label(root, text=myCal, font='Consolas 10 bold')

#Packing the label widget
cal_year.pack()

#Running the program in read state
root.mainloop()

