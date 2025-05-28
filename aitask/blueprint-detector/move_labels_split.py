import os
import shutil
from pathlib import Path

base_dir = Path(__file__).parent
images_dir = base_dir / 'images'
labels_dir = base_dir / 'labels'
train_img_dir = images_dir / 'train'
val_img_dir = images_dir / 'val'
train_lbl_dir = labels_dir / 'train'
val_lbl_dir = labels_dir / 'val'

# Create label train/val directories if they don't exist
train_lbl_dir.mkdir(parents=True, exist_ok=True)
val_lbl_dir.mkdir(parents=True, exist_ok=True)

def move_labels(img_dir, lbl_dir):
    for img_file in os.listdir(img_dir):
        if img_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            base = os.path.splitext(img_file)[0]
            label_file = f"{base}.txt"
            src = labels_dir / label_file
            dst = lbl_dir / label_file
            if src.exists():
                shutil.copy2(src, dst)
                print(f"Moved {label_file} to {lbl_dir}")
            else:
                print(f"Warning: {label_file} not found for {img_file}")

move_labels(train_img_dir, train_lbl_dir)
move_labels(val_img_dir, val_lbl_dir)

print("\nLabel split complete!")
