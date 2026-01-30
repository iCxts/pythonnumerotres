import cv2
import numpy as np
import pytesseract
import sys

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    denoised = cv2.fastNlMeansDenoising(gray, h=10)
    binary = cv2.adaptiveThreshold(
        denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )
    return binary

def extract_text(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image '{image_path}'")
        return None

    processed = preprocess_image(image)
    text = pytesseract.image_to_string(processed, lang='eng')
    return text.strip()

def create_sample_image():
    img = np.ones((200, 600, 3), dtype=np.uint8) * 255
    cv2.putText(img, "Hello World!", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3)
    cv2.putText(img, "NumPy + OpenCV + Tesseract", (30, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 50), 2)
    cv2.imwrite("sample_text.png", img)
    print("Created sample_text.png")
    return "sample_text.png"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    else:
        print("No image provided, creating sample image...")
        image_path = create_sample_image()

    print(f"\nExtracting text from: {image_path}")
    print("-" * 40)
    text = extract_text(image_path)
    if text:
        print(text)
    print("-" * 40)
