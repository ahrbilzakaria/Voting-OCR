@echo off

REM Run PaddleOCR
call conda activate ./torch_paddle_env
python paddle.py
call conda deactivate

REM Run EasyOCR
call conda activate ./easyocr_env
python easy.py
call conda deactivate

REM Compare results
python vote.py