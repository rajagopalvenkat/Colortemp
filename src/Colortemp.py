##############################  Colortemp  ############################################

#	Version 1.0
#	V.Rajagopal, 2015
#	Copyleft, RV, 2015-16
#	Send feedback to rajagopalvenkat@outlook.com

######################################################################################


import Tkinter as Tk
import os

top = Tk.Tk()	#Parent Window
top.wm_title("Redshift Control")
ison=0

text=Tk.Label(top, text="Redshift Control")
text.pack()
text.place(x=115, y=10)


###############################  ON AND OFF FUNCTIONS   ##############################

def enable():
	global ison
	ison=1
	os.system("gtk-redshift -O 5500")
	slide.set(1000)

def disable():
	global ison
	os.system("gtk-redshift -x")
	ison=0
	slide.set(0)

#####################################################################################

###############################  COLOR LEVEL SETTING   ##############################

def settempvlow():
	global ison
	if ison==1:
		os.system("gtk-redshift -O 5500")
		slide.set(1000)

def settemplow():
	global ison
	if ison==1:
		os.system("gtk-redshift -O 4700")
		slide.set(1800)

def settempmed():
	global ison
	if ison==1:
		os.system("gtk-redshift -O 4000")
		slide.set(2500)

def settemphigh():
	global ison
	if ison==1:
		os.system("gtk-redshift -O 3400")
		slide.set(3100)

def settempvhigh():
	global ison
	if ison==1:
		os.system("gtk-redshift -O 3000")
		slide.set(3500)

def settempnight():
	global ison
	if ison==1:
		os.system("gtk-redshift -O 2500")
		slide.set(4000)

#######################################################################################		

on=Tk.Button(top, text="ON", command= enable)			#ON button
off=Tk.Button(top, text="OFF",  command= disable)		#OFF button

on.pack()
off.pack()

on.place(x=230, y=150)									#positioning on / off buttons
off.place(x=280, y=150)


##################################      PRESETS       #################################

VLow=Tk.Button(top, text="Mild", command= settempvlow)
Low=Tk.Button(top, text="Low", command= settemplow)
Med=Tk.Button(top, text="Moderate", command= settempmed)
High=Tk.Button(top, text="High", command= settemphigh)
VHigh=Tk.Button(top, text="Ultra", command= settempvhigh)
Night=Tk.Button(top, text="Night", command= settempnight)

VLow.pack()
Low.pack()
Med.pack()
High.pack()
VHigh.pack()
Night.pack()

VLow.place(x=45, y=75, height=30, width=70)
Low.place(x=130, y=75, height=30, width=70)
Med.place(x=215, y=75, height=30, width=70)
High.place(x=45, y=110, height=30, width=70)
VHigh.place(x=130, y=110, height=30, width=70)
Night.place(x=215, y=110, height=30, width=70)

######################################################################################



######################################    SLIDER   ###################################



def setcolor(int):
	num=slide.get()
	global ison
	if ison==1:
		os.system("gtk-redshift -O " + str(6500-num))

slide=Tk.Scale(top, orient=Tk.HORIZONTAL, length=200, showvalue=0, from_=0, to=4000, command=setcolor)
slide.place(x=65, y=35)

#####################################################################################

top.geometry("350x200+358+234")							#root window

top.mainloop()
