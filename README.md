### 📄 **README for Image to PDF Converter**  

---

## 📌 **Overview**  
This Python script converts multiple images (**JPG, JPEG, PNG**) into a **single PDF file**.  
It allows users to:  
✅ Choose **paper size** (A4, F4, Full Page).  
✅ Select **number of images per page**.  
✅ Generate a **high-quality PDF output**.  

---

## 🚀 **Features**  
✅ **Batch Processing:** Converts multiple images at once.  
✅ **Multiple Paper Sizes:** Supports A4 (210×297mm), F4 (216×330mm), or full-size images.  
✅ **Custom Grid Layout:** Arrange multiple images per page.  
✅ **Automatic Filename Sanitization:** Removes invalid characters.  
✅ **Error Handling:** Detects missing or corrupted images.  

---

## 🛠 **Requirements**  
- Python **3.x**  
- Required Python packages:  
  ```bash
  pip install pillow
  ```

---

## 📂 **Folder Structure**  
```
📂 Converter Photo to PDF
 ├── 📂 File-Sumber     # Place input images here
 ├── 📂 File-Hasil      # Converted PDF files are saved here
 ├── 📜 convert_images_to_pdf.py  # Main script
 ├── 📜 README.md       # Documentation
```

---

## 📥 **Installation & Usage**  
### 1️⃣ **Clone or Download the Script**  
```bash
git clone https://github.com/Yodhaardiansyah/image-to-pdf.git
cd image-to-pdf
```

### 2️⃣ **Place Images in the Source Folder**  
- Move your JPG, JPEG, or PNG images to `File-Sumber/`  

### 3️⃣ **Run the Script**  
```bash
python convert_images_to_pdf.py
```

### 4️⃣ **Follow the On-Screen Prompts**  
- Select **paper size**:  
  ```
  1. A4 (210 × 297 mm)
  2. F4 (216 × 330 mm)
  3. Full Page (Original Image Size)
  ```
- Enter the **number of images per page**  
- Enter **output PDF file name**  

✅ The generated **PDF** will be saved in `File-Hasil/`.  

---

## 📌 **Example Output**  
```
Select paper size:
1. A4 (210 × 297 mm)
2. F4 (216 × 330 mm)
3. Full Page (Original Image Size)
Enter choice (1/2/3): 1

Enter number of images per page: 4

Enter output file name (without .pdf): my_photos

✅ PDF successfully created: E:\Backup_NAS\Converter Photo to PDF\File-Hasil\my_photos.pdf
```

---

## 🛠 **Customization**  
- Modify the **source and output folder paths** in the script:  
  ```python
  SOURCE_FOLDER = r"E:\Backup_NAS\Converter Photo to PDF\File-Sumber"
  OUTPUT_FOLDER = r"E:\Backup_NAS\Converter Photo to PDF\File-Hasil"
  ```
- Adjust **default paper size** in `PAPER_SIZES`.  

---

## 👨‍💻 **Developer Info**  
**Author:** Yodha Ardiansyah  
**GitHub:** [https://github.com/Yodhaardiansyah](https://github.com/Yodhaardiansyah)  

---

## 📜 **License**  
This project is licensed under the **MIT License**.  

---
