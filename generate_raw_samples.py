# -*- coding: utf-8 -*-
"""
Generate valid (non-blank) raw sample image grids for Train, Validation, and Test sets.
"""
import os
import glob
import random
from PIL import Image
import matplotlib.pyplot as plt

BASE_DIR = r'd:\mahfuj\cic1\dataset_png'
CLASSES = ['one_molecule', 'reactions', 'rest', 'several_molecules']
SAMPLES_PER_CLASS = 4

TARGET_DIR = r'd:\mahfuj\cic1\chemical_classification_models\samples and distrubutation\raw dataset'
os.makedirs(TARGET_DIR, exist_ok=True)

SUPPORTED_EXTS = ('.png', '.jpg', '.jpeg', '.tif', '.tiff', '.bmp')

def get_images(class_dir):
    files = []
    for ext in SUPPORTED_EXTS:
        files += glob.glob(os.path.join(class_dir, f'*{ext}'))
        files += glob.glob(os.path.join(class_dir, f'*{ext.upper()}'))
    return sorted(set(files))

def load_image_rgb(path, size=(224, 224)):
    img = Image.open(path).convert('RGB')
    img = img.resize(size, Image.Resampling.LANCZOS)
    return img

def generate_and_save_grid(split):
    split_dir = os.path.join(BASE_DIR, split)
    fig, axes = plt.subplots(len(CLASSES), SAMPLES_PER_CLASS, figsize=(16, 16))
    fig.suptitle(f'Sample Images — {split.capitalize()} Set', fontsize=22, fontweight='bold')
    
    for row, cls in enumerate(CLASSES):
        cls_dir = os.path.join(split_dir, cls)
        imgs = get_images(cls_dir)
        # Fix random seed for reproducible report images
        random.seed(42 + row)
        chosen = random.sample(imgs, min(SAMPLES_PER_CLASS, len(imgs)))
        
        for col, path in enumerate(chosen):
            ax = axes[row][col]
            ax.imshow(load_image_rgb(path))
            ax.axis('off')
            if col == 0:
                ax.set_ylabel(cls, fontsize=14, fontweight='bold', rotation=0, labelpad=80, va='center')
                
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    out_path = os.path.join(TARGET_DIR, f'{split}_samples.png')
    # Save BEFORE calling show()
    plt.savefig(out_path, bbox_inches='tight', dpi=150)
    plt.close(fig)
    print(f'Generated and saved: {out_path}')

# Generate grids for all splits
for split in ['train', 'validation', 'test']:
    generate_and_save_grid(split)

print("Done generating raw samples!")
