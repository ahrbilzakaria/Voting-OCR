from paddleocr import PaddleOCR
import json

# Initialize the OCR model
ocr = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=True)

# Perform OCR on an image
img_path = './image.jpg'
result = ocr.ocr(img_path, cls=True)

# Save the results to a JSON file
with open('paddleocr_results.json', 'w') as f:
    json.dump(result, f)

print("PaddleOCR results saved to paddleocr_results.json")