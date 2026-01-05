import cv2
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from pyzbar.pyzbar import decode, ZBarSymbol
from time import strftime as stf
# ---------------- LOAD EXCEL ----------------
try:
    df = pd.read_excel("students.xlsx")
    df["student_id"] = df["student_id"].astype(str).str.strip().str.upper()
except:
    messagebox.showerror("Error", "students.xlsx not found")
    exit()

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Student QR Verification System")
root.geometry("500x420")
root.config(bg="#f2f2f2")
x = root.winfo_screen



tk.Label(
    root,
    text="Student QR Code Scanner",
    font=("Arial", 18, "bold"),
    bg="#f2f2f2"
).pack(pady=10)

scan_lbl = tk.Label(
    root,
    text="Scanned ID: ---",
    font=("Arial", 11, "bold"),
    bg="#f2f2f2",
    fg="green"
)
scan_lbl.pack()

result_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
result_frame.pack(pady=10, fill="both", expand=True)

student_id_lbl = tk.Label(result_frame, text="student_id: ", font=("Arial", 12), bg="white")
name_lbl = tk.Label(result_frame, text="Name: ", font=("Arial", 12), bg="white")
course_lbl = tk.Label(result_frame, text="Course: ", font=("Arial", 12), bg="white")
#institute_lbl = tk.Label(result_frame, text="institute: ", font=("Arial", 12), bg="white")
#branch_lbl = tk.Label(result_frame, text="branch: ", font=("Arial", 12), bg="white")
email_lbl = tk.Label(result_frame, text="email: ", font=("Arial", 12), bg="white")
phone_lbl = tk.Label(result_frame, text="Phone: ", font=("Arial", 12), bg="white")

student_id_lbl.pack(anchor="w", padx=10, pady=5)
name_lbl.pack(anchor="w", padx=10, pady=5)
course_lbl.pack(anchor="w", padx=10, pady=5)
#institute_lbl.pack(anchor="w", padx=10, pady=5)
#branch_lbl.pack(anchor="w", padx=10, pady=5)
email_lbl.pack(anchor="w", padx=10, pady=5)
phone_lbl.pack(anchor="w", padx=10, pady=5)




def att_reg(sid):
    with open(f'{stf("%B-%d")}','a') as f:
        f.write(f"Student Id,{sid},{stf('%H:%M:%S')}\n")

# ---------------- FETCH STUDENT ----------------
def fetch_student(sid):
    student = df[df["student_id"] == sid]

    if student.empty:
        messagebox.showerror("Error", f"Student not found!\nID: {sid}")
        return

    row = student.iloc[0]
    student_id_lbl.config(text=f"student_id: {row['student_id']}")
    name_lbl.config(text=f"Name: {row['name']}")
    course_lbl.config(text=f"Course: {row['course']}")
    #institute_lbl.config(text=f"institute: {row['institute']}")
    #branch_lbl.config(text=f"branch: {row['branch']}")
    email_lbl.config(text=f"email: {row['email']}")
    phone_lbl.config(text=f"Phone: {row['phone']}")

    att_reg(sid)




# ---------------- CAMERA SCAN ----------------
def scan_id():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        messagebox.showerror("Error", "Camera not accessible")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # GREEN GUIDE BOX (visual only)
        h, w, _ = frame.shape
        x1, y1 = int(w*0.1), int(h*0.1)
        x2, y2 = int(w*0.9), int(h*0.9)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
        cv2.putText(frame, "Show QR here",
                    (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 255, 0), 2)

        decoded = decode(frame, symbols=[ZBarSymbol.QRCODE])

        for obj in decoded:
            student_id = obj.data.decode("utf-8", errors="ignore").strip().upper()
            scan_lbl.config(text=f"Scanned ID: {student_id}")

            cap.release()
            cv2.destroyAllWindows()
            fetch_student(student_id)
            return

        cv2.imshow("QR Scanner - Press Q to Exit", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# ---------------- BUTTON ----------------
tk.Button(
    root,
    text="Scan QR Code",
    command=scan_id,
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=22
).pack(pady=15)

root.mainloop()
