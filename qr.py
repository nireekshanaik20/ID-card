import pandas as pd
import qrcode
import os

# Load Excel
df = pd.read_excel("students.xlsx")

# Create folder for QR codes
os.makedirs("qr_codes", exist_ok=True)

for _, row in df.iterrows():
    student_id = str(row["student_id"]).strip().upper()

    qr = qrcode.make(student_id)
    qr.save(f"qr_codes/{student_id}.png")

print("✅ QR codes generated successfully!")
