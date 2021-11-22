from tkinter import *
from tkinter import ttk
from tkinter import font


def enter_relese_entry_event_handler(event):
    print("Text entered = " + event.widget.get())

def combobox_handler(event):
    print(event.widget["text"] + "Selected = " + str(event.widget.get()))
# prints out the state of the radio button for update column
def radio_button1_handler(event):
    print("Receive updates = " + event.widget["text"])

# prints out the state of the radio button for notification column
def radio_button2_handler(event):
    print("Receive emails = " + event.widget["text"]) 

# prints out the state of the check buttons
def check_button_handler(event):
    print(event.widget["text"] + " is Selected") 

# text will print on console after clicking enter
def enter_release_text_handler(event):
    print("Text entered = \n" + event.widget.get("1.0", END))

# prints out the state of the button once clicked
def button_pressed_handler(event):
    print(event.widget["text"] + " clicked")


def main():
    root = Tk()
    root.resizable(width=True, height=True)
    # Put the main window in the center of the screen
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth)
    positionDown = int(root.winfo_screenheight() / 3 - windowHeight / 2)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown)) 

    # The geometry() method defines the width, height and coordinates of top left corner of the frame
    # as below (all values are in pixels): top.geometry("widthxheight+XPOS+YPOS")
    
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    # root.columnconfigure(1, weight=1)

    # sticky -> means widget can be places or stretched within the limits of its bounding area
    # highlightcolor − Foreground color of the highlight region
    # highlightbackground − Background color of the highlight region
    top_frame = Frame(root, highlightcolor="pink", highlightbackground="pink",  highlightthickness=5)

    # place frame on top on root
    top_frame.grid(row=0, sticky=N+S+E+W)

    top_frame.rowconfigure(0, weight=1)
    top_frame.rowconfigure(1, weight=1)
    top_frame.rowconfigure(2, weight=1)
    top_frame.rowconfigure(3, weight=1)
    top_frame.rowconfigure(4, weight=1)
    top_frame.rowconfigure(5, weight=1)

    top_frame.columnconfigure(0, weight=1)
    top_frame.columnconfigure(1, weight=1)

    # attach all the labels and entries to the top frame of root
    label1 = ttk.Label(top_frame, text="User Name:", font=font.Font(family="Times New Roman", size=12))
    label1.grid(row=0, sticky=N+W)
    label2 = ttk.Label(top_frame, text="First Name:", font=font.Font(family="Times New Roman", size=12))
    label2.grid(row=1, sticky=N+W)
    label3 = ttk.Label(top_frame, text="Last Name:", font=font.Font(family="Times New Roman", size=12))
    label3.grid(row=2, sticky=N+W)
    label4 = ttk.Label(top_frame, text="Password:", font=font.Font(family="Times New Roman", size=12))
    label4.grid(row=3, sticky=N+W)
    label5 = ttk.Label(top_frame, text="Favorite Color:", font=font.Font(family="Times New Roman", size=12))
    label5.grid(row=4, sticky=N+W)
    label6 = ttk.Label(top_frame, text="Account Options:", font=font.Font(family="Times New Roman", size=12))
    label6.grid(row=5, column=0, sticky=N+W)
    label7 = ttk.Label(top_frame, text="Sports (like to watch):", font=font.Font(family="Times New Roman", size=12))
    label7.grid(row=5, column=1, sticky=N+E)
    
    entry1 = ttk.Entry(top_frame)
    entry2 = ttk.Entry(top_frame)
    entry3 = ttk.Entry(top_frame)
    entry4 = ttk.Entry(top_frame)

    entry1.grid(row=0, column=1, sticky=N+S+W+E)
    entry2.grid(row=1, column=1, sticky=N+S+W+E)
    entry3.grid(row=2, column=1, sticky= N+S+W+E)
    entry4.grid(row=3, column=1, sticky=N+S+W+E)

    # click on enter to call the event handler
    entry1.bind("<KeyRelease-Return>", enter_relese_entry_event_handler)
    entry2.bind("<KeyRelease-Return>", enter_relese_entry_event_handler)
    entry3.bind("<KeyRelease-Return>", enter_relese_entry_event_handler)
    entry4.bind("<KeyRelease-Return>", enter_relese_entry_event_handler)

    combo_box1 = ttk.Combobox(top_frame)
    combo_box1.grid(row=4, column=1, sticky=N+S+E+W)
    combo_box1.state(["readonly"])
    combo_box1["values"] = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet", "Pink", "White", "Black"]
    combo_box1.current(0)

    # The combobox widgets generates a <<ComboboxSelected>> virtual event
    # WHEN the user selects an element from the list of values.
    combo_box1.bind("<<ComboboxSelected>>", combobox_handler) # Select one of the choices to call the handler

    mid_frame = Frame(root, highlightcolor="cyan", highlightbackground="cyan",  highlightthickness=5)  

    mid_frame.grid(row=6, sticky=N+S+E+W)

    mid_frame.rowconfigure(6, weight=1)
    mid_frame.rowconfigure(7, weight=1)

    mid_frame.columnconfigure(0, weight=1)
    mid_frame.columnconfigure(1, weight=1)

    mid_frame_left = Frame(mid_frame, highlightcolor="orange", highlightbackground="orange",  highlightthickness=5)
    mid_frame_left.grid(row=6, column=0, sticky=N+W)

    mid_frame_left.rowconfigure(0, weight=1)
    mid_frame_left.rowconfigure(1, weight=1)

    mid_frame_left.columnconfigure(0, weight=1)
    mid_frame_left.columnconfigure(1, weight=1)

    label_updates = ttk.Label(mid_frame_left, text="Updates:", font=font.Font(family="Times New Roman", size=10))
    label_updates.grid(row=6, column=0, sticky=N+W) #update column

    label_notif = ttk.Label(mid_frame_left, text="Notification Emails:", font=font.Font(family="Times New Roman", size=10))
    label_notif.grid(row=6, column=1, sticky=E) #email notification column

    update_control = IntVar()
    update_control.set(0)
    email_control = IntVar()
    email_control.set(0)
    
    
    radio_button1 = ttk.Radiobutton(mid_frame_left, value= 'Yes', variable=update_control, text="Yes") # After
    radio_button1.bind("<Button-1>", radio_button1_handler) # Before and During

    radio_button2 = ttk.Radiobutton(mid_frame_left, value='Yes', variable=email_control, text="Yes") # After
    radio_button2.bind("<Button-1>", radio_button2_handler) # Before and During

    radio_button3 = ttk.Radiobutton(mid_frame_left, value='No', variable=update_control, text="No") # After
    radio_button3.bind("<Button-1>", radio_button1_handler) # Before and During calling the event handler 

    radio_button4 = ttk.Radiobutton(mid_frame_left, value='No', variable=email_control, text="No") # After
    radio_button4.bind("<Button-1>", radio_button2_handler) # Before and During calling the event handler 

    radio_button1.grid(row=7, sticky= N+W)
    radio_button2.grid(row=7, column= 1, sticky= N+W)
    radio_button3.grid(row=8, sticky= N+W)
    radio_button4.grid(row=8, column=1, sticky= N+W)

    mid_frame_right = Frame(mid_frame, highlightcolor="green", highlightbackground="green",  highlightthickness=5)
    mid_frame_right.grid(row=6, column= 1, sticky=N+E)

    mid_frame_right.rowconfigure(0, weight=1)
    mid_frame_right.rowconfigure(1, weight=1)

    mid_frame_right.columnconfigure(0, weight=1)
    mid_frame_right.columnconfigure(1, weight=1)

    label_empty = ttk.Label(mid_frame_right, text="", font=font.Font(family="Times New Roman", size=10))
    label_empty.grid(row=6, column=1, sticky=N+E)

    control1 = IntVar()
    control1.set(0)

    control2 = IntVar()
    control2.set(0)

    control3 = IntVar()
    control3.set(0)

    control4 = IntVar()
    control4.set(0)

    check_button1 = ttk.Checkbutton(mid_frame_right, variable=control1, text="Baseball") # After
    check_button1.bind("<Button-1>", check_button_handler) # Before and During calling the event handler 

    check_button2 = ttk.Checkbutton(mid_frame_right, variable=control2, text="Basketball") # After
    check_button2.bind("<Button-1>", check_button_handler) # Before and During calling the event handler 

    check_button3 = ttk.Checkbutton(mid_frame_right, variable=control3, text="Football") # After
    check_button3.bind("<Button-1>", check_button_handler) # Before and During calling the event handler 

    check_button4 = ttk.Checkbutton(mid_frame_right, variable=control4, text="Hockey") # After
    check_button4.bind("<Button-1>", check_button_handler) # Before and During calling the event handler 

    check_button1.grid(row=7, column= 0)
    check_button2.grid(row=7, column= 1, sticky=W)
    check_button3.grid(row=8, column= 0)
    check_button4.grid(row=8, column=1, sticky=W)

    # Create the text frame on root window
    text_frame = Frame(root, highlightcolor="red", highlightbackground="red",  highlightthickness=5)  

    text_frame.grid(row=9, sticky=N+S+E+W)

    text_frame.rowconfigure(9, weight=1)
    # mid_frame.rowconfigure(7, weight=1)

    text_frame.columnconfigure(0, weight=1)
    # text_frame.columnconfigure(1, weight=1)
    
    label_text = ttk.Label(text_frame, text="Other Comments:", font=font.Font(family="Times New Roman", size=12))
    label_text.grid(row=9, column=0, sticky=N+S+E+W)

    # add the text field to the frame
    text1 = Text(text_frame, wrap=WORD, height=10, width=50)
    y_scrollbar = ttk.Scrollbar(text_frame, orient=VERTICAL, command=text1.yview)
    text1["yscrollcommand"] = y_scrollbar.set

    text1.grid(row=10, column=0, sticky=N+S+E+W)
    y_scrollbar.grid(row=10, column=1, sticky=N+S) #N+S: fill the arrow vertically in both north and south direction

    # Return: Press the <Enter> key and Release to call the event handler
    text1.bind("<KeyRelease-Return>", enter_release_text_handler)

    # Create the last frame
    button_frame = Frame(root, highlightcolor="blue", highlightbackground="blue",  highlightthickness=5)  

    button_frame.grid(row=11, sticky=N+S+E+W)

    button_frame.rowconfigure(11, weight=1)

    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)

    # attach buttons to the last frame of root window
    button1 = ttk.Button(button_frame, text="Submit")
    button2 = ttk.Button(button_frame, text="Cancel")

    # create a style for the button
    button_style1 = ttk.Style()
    button_style2 = ttk.Style()

    # configure button styles called button1 and button2
    button_style1.configure("button1.TButton", font=("Times New Roman", 12))
    button_style2.configure("button2.TButton", font=("Times New Roman", 12))

    # set button1 and button2 to have the "button1" and "button2" styles
    button1.configure(style="button1.TButton")
    button2.configure(style="button2.TButton")

    # button1 and button2 are impacted
    button1.bind_class("TButton", "<Button-1>", button_pressed_handler)  # One Event - Button Left Clicked
    # button1.bind_class("TButton", "<ButtonRelease-1>", button_released_handler)  # One Event - Button Released

    button1.bind_class("TButton", "<Button-3>", button_pressed_handler)  # One Event - Button Right Clicked
    # button1.bind_class("TButton", "<ButtonRelease-3>", button_released_handler)  # One Event - Button Released

    button1.grid(row=11, column=0, sticky=N+S+E+W)
    button2.grid(row=11, column=1, sticky=N+S+E+W)


    root.mainloop()

if __name__ == '__main__':
    main()