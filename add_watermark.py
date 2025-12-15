import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

def upload_image():
    global img, img_path
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if img_path:
        img = Image.open(img_path)
        status.config(text="Image loaded")

def add_watermark():
    if not img_path:
        return

    watermark_text = entry.get()
    image = Image.open(img_path).convert("RGBA")

    txt_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)

    font = ImageFont.load_default()
    width, height = image.size

    draw.text((width - 150, height - 30), watermark_text, fill=(255, 255, 255, 120), font=font)

    watermarked = Image.alpha_composite(image, txt_layer)
    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    if save_path:
        watermarked.save(save_path)
        status.config(text="Watermark added & saved")

# GUI
root = tk.Tk()
root.title("Simple Watermark App")
root.geometry("300x200")

tk.Button(root, text="Upload Image", command=upload_image).pack(pady=10)

entry = tk.Entry(root)
entry.insert(0, "My Watermark")
entry.pack(pady=5)

tk.Button(root, text="Add Watermark & Save", command=add_watermark).pack(pady=10)

status = tk.Label(root, text="")
status.pack()

root.mainloop()
