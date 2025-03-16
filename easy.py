import easyocr
import json
import numpy as np

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])

# Perform OCR on an image
img_path = 'image.jpg'
result = reader.readtext(img_path)

# Save the results to a JSON file
with open('easyocr_results.json', 'w') as f:
    # Convert the result to a list of dictionaries for easier JSON serialization
    extracted = []
    for detection in result:
        # Convert numpy array to list for bounding box coordinates
        bounding_box = [list(map(float, point)) for point in detection[0]]
        extracted.append({
            'text': detection[1],  # Extracted text
            'confidence': float(detection[2]),  # Confidence score
            'bounding_box': bounding_box  # Bounding box coordinates (list of lists)
        })
    json.dump(extracted, f)

print("EasyOCR results saved to easyocr_results.json")