import customtkinter as ctk

# ================= Appearance =================
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

# ================= Functions =================

def button_click(value):
    display.configure(state="normal")
    current = display.get()
    operators = "+-*/"

    # Prevent invalid operator usage
    if value in operators:
        if not current or current[-1] in operators:
            display.configure(state="disabled")
            return

    # Prevent multiple decimals in one number
    if value == ".":
        last_number = current.split("+")[-1].split("-")[-1].split("*")[-1].split("/")[-1]
        if "." in last_number:
            display.configure(state="disabled")
            return

    display.insert("end", value)
    display.configure(state="disabled")


def clear_display():
    display.configure(state="normal")
    display.delete(0, "end")
    display.configure(state="disabled")


def backspace():
    display.configure(state="normal")
    current = display.get()
    display.delete(0, "end")
    display.insert(0, current[:-1])
    display.configure(state="disabled")


def calculate():
    expression = display.get()
    try:
        result = eval(expression)

        # Fix floating precision
        if isinstance(result, float):
            result = round(result, 10)
            result = int(result) if result.is_integer() else result

        display.configure(state="normal")
        display.delete(0, "end")
        display.insert(0, str(result))
        display.configure(state="disabled")

    except:
        display.configure(state="normal")
        display.delete(0, "end")
        display.insert(0, "Error")
        display.configure(state="disabled")


# ================= Window =================
app = ctk.CTk()
app.title("Simple Calculator")
app.geometry("380x550")
app.resizable(False, False)

# ================= Display =================
display = ctk.CTkEntry(
    app,
    font=("Arial", 30),
    width=330,
    height=70,
    corner_radius=15,
    justify="right",
    state="disabled"
)
display.pack(pady=20)

# ================= Buttons =================
frame = ctk.CTkFrame(app, fg_color="transparent")
frame.pack()

buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        btn = ctk.CTkButton(
            frame, text=text,
            width=70, height=70,
            corner_radius=20,
            font=("Arial", 25),
            fg_color="#22c55e",
            hover_color="#16a34a",
            command=calculate
        )
    else:
        btn = ctk.CTkButton(
            frame, text=text,
            width=70, height=70,
            corner_radius=20,
            font=("Arial", 25),
            command=lambda t=text: button_click(t)
        )

    btn.grid(row=row, column=col, padx=8, pady=8)

# ================= CLEAR + BACKSPACE  =================
bottom_frame = ctk.CTkFrame(app, fg_color="transparent")
bottom_frame.pack(pady=10)

clear_btn = ctk.CTkButton(
    bottom_frame,
    text="CLEAR",
    width=155,
    height=70,
    corner_radius=20,
    font=("Arial", 22),
    fg_color="#ef4444",
    hover_color="#dc2626",
    command=clear_display
)
clear_btn.grid(row=0, column=0, padx=5)

back_btn = ctk.CTkButton(
    bottom_frame,
    text="⌫",
    width=155,
    height=70,
    corner_radius=20,
    font=("Arial", 26),
    fg_color="#64748b",
    hover_color="#475569",
    command=backspace
)
back_btn.grid(row=0, column=1, padx=5)

# ================= Start =================
app.mainloop()
