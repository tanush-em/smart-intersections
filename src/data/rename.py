import os
import glob

directory_path = r"E:\PROJECTS\SIH-2024\src\data\EVD_model\finetune\images"
file_pattern = os.path.join(directory_path, '*.*')
image_files = glob.glob(file_pattern)
for index, file_path in enumerate(image_files, start=151):
    new_file_name = f'{index}.jpg'
    new_file_path = os.path.join(directory_path, new_file_name)
    os.rename(file_path, new_file_path)
print(f"Renamed {len(image_files)} files.")