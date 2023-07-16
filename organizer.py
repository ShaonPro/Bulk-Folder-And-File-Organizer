import os
import shutil

# Function to create subfolders inside a parent folder
def create_subfolders(parent_folder, subfolder_prefix, num_subfolders):
    for i in range(1, num_subfolders + 1):
        subfolder_name = f"{subfolder_prefix}-{i}"
        subfolder_path = os.path.join(parent_folder, subfolder_name)
        os.makedirs(subfolder_path, exist_ok=True)

# Main code
parent_folder = os.getcwd()  # Get the current working directory

# Create the main folders
main_folders = ["Folder-1", "Folder-2", "Folder-3", "Folder-4"]
for main_folder in main_folders:
    os.makedirs(os.path.join(parent_folder, main_folder), exist_ok=True)

# Create the subfolders within each main folder
subfolder_prefix = "10"
num_subfolders = 5
for main_folder in main_folders:
    create_subfolders(os.path.join(parent_folder, main_folder), subfolder_prefix, num_subfolders)

# Get the list of images
images = [file for file in os.listdir(parent_folder) if file.endswith(".jpg")]
num_images = len(images)

# Copy images to the subfolders
subfolder_index = 1
subfolder_count = 0
for i, image in enumerate(images):
    subfolder_name = f"{subfolder_prefix}-{subfolder_index}"
    main_folder = main_folders[subfolder_count]
    destination_folder = os.path.join(parent_folder, main_folder, subfolder_name)
    os.makedirs(destination_folder, exist_ok=True)
    
    source_path = os.path.join(parent_folder, image)
    destination_path = os.path.join(destination_folder, image)
    shutil.copy(source_path, destination_path)

    if (i + 1) % 10 == 0:
        subfolder_index += 1
        if subfolder_index > num_subfolders:
            subfolder_index = 1
            subfolder_count += 1

print("Images have been copied successfully. Chill - By: Shaon.Pro")
