from tkinter import *
from tkmacosx import Button
from tkinter import messagebox

DEF_WIDTH = 350
DEF_HEIGHT = 500
label_height = DEF_HEIGHT // 6
label_width = DEF_WIDTH
global operator
operator = ""
global first_number
first_number = ""
global last_key_clicked
last_key_clicked = ""


root = Tk()

root.geometry(f"{DEF_WIDTH+10}x{DEF_HEIGHT+10}")
root.attributes("-topmost", True)
root.resizable(False, False)

root.title("Calculator")

# Convert and save the image as icon.ico for Windows or icon.xbm for macOS
# Replace "app-icon.png" with the path to your actual image file
icon_file = "app-icon.png"
icon = PhotoImage(file=icon_file)
root.iconphoto(True, icon)

# -----functions-------
def last_key_button_pressed(key):
    global last_key_clicked
    last_key_clicked = key

def pressed_operator(op):
    global operator
    global first_number
    global last_key_clicked
    last_key_clicked = op
    operator = op
    first_number = label_text.get()


def check_input(value):
    input_size = label_text.get()
    if len(input_size) > 10:
        root.attributes("-topmost", False)  
        messagebox.showerror("Input Error", value)
        root.attributes("-topmost", True)
        label_text.set("0")

def pressed_c_button():
    label_text.set("0")
    
def pressed_dot_button():
    if not (label_text.get().__contains__(".")):
        label_text.set(label_text.get()+".")

def pressed_sign_button():
    number = int(label_text.get())  
    if number > 0:
        number = -number
    else:
        number = abs(number)
    label_text.set(str(number))  

    

def number_clicked(number):
    global last_key_clicked
    global first_number
    if label_text.get()=="0":
        label_text.set(number)
    elif last_key_clicked in ("/", "+", "-", "%", "*"):
        first_number = label_text.get()
        label_text.set(number)
    else:
        label_text.set(label_text.get()+number)
    check_input("Should not exceed more than 10 digits")
    last_key_clicked = number

def c_button():
    label_text.set("0")

def pressed_equal_to_button():
    global operator
    global first_number
    try:
        result = eval(f"{first_number} {operator} {label_text.get()}")
        label_text.set(result)
    except (ArithmeticError, ValueError) as e:
      check_input("Invalid Operation")

    if len(label_text.get()) > 10:
        check_input("Sorry, the result has more than 10 digits.\n10 digits is the limit.")


label_text = StringVar()
label_text.set("0")

root.grid_propagate(False)
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure((1,2,3,4,5),weight=1)
root.grid_columnconfigure((0,1,2,3),weight=1)

# Create label
label = Label(root, textvariable=label_text, font=('Arial', 60))
label.configure(foreground="#ffffff", background="#222222", anchor="e", borderwidth=1)
label.grid(row=0, column=0, columnspan=6, sticky="ewns")

SPECIAL_BUTTONS_FG = "#000000"
SPECIAL_BUTTONS_BG = "#FFFF00"

special_buttons_properties = [
    {"text":"C","row":1,"col":0,"bg":SPECIAL_BUTTONS_BG,"fg":SPECIAL_BUTTONS_FG,"function":c_button},
    {"text":"+/-","row":1,"col":1,"bg":SPECIAL_BUTTONS_BG,"fg":SPECIAL_BUTTONS_FG,"function":pressed_sign_button},
    {"text":"%","row":1,"col":2,"bg":SPECIAL_BUTTONS_BG,"fg":SPECIAL_BUTTONS_FG,"function": lambda: pressed_operator("%")},
    {"text":"/","row":1,"col":3,"bg":SPECIAL_BUTTONS_BG,"fg":SPECIAL_BUTTONS_FG,"function": lambda: pressed_operator("/")},
    {"text":"*","row":2,"col":3,"bg":SPECIAL_BUTTONS_BG,"fg":SPECIAL_BUTTONS_FG,"function": lambda: pressed_operator("*")},
    {"text":"-","row":3,"col":3,"bg":SPECIAL_BUTTONS_BG,"fg":SPECIAL_BUTTONS_FG,"function": lambda: pressed_operator("-")},
    {"text":"+","row":4,"col":3,"bg":SPECIAL_BUTTONS_BG,"fg":SPECIAL_BUTTONS_FG,"function": lambda: pressed_operator("+")},
    {"text":"=","row":5,"col":3,"bg":SPECIAL_BUTTONS_BG,"fg":SPECIAL_BUTTONS_FG,"function":pressed_equal_to_button},
    {"text":".","row":5,"col":2,"bg":SPECIAL_BUTTONS_BG,"fg":SPECIAL_BUTTONS_FG,"function":pressed_dot_button},
]

keypad_numbers = [{"7": 0, "8": 1, "9": 2},{"4": 0, "5": 1, "6": 2},{"1": 0, "2": 1, "3": 2}]


for special_button in special_buttons_properties:
    button = Button(root, text=special_button["text"], command=special_button["function"], font=("Arial", 20, 'bold'), fg="#fff", bg="#848884")
    button.configure(bg=special_button["bg"],fg=special_button["fg"],highlightbackground="#000000")
    button.grid(row=special_button["row"], column=special_button["col"], sticky="ewns")



for row, dictionary in enumerate(keypad_numbers, start=2):
    for text, col in dictionary.items():
        button = Button(root, text=text,command=lambda number=text: number_clicked(number),font=("Arial", 20, 'bold'), fg="#fff", bg="#848884")
        button.configure(highlightbackground="#000000",bg="#fff",fg="#000000")
        button.grid(row=row, column=col, sticky="ewns")

button_zero = Button(root, text="0", command=lambda number="0": number_clicked(number), font=("Arial", 20, 'bold'), fg="#fff", bg="#848884")
button_zero.configure(bg="#fff",fg="#000000",highlightbackground="#000000")
button_zero.grid(row=5, column=0, columnspan=2, sticky="ewns")

root.mainloop()