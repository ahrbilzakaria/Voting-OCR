import json

# Load PaddleOCR results
with open('paddleocr_results.json', 'r') as f:
    paddle_results = json.load(f)

# Load EasyOCR results
with open('easyocr_results.json', 'r') as f:
    easy_results = json.load(f)

# Function to extract text and confidence from PaddleOCR results
def extract_paddle_results(paddle_results):
    extracted = []
    for line in paddle_results:
        if line:  # Check if line is not empty
            for word_info in line:
                text = word_info[1][0]  # Extracted text
                confidence = word_info[1][1]  # Confidence score
                bounding_box = word_info[0]  # Bounding box coordinates
                extracted.append({
                    'text': text,
                    'confidence': confidence,
                    'bounding_box': bounding_box,
                    'source': 'PaddleOCR'
                })
    return extracted

# Function to extract text and confidence from EasyOCR results
def extract_easy_results(easy_results):
    extracted = []
    for detection in easy_results:
        text = detection['text']  # Extracted text
        confidence = detection['confidence']  # Confidence score
        bounding_box = detection['bounding_box']  # Bounding box coordinates
        extracted.append({
            'text': text,
            'confidence': confidence,
            'bounding_box': bounding_box,
            'source': 'EasyOCR'
        })
    return extracted

# Function to align results and select the best one for each text region
def align_results(paddle_results, easy_results):
    final_results = []

    # Compare each PaddleOCR result with each EasyOCR result
    for paddle_detection in paddle_results:
        best_match = None
        best_confidence = paddle_detection['confidence']
        best_source = 'PaddleOCR'

        for easy_detection in easy_results:
            # Check if bounding boxes overlap (simple comparison for now)
            paddle_box = paddle_detection['bounding_box']
            easy_box = easy_detection['bounding_box']

            # Simple overlap check (you can improve this)
            if (paddle_box[0][0] < easy_box[1][0] and paddle_box[1][0] > easy_box[0][0] and
                paddle_box[0][1] < easy_box[1][1] and paddle_box[1][1] > easy_box[0][1]):
                # If bounding boxes overlap, compare confidence scores
                if easy_detection['confidence'] > best_confidence:
                    best_match = easy_detection
                    best_confidence = easy_detection['confidence']
                    best_source = 'EasyOCR'

        # Add the best result for this text region
        if best_match:
            final_results.append({
                'text': best_match['text'],
                'confidence': best_confidence,
                'bounding_box': best_match['bounding_box'],  # Include bounding box
                'source': best_source
            })
        else:
            final_results.append({
                'text': paddle_detection['text'],
                'confidence': paddle_detection['confidence'],
                'bounding_box': paddle_detection['bounding_box'],  # Include bounding box
                'source': 'PaddleOCR'
            })

    # Add any EasyOCR results that were not matched
    for easy_detection in easy_results:
        if not any(easy_detection['bounding_box'] == final['bounding_box'] for final in final_results):
            final_results.append({
                'text': easy_detection['text'],
                'confidence': easy_detection['confidence'],
                'bounding_box': easy_detection['bounding_box'],  # Include bounding box
                'source': 'EasyOCR'
            })

    return final_results

# Extract results
paddle_texts = extract_paddle_results(paddle_results)
easy_texts = extract_easy_results(easy_results)

# Align results and select the best one for each text region
final_results = align_results(paddle_texts, easy_texts)

# Print final results
print("Final Results (Voting):")
for result in final_results:
    print(f"Text: {result['text']}, Confidence: {result['confidence']}, Source: {result['source']}")

# Pause to keep the window open
input("Press Enter to exit...")