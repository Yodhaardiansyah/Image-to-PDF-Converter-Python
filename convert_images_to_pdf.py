"""
Image to PDF Converter
----------------------
This script converts images (JPG, JPEG, PNG) into a single PDF file.
Supports different paper sizes (A4, F4, Full Page) and multiple images per page.

Developed by: Yodha Ardiansyah
GitHub: https://github.com/Yodhaardiansyah
"""

from PIL import Image, ImageOps
import os
import glob
import re
import math

# Source and output folders
SOURCE_FOLDER = r"E:\Backup_NAS\Converter Photo to PDF\File-Sumber"
OUTPUT_FOLDER = r"E:\Backup_NAS\Converter Photo to PDF\File-Hasil"

# Paper size in pixels (300 dpi)
PAPER_SIZES = {
    "A4": (2480, 3508),  # 210 × 297 mm @ 300 dpi
    "F4": (2551, 3898),  # 216 × 330 mm @ 300 dpi
    "Full": None          # Use original image size
}

def find_images(folder):
    """Find all image files in the folder and subfolders."""
    extensions = ("*.jpg", "*.jpeg", "*.png")
    image_files = []

    for ext in extensions:
        image_files.extend(glob.glob(os.path.join(folder, "**", ext), recursive=True))

    return sorted(image_files)  # Sort files for better order

def sanitize_filename(filename):
    """Sanitize file name by removing invalid characters."""
    return re.sub(r'[\\/*?:"<>|]', "", filename).strip()

def arrange_images_on_paper(images, paper_size, images_per_page):
    """Arrange multiple images into a single PDF page."""
    if paper_size:
        paper = Image.new("RGB", paper_size, "white")  # White background

        # Determine grid (rows & columns) for image arrangement
        cols = math.ceil(math.sqrt(images_per_page))
        rows = math.ceil(images_per_page / cols)

        # Calculate image size within the grid
        img_width = paper_size[0] // cols
        img_height = paper_size[1] // rows

        x_positions = [i * img_width for i in range(cols)]
        y_positions = [i * img_height for i in range(rows)]

        # Place images on the grid
        for idx, img in enumerate(images):
            if idx >= images_per_page:
                break

            img.thumbnail((img_width, img_height), Image.LANCZOS)  # Resize image
            x_offset = x_positions[idx % cols]
            y_offset = y_positions[idx // cols]

            paper.paste(img, (x_offset, y_offset))

        return paper
    return images[0]  # If "Full" is selected, use the original image size

def convert_images_to_pdf(image_files, output_pdf, paper_size, images_per_page):
    if not image_files:
        print("❌ No images found.")
        return

    pages = []
    for i in range(0, len(image_files), images_per_page):
        batch = image_files[i:i + images_per_page]  # Select images per page
        images = []

        for img_path in batch:
            try:
                img = Image.open(img_path).convert("RGB")  # Convert to RGB
                images.append(img)
            except Exception as e:
                print(f"⚠️ Failed to read {img_path}: {e}")

        if images:
            page = arrange_images_on_paper(images, paper_size, images_per_page)
            pages.append(page)

    if pages:
        pages[0].save(output_pdf, save_all=True, append_images=pages[1:])
        print(f"✅ PDF successfully created: {output_pdf}")
    else:
        print("❌ No valid images found for conversion.")

if __name__ == "__main__":
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)  # Create output folder if not exists
    image_files = find_images(SOURCE_FOLDER)  # Find images in source folder

    # Select paper size
    print("Select paper size:")
    print("1. A4 (210 × 297 mm)")
    print("2. F4 (216 × 330 mm)")
    print("3. Full Page (Original Image Size)")
    
    choice = input("Enter choice (1/2/3): ").strip()
    if choice == "1":
        paper_size = PAPER_SIZES["A4"]
    elif choice == "2":
        paper_size = PAPER_SIZES["F4"]
    elif choice == "3":
        paper_size = PAPER_SIZES["Full"]
    else:
        print("❌ Invalid choice. Using Full Page.")
        paper_size = PAPER_SIZES["Full"]

    # Select number of images per page
    try:
        images_per_page = int(input("Enter number of images per page: ").strip())
        if images_per_page < 1:
            raise ValueError
    except ValueError:
        print("❌ Invalid input. Using 1 image per page.")
        images_per_page = 1

    # Enter output filename
    filename = input("Enter output file name (without .pdf): ").strip()
    filename = sanitize_filename(filename)  # Sanitize filename

    # Default filename if empty
    if not filename:
        filename = "output"

    output_pdf = os.path.join(OUTPUT_FOLDER, f"{filename}.pdf")

    convert_images_to_pdf(image_files, output_pdf, paper_size, images_per_page)
