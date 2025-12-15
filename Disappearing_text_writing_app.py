import tkinter as tk

TIME_LIMIT = 5000  # 5 seconds (milliseconds)

class WriteOrVanish:
    def __init__(self, root):
        self.root = root
        self.root.title("Write or Vanish")

        self.text = tk.Text(root, font=("Arial", 14))
        self.text.pack(expand=True, fill="both")

        self.timer = None
        self.text.bind("<Key>", self.reset_timer)

    def reset_timer(self, event=None):
        if self.timer:
            self.root.after_cancel(self.timer)
        self.timer = self.root.after(TIME_LIMIT, self.clear_text)

    def clear_text(self):
        self.text.delete("1.0", tk.END)

root = tk.Tk()
app = WriteOrVanish(root)
root.mainloop()
