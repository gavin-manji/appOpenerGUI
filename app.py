# Name (Author of the Code): Gavin Manjitha Thawalampitiya

"""
Briefing : GUI/App which can open any other app or you can also use this GUI/app
as an App opening automating GUI, by providing file path locations by default)
"""

# tkinter - To create the GUI
# filedialog - To Pick Apps
# os - To run apps which are being added
import tkinter as tk
from tkinter import filedialog
import os


# root is holding the whole app/whole structure
root = tk.Tk()

# Creating a blank array as app
app = []

# Loading the text file
if os.path.isfile('Location Path Saver.txt'):
    with open('Location Path Saver.txt', 'r') as s:
        temporary = s.read()
        temporary = temporary.split('\n')
        # To remove/ ignore the blank lines
        app = [x for x in temporary if x.strip()]


# Function To open an app
def openApp():

    # Stopping the previously displayed file path being displayed twice in the frame when opening another file
    # x can be defined as the previously displayed file path, if opening another file again
    for x in frame.winfo_children():
        x.destroy()

    file = filedialog.askopenfilename(initialdir="/", title="Select",
                                      filetype=(("Executables", "*.exe"), ("All Files", "*.*")))

    # append the file to array named as app
    app.append(file)

    # for checking purposes - printing the file or app
    print(file)

    # Displaying the location address of the opened file in the frame when file is opened
    for i in app:
        label = tk.Label(frame, text=i, bg="yellow")
        label.pack()


# To run the selected/ opened apps
def appRunning():
    for i in app:
        os.startfile(i)


# To arrange/ modify the GUI using canvas
canvas = tk.Canvas(root, height=610, width=610, bg="#325ea1")

# To attach the canvas to root
canvas.pack()

# Adding a frame or a border to GUI
frame = tk.Frame(root, bg="white")

# Arranging the height, width and leaving space around(to make the frame centered)
frame.place(relwidth=0.7, relheight=0.7, relx=0.15, rely=0.15)

# Adding a button to open files and assigning a place for the button while arranging the size, colour of the button
fileOpen = tk.Button(root, text="Open", padx=10, pady=6, fg="white", bg="black", command=openApp)

# To attach the button to root and run
fileOpen.pack()

# Adding a button to run files and assigning a place for the button while arranging the size, colour of the button
appRun = tk.Button(root, text="Run", padx=10, pady=6, fg="white", bg="black", command=appRunning)

# To attach the button to root and run
appRun.pack()

# Opening the selected apps by default in the next time running (App opening automation)
for x in app:
    label = tk.Label(frame, text=x)
    label.pack()

# To run the whole structure which is the root
root.mainloop()

# To save/write location path of the opened app in a text file.
with open('Location Path Saver.txt', 'w') as s:
    for i in app:
        s.write(i + '\n')
