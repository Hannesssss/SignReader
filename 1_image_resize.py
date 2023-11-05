from PIL import Image
import os

# Specify input and output folders for 30 km/h signs
input_folder_30 = 'Data/Signs/raw_30'
output_folder_30 = 'Data/Signs/clean_30'



# Ensure the output folders exist, or create them if they don't
os.makedirs(output_folder_30, exist_ok=True)


# List all files in the input folder for 30 km/h signs
file_list_30 = os.listdir(input_folder_30)

# Iterate through each image file in the 30 km/h sign input folder
for filename in file_list_30:
    # Join the input and output paths
    input_path = os.path.join(input_folder_30, filename)
    output_path = os.path.join(output_folder_30, filename)

    # Open the image
    image = Image.open(input_path)

    # Resize the image to 256x256 pixels
    image = image.resize((256, 256))

    # Save the resized image to the 30 km/h sign output folder
    image.save(output_path)


print("All images resized and saved to their respective clean folders.")
