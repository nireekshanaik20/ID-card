# 🎓 AI-Based QR Code Attendance System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**An intelligent attendance management system using QR code scanning and computer vision**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Tech Stack](#-tech-stack) • [Screenshots](#-screenshots)

</div>

---

## 📋 Overview

This project is an **AI-powered attendance system** that combines QR code technology with computer vision to streamline student verification and attendance tracking. The system generates unique QR codes for each student and provides a real-time scanning interface for instant identity verification.

### 🎯 Key Highlights

- ✅ **Automated QR Code Generation** - Generate unique QR codes for each student
- ✅ **Real-time Scanning** - Instant QR code detection using webcam
- ✅ **Student Database Management** - Excel-based storage with pandas
- ✅ **Attendance Logging** - Automatic timestamp recording
- ✅ **User-friendly GUI** - Built with Tkinter for easy interaction
- ✅ **Data Validation** - Prevents duplicate entries and validates student information

---

## 🚀 Features

### 1. **Student Registration & QR Generation**
- Add student details (ID, Name, Course, Institute, Branch, Email, Phone)
- Automatically generate unique QR codes
- Store student data in Excel format
- Prevent duplicate student IDs
- Visual QR code preview

### 2. **QR Code Scanning & Verification**
- Real-time camera feed with visual guide box
- Instant QR code detection and decoding
- Automatic student information retrieval
- Live display of student details

### 3. **Attendance Tracking**
- Automatic attendance logging with timestamps
- Daily attendance files (organized by date)
- Excel-compatible format for easy analysis

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Core programming language |
| **OpenCV** | Computer vision and camera handling |
| **Tkinter** | GUI framework |
| **Pandas** | Data management and Excel operations |
| **pyzbar** | QR code decoding |
| **qrcode** | QR code generation |
| **Pillow (PIL)** | Image processing |

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- Webcam/Camera
- Windows/Linux/macOS

### Step 1: Clone the Repository

```bash
git clone https://github.com/nireekshanaik20/ID-card.git
cd ID-card
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install opencv-python pandas openpyxl pyzbar qrcode[pil] pillow
```

### Step 3: Verify Installation

```bash
python --version
# Should show Python 3.8+
```

---

## 💻 Usage

### 🔹 Generate Student QR Codes

1. Run the QR code generator:
```bash
python qrcodegenerate.py
```

2. Fill in student details:
   - Student ID
   - Name
   - Course
   - Institute
   - Branch
   - Email
   - Phone

3. Click **"Save & Generate QR"**
4. QR code will be saved in the `qrcodes/` folder
5. Student data will be stored in `students.xlsx`

### 🔹 Scan QR Codes & Mark Attendance

1. Run the attendance system:
```bash
python idc.py
```

2. Click **"Scan QR Code"**
3. Position the QR code within the green guide box
4. Student information will be displayed automatically
5. Attendance will be logged in a date-stamped file

---

## 📸 Screenshots

### Student Registration Interface
*Clean and intuitive form for entering student details*

### QR Code Generation
*Automatically generated QR codes with preview*

### QR Scanner Interface
*Real-time camera feed with visual guide for scanning*

### Student Verification Display
*Instant display of student information after successful scan*

---

## 📁 Project Structure

```
id-card-project/
│
├── idc.py                    # Main attendance scanning application
├── qrcodegenerate.py         # QR code generator application
├── students.xlsx             # Student database (auto-generated)
├── attendance.xlsx           # Attendance records
├── qrcodes/                  # Generated QR code images
│   └── [STUDENT_ID].png
├── December-16               # Daily attendance log
└── README.md                 # Project documentation
```

---

## 🔧 Configuration

### Camera Settings

Modify camera index in `idc.py` if you have multiple cameras:

```python
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Change 0 to 1, 2, etc.
```

### QR Code Settings

Adjust QR code parameters in `qrcodegenerate.py`:

```python
qr = qrcode.QRCode(
    version=None,              # Auto-size
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=12,               # Size of each box
    border=4                   # Border thickness
)
```

---

## 🎓 Domain & Classification

| Category | Details |
|----------|---------|
| **Domain** | Artificial Intelligence, Computer Vision |
| **Sub-domain** | Applied Machine Learning, Image Processing |
| **Technologies** | Python, OpenCV, QR Code Detection, Pandas |
| **Application** | Attendance Management, Identity Verification |

### Is This an AI Project?

**Yes!** This project qualifies as an AI project because:

- ✅ Uses **Computer Vision** (a core AI domain)
- ✅ Implements **image processing** and pattern recognition
- ✅ Applies **intelligent decision logic** for automated verification
- ✅ Utilizes **real-time object detection** (QR codes)
- ✅ Automates **identity verification** and attendance logging

---

## 🚀 Future Enhancements

Want to make this project even more powerful? Consider adding:

### 🔥 Advanced AI Features

- [ ] **Face Recognition** - Combine QR with facial verification
- [ ] **Deep Learning Models** - CNN-based face detection
- [ ] **Liveness Detection** - Anti-spoofing measures
- [ ] **Emotion Detection** - Monitor student engagement
- [ ] **Mask Detection** - COVID-19 safety compliance
- [ ] **Fraud Detection** - AI-based anomaly detection
- [ ] **Multi-factor Authentication** - QR + Face + PIN
- [ ] **Cloud Integration** - Real-time sync with cloud databases
- [ ] **Mobile App** - Cross-platform mobile application
- [ ] **Analytics Dashboard** - Attendance trends and insights

---

## 🐛 Troubleshooting

### Camera Not Accessible

```python
# Try different camera backends
cap = cv2.VideoCapture(0)  # Default
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # DirectShow (Windows)
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)   # V4L2 (Linux)
```

### QR Code Not Detected

- Ensure good lighting conditions
- Keep QR code flat and within the green guide box
- Adjust camera focus
- Clean the camera lens

### Excel File Errors

- Make sure `students.xlsx` exists (will be created automatically)
- Check file permissions
- Close Excel if the file is open

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Nireeksha Naik**

- 💼 [LinkedIn](https://linkedin.com/in/yourprofile)
- 🐙 [GitHub](https://github.com/yourusername)
- 📧 Email: your.email@example.com

---

## 🙏 Acknowledgments

- OpenCV community for excellent computer vision tools
- pyzbar developers for QR code decoding capabilities
- Python community for amazing libraries

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Open an issue on GitHub
3. Contact the author

---

<div align="center">

### ⭐ Star this repository if you found it helpful!

**Made with ❤️ and Python**

</div>
