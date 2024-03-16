from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer_count = ''
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    window.after_cancel(timer_count)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    check.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    work_time = WORK_MIN * 60
    break_time = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        timer(long_break)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        timer(break_time)
        label.config(text="Break", fg=PINK)

    else:
        timer(work_time)
        label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def timer(count):

    count_min = math.floor(count / 60)
    count_sec = (count % 60)

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer_count
        timer_count = window.after(1000, timer, count - 1)

    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            mark += "✔"
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="TIMER", bg=YELLOW, font=(FONT_NAME, 65), fg=GREEN)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
canvas.grid(column=1, row=1)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

check = Label(text="", fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset)
reset_button.grid(column=2, row=2)

window.mainloop()
