# -*- coding: utf-8 -*-
"""
Extract images from notebook and save them exactly to the raw dataset and preprocess dataset folders.
"""
import json
import base64
import os

BASE = r'd:\mahfuj\cic1\chemical_classification_models\samples and distrubutation'
RAW_DIR = os.path.join(BASE, 'raw dataset')
PRE_DIR = os.path.join(BASE, 'preprocess dataset')

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PRE_DIR, exist_ok=True)

with open(r'd:\mahfuj\cic1\Chemical_Image_Classification.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

def save_image(cell_idx, out_idx, target_path):
    cell = nb['cells'][cell_idx]
    if out_idx < len(cell['outputs']):
        o = cell['outputs'][out_idx]
        if 'image/png' in o.get('data', {}):
            b64data = o['data']['image/png']
            img_data = base64.b64decode(b64data)
            with open(target_path, 'wb') as f_out:
                f_out.write(img_data)
            print(f'Extracted Cell {cell_idx} Output {out_idx} -> {target_path} (Size: {len(img_data)} bytes)')
        else:
            print(f'Error: Output {out_idx} in cell {cell_idx} is not image/png')
    else:
        print(f'Error: Cell {cell_idx} does not have output index {out_idx}')

# Map files to notebook cell outputs
mapping = [
    # Raw Dataset
    (49, 0, os.path.join(RAW_DIR, 'train_samples.png')),
    (51, 0, os.path.join(RAW_DIR, 'validation_samples.png')),
    (53, 0, os.path.join(RAW_DIR, 'test_samples.png')),
    (29, 0, os.path.join(RAW_DIR, 'class_distribution.png')),
    
    # Preprocessed Dataset
    (54, 0, os.path.join(PRE_DIR, 'Figure_Preprocessed_Class_Distribution.png')),
    (43, 0, os.path.join(PRE_DIR, 'train_preprocessed_samples.png')),
    (43, 1, os.path.join(PRE_DIR, 'validation_preprocessed_samples.png')),
    (43, 2, os.path.join(PRE_DIR, 'test_preprocessed_samples.png'))
]

for cell_idx, out_idx, target_path in mapping:
    save_image(cell_idx, out_idx, target_path)

print("Finished extracting all figures from the notebook!")
