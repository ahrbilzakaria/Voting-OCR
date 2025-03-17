import json

def weighted_voting(paddle_results, easy_results):

    # Extract and normalize results from PaddleOCR
    paddle_extracted = []
    lenght_paddle = 0
    for line in paddle_results:
        if line:  # Check if line is not empty
            for word_info in line:
                lenght_paddle += len(word_info[1][0])
                paddle_extracted.append({
                    'text': word_info[1][0],  # Extracted text
                    'confidence': word_info[1][1],  # Confidence score
                    'bounding_box': word_info[0],  # Bounding box coordinates
                    'source': 'PaddleOCR',
                    'length': len(word_info[1][0])  # Add text length
                })

    # Extract and normalize results from EasyOCR
    easy_extracted = []
    lenght_easy = 0
    for detection in easy_results:
        lenght_easy += len(detection['text'])
        easy_extracted.append({
            'text': detection['text'],  # Extracted text
            'confidence': detection['confidence'],  # Confidence score
            'bounding_box': detection['bounding_box'],  # Bounding box coordinates
            'source': 'EasyOCR',
            'length': len(detection['text'])  # Add text length
        })

    if lenght_paddle > lenght_easy:
        return paddle_extracted , lenght_paddle
    else:
        return easy_extracted , lenght_easy


# Load results
with open('paddleocr_results.json', 'r') as f:
    paddle_results = json.load(f)

with open('easyocr_results.json', 'r') as f:
    easy_results = json.load(f)

# Apply the weighted voting mechanism
final_results , length = weighted_voting(paddle_results, easy_results)

# Print final results sorted by text length
print(f"\nFinal Results from :{'PaddleOCR' if final_results[0]['source'] == 'PaddleOCR' else 'EasyOCR'}")
print('Total length of text:', length)
print("---------------------------------------------------")
for result in final_results:
    print(f"Text ({result['length']} chars): {result['text']}")
    print(f"Confidence: {result['confidence']}\n")

input("Press Enter to exit...")