import tkinter as tk
import time

TEST_TIME = 60 

def start_test():
    global start_time, running
    running = True
    start_time = time.time()
    timer_label.config(text="Time left: 60")
    text_box.delete("1.0", "end")
    text_box.config(state="normal")
    text_box.focus()
    update_timer()

def update_timer():
    if not running:
        return
    elapsed = int(time.time() - start_time)
    remaining = TEST_TIME - elapsed

    if remaining <= 0:
        end_test()
    else:
        timer_label.config(text=f"Time left: {remaining}")
        root.after(1000, update_timer)

def end_test():
    global running
    running = False
    typed = text_box.get("1.0", "end").strip()
    words = typed.split()
    wpm = len(words)  # since test is exactly 60 seconds

    result_label.config(text=f"WPM: {wpm}")
    text_box.config(state="disabled")

def reset_test():
    global running
    running = False
    timer_label.config(text="Time left: 60")
    result_label.config(text="WPM: —")
    text_box.config(state="disabled")


root = tk.Tk()
root.title("Simple Typing Speed Test")
root.geometry("600x350")


text_box = tk.Text(root, height=6, width=60, state="disabled", font=("Arial", 12))
text_box.pack(pady=10)

start_btn = tk.Button(root, text="Start Test", command=start_test)
start_btn.pack()

reset_btn = tk.Button(root, text="Reset", command=reset_test)
reset_btn.pack(pady=5)

timer_label = tk.Label(root, text="Time left: 60", font=("Arial", 12))
timer_label.pack()

result_label = tk.Label(root, text="WPM: —", font=("Arial", 14))
result_label.pack(pady=10)

running = False
root.mainloop()
