import pdfplumber
import os

def extract_images(pdf_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    image_paths = []

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            for j, img in enumerate(page.images):
                try:
                    image = page.extract_image(img["object_id"])
                    if image:
                        img_bytes = image["image"]
                        img_path = f"{output_folder}/img_{i}_{j}.png"

                        with open(img_path, "wb") as f:
                            f.write(img_bytes)

                        image_paths.append(img_path)
                except:
                    continue

    return image_paths