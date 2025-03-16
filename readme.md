# Voting-Based OCR System using PaddleOCR & EasyOCR

This project implements an OCR system using both PaddleOCR and EasyOCR in separate Conda environments, then applies a voting mechanism to determine the final recognized text.

## Features
- Uses PaddleOCR and EasyOCR for text extraction.
- Runs each OCR model in its own Conda environment.
- Saves OCR results as JSON files.
- Implements a voting mechanism to choose the most accurate text.

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Voting-OCR.git
cd Voting-OCR
```

### 2. Set Up Conda Environments

#### EasyOCR Environment
```bash
conda create -n easyocr_env python=3.8 -y
conda activate easyocr_env
pip install easyocr numpy
conda deactivate
```

#### PaddleOCR Environment
```bash
conda create -n torch_paddle_env python=3.8 -y
conda activate torch_paddle_env
pip install paddleocr
conda deactivate
```

> ⚠ **Note**: Before installing PaddleOCR and Torch, ensure you install the appropriate PaddlePaddle, Torch, and TorchVision versions compatible with your CUDA version.

### 3. Add Your Image
Place your image in the project directory as `image.jpg`.

### 4. Run the OCR System

#### On Windows (Using Batch File)
```bash
run_voting.bat
```

#### On Linux/macOS (Manual Steps)
```bash
conda activate torch_paddle_env
python paddle.py
conda deactivate

conda activate easyocr_env
python easy.py
conda deactivate

python vote.py
```

### 5. View the Results
- **PaddleOCR results** → `paddleocr_results.json`
- **EasyOCR results** → `easyocr_results.json`
- **Final voted result** → Displayed in the terminal.

## Project Files

| File              | Description                                             |
|-------------------|---------------------------------------------------------|
| `paddle.py`       | Runs PaddleOCR and saves results in JSON format.        |
| `easy.py`         | Runs EasyOCR and saves results in JSON format.          |
| `vote.py`         | Compares OCR outputs and applies the voting mechanism.  |
| `run_voting.bat`  | Automates running both OCRs and the voting system (Windows). |


