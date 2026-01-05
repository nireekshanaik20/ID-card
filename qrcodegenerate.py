import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os
import qrcode
from PIL import Image, ImageTk

FILE_NAME = "students.xlsx"
QR_FOLDER = "qrcodes"

# ---------- Save to Excel + Generate QR ----------
def save_student():
    data = {
        "student_id": entry_id.get().strip(),
        "name": entry_name.get().strip(),
        "course": entry_course.get().strip(),
        "institute": entry_institute.get().strip(),
        "branch": entry_branch.get().strip(),
        "email": entry_email.get().strip(),
        "phone": entry_phone.get().strip()
    }

    # Validation
    if "" in data.values():
        messagebox.showerror("Error", "All fields are required")
        return

    # ---------- Save to Excel ----------
    if os.path.exists(FILE_NAME):
        df = pd.read_excel(FILE_NAME)

        # Prevent duplicate student_id
        if data["student_id"] in df["student_id"].values:
            messagebox.showerror("Error", "Student ID already exists!")
            return

        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    else:
        df = pd.DataFrame([data])

    df.to_excel(FILE_NAME, index=False)

    # ---------- Generate QR (ONLY student_id) ----------
    os.makedirs(QR_FOLDER, exist_ok=True)

    qr = qrcode.QRCode(
        version=None,  # AUTO (important)
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=12,
        border=4
    )

    qr.add_data(data["student_id"])
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    qr_path = f"{QR_FOLDER}/{data['student_id']}.png"
    img.save(qr_path)

    show_qr(qr_path)

    messagebox.showinfo("Success", "Student saved & QR generated successfully!")
    clear_fields()

# ---------- Show QR ----------
def show_qr(path):
    top = tk.Toplevel(root)
    top.title("Generated QR Code")
    top.resizable(False, False)

    img = Image.open(path)
    img = img.resize((260, 260))
    photo = ImageTk.PhotoImage(img)

    lbl = tk.Label(top, image=photo)
    lbl.image = photo
    lbl.pack(padx=10, pady=10)

    tk.Label(
        top,
        text="Scan this QR Code",
        font=("Arial", 12, "bold")
    ).pack(pady=5)

# ---------- Clear Inputs ----------
def clear_fields():
    for entry in entries:
        entry.delete(0, tk.END)

# ---------- GUI ----------
root = tk.Tk()
root.title("Student QR Code Generator")
root.geometry("420x500")
root.config(bg="#f2f2f2")

tk.Label(
    root,
    text="Student Details Entry",
    font=("Arial", 18, "bold"),
    bg="#f2f2f2"
).pack(pady=12)

frame = tk.Frame(root, bg="white", bd=2, relief="groove")
frame.pack(padx=20, pady=10, fill="both", expand=True)

def create_row(text):
    tk.Label(
        frame,
        text=text,
        anchor="w",
        bg="white",
        font=("Arial", 10, "bold")
    ).pack(fill="x", padx=10, pady=(8, 0))

    entry = tk.Entry(frame)
    entry.pack(fill="x", padx=10)
    return entry

entry_id = create_row("Student ID")
entry_name = create_row("Name")
entry_course = create_row("Course")
entry_institute = create_row("Institute")
entry_branch = create_row("Branch")
entry_email = create_row("Email")
entry_phone = create_row("Phone")

entries = [
    entry_id, entry_name, entry_course,
    entry_institute, entry_branch,
    entry_email, entry_phone
]

tk.Button(
    root,
    text="Save & Generate QR",
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12, "bold"),
    command=save_student
).pack(pady=18)

root.mainloop()
