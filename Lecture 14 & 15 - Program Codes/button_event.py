from tkinter import *
from tkinter import ttk

def button_pressed_handler(event):
    print(event.widget["text"] + " pressed")

def button_released_handler(event):
    print(event.widget["text"] + " released")

def main():
    root = Tk()

    # Put the main window in the center of the screen
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))
    # The geometry() method defines the width, height and coordinates of top left corner of the frame
    # as below (all values are in pixels): top.geometry("widthxheight+XPOS+YPOS")

    # attach button2 to root window
    button1 = ttk.Button(root, text="Button 1")
    button2 = ttk.Button(root, text="Button 2")

    # create a style for the button
    button_style1 = ttk.Style()
    button_style2 = ttk.Style()

    # configure button styles called button1 and button2
    button_style1.configure("button1.TButton", font=("Times New Roman", 20))
    button_style2.configure("button2.TButton", font=("Times New Roman", 20))

    # set button1 and button2 to have the "button1" and "button2" styles
    button1.configure(style="button1.TButton")
    button2.configure(style="button2.TButton")

    # button1 and button2 are impacted
    button1.bind_class("TButton", "<Button-1>", button_pressed_handler)  # One Event - Button Clicked
    button1.bind_class("TButton", "<ButtonRelease-1>", button_released_handler)  # One Event - Button Released

    # display the buttons using pack layout
    button1.pack(side=TOP)
    button2.pack(side=BOTTOM)

    root.mainloop()

if __name__ == "__main__":
    main()