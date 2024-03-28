#Collin's Button
#Collin can click this and it will randomly pick a pathfinder race and class and prestige class

import tkinter as tk
from tkinter import W, E
import random
from classListModule import classList, raceList, archetypemap

#definitions
def runTheProgram():
    

    race = random.choice(raceList)

    clas = random.choice(classList)
    
    arch = random.choice((archetypemap(clas)))

    print("Race: {}, Class: {}, Archetype: {}\n".format(race, clas, arch))
    text.insert(tk.INSERT, "Race: {}, Class: {}, Archetype: {}\n".format(race, clas, arch))

#GUI
master = tk.Tk()
master.title("Collin's Button")
master.configure(background = '#ccf2ff')

tk.Label(master, text="Hit Run for a random Pathfinder race, class, and prestige class.", anchor=E, background = '#ccf2ff').grid(row=0)

text = tk.Text(master)
text.grid(row=2, column=1)
#text.insert(tk.INSERT, ">>>")

tk.Button(master, text='Run', command=runTheProgram).grid(row=0, column=1, sticky=W, pady=4)
tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
tk.Button(master, text='Clear Text Box', command=text.delete(1.0,tk.END)).grid(row=3, column=1, sticky=W, pady=4) #clear button not working

tk.mainloop( )



