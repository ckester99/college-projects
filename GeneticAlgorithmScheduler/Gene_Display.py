from tkinter import *
import Genetic

root = Tk()
g = Genetic.Genetic()



def generate10():

	light.config(bg = "red")
	for _ in range(10):
		g.generate()
	light.config(bg = "green")
	avgLabel.config(text = "Curr Avg: " + str(g.avgFit[g.genNum]))
	bestLabel.config(text = "Curr Best: " + str(g.bestFit[g.genNum]))
	
def generate100():

	light.config(bg = "red")
	for _ in range(100):
		g.generate()
	light.config(bg = "green")
	avgLabel.config(text = "Curr Avg: " + str(g.avgFit[g.genNum]))
	bestLabel.config(text = "Curr Best: " + str(g.bestFit[g.genNum]))
	
def generateX(x):

	light.config(bg = "red")
	for _ in range(x):
		g.generate()
	light.config(bg = "green")	
	avgLabel.config(text = "Curr Avg: " + str(g.avgFit[g.genNum]))
	bestLabel.config(text = "Curr Best: " + str(g.bestFit[g.genNum]))
	
def viewBest():
	displaySched(g.genNum)

def viewOld():
	displaySched(g.genNum-1)

def displaySched(genNum):
	global dispFrame
	global g
	dispFrame.destroy()
	dispFrame = Frame(root)
	sched = g.best[genNum]
	
	for x in range(len(g.classrooms)):	#Labels for classrooms
		Label(dispFrame, text = g.classrooms[x], relief = SUNKEN, width = 18).grid(row = 1, column = x+2, sticky = "W")
	
	for x in range(len(g.times)):	#Labels for times
		Label(dispFrame, text = g.times[x], relief = SUNKEN, width = 5, height = 2).grid(row = x+2, column = 1, sticky = "W")
		
	r,c = 2,2
	for time in g.times:
		for room in g.classrooms:
			tempS = ""
			flag = False
			for x in sched[time][room]:
				if x != 0:
					if flag == True:
						tempS = tempS + x[0] + " " + x[1] + " "  + x[2]
					else:
						tempS = tempS + x[0] + " " + x[1] + " "  + x[2] + "\n"
					flag = True
			Label(dispFrame, text = tempS, relief = SUNKEN, width = 18, height = 2).grid(row = r, column = c)
			c +=1
		r +=1
		c = 2
	#print(g.best[genNum])
	dispFrame.pack()
	

#////////////////dropdown menu////////////////
menu = Menu(root)
root.config(menu=menu)

control = Menu(menu)	#CONTROL MENU
control.add_command(label = "10 generations", command = generate10)
control.add_command(label = "100 generations", command = generate100)
#control.add_command(label = "reset", command = reset)
control.add_command(label = "exit", command = quit)

view = Menu(menu)	#VIEW MENU
view.add_command(label = "overall best", command = viewBest)
view.add_command(label = "next best", command = viewOld)

menu.add_cascade(label = "Control", menu = control)
menu.add_cascade(label = "View", menu = view)

#//////////////////frames/////////////////
dataFrame = Frame(root)
dataFrame.pack()

var = IntVar()
light = Label(dataFrame, bg = "green", width = 3)
#entryLabel = Label(dataFrame, text = "Enter number of generations" )
genEntry = Entry(dataFrame, textvariable = var)
genEntry.insert(0,"0")

avgLabel = Label(dataFrame, text = "Curr Avg: " + str(g.avgFit[g.genNum]), relief = SUNKEN)
bestLabel = Label(dataFrame, text = "Curr Best: " + str(g.bestFit[g.genNum]), relief = SUNKEN)
genButton = Button(dataFrame, text = "Generate", command = lambda: generateX(var.get()))

light.pack(side = RIGHT)
#entryLabel.pack(side = LEFT)
genEntry.pack(side = LEFT)
genButton.pack(side = LEFT)
bestLabel.pack(side = RIGHT)
avgLabel.pack(side = RIGHT)

dispFrame = Frame(root)
dispFrame.pack()
Label(dispFrame, text = "Use 'Control' to generate populations").pack()


root.geometry("500x400")
root.title("GUI")
root.mainloop()
