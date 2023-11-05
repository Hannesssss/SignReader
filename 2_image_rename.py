import os

# Specify the folder paths for 30 km/h signs and potatoes
folder_path_30 = 'Data/Signs/clean_30'
folder_path_potatoes = 'Data/Potatoes/clean_potatoes'

# Function to rename images in a folder
def rename_images(folder_path, prefix):
    # List all files in the folder
    file_list = os.listdir(folder_path)

    # Rename the images with a suitable pattern
    for i, filename in enumerate(file_list):
        new_filename = f"{prefix}{i+1:03}.jpg"  # Use leading zeros for sorting
        new_path = os.path.join(folder_path, new_filename)

        # Check if the new filename already exists, and skip if it does
        if os.path.exists(new_path):
            print(f"Skipping existing file: {new_filename}")
        else:
            os.rename(os.path.join(folder_path, filename), new_path)

# Rename 30 km/h sign images
rename_images(folder_path_30, '30_sign_')

# Rename potato images
rename_images(folder_path_potatoes, 'potato_')

print("Image renaming completed.")
