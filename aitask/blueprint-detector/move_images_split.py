import os
import shutil
import random
from pathlib import Path

# Set random seed for reproducibility
random.seed(42)

base_dir = Path(__file__).parent
images_dir = base_dir / 'images'
train_dir = images_dir / 'train'
val_dir = images_dir / 'val'

# Create train/val directories if they don't exist
train_dir.mkdir(parents=True, exist_ok=True)
val_dir.mkdir(parents=True, exist_ok=True)

# Get all image files in images/ (not in train/ or val/)
image_files = [f for f in os.listdir(images_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg')) and os.path.isfile(images_dir / f)]
random.shuffle(image_files)

split_idx = int(len(image_files) * 0.8)
train_files = image_files[:split_idx]
val_files = image_files[split_idx:]

for f in train_files:
    shutil.move(str(images_dir / f), str(train_dir / f))
    print(f"Moved {f} to train/")
for f in val_files:
    shutil.move(str(images_dir / f), str(val_dir / f))
    print(f"Moved {f} to val/")

print("\nImage split complete!")