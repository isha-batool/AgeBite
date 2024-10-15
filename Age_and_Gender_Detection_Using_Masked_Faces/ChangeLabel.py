import os
import datetime

# Define the path to your image directory and the new directory
image_dir = r'D:\FYP\DATASETS\FGNET_Masked\FGNET-MASK'
new_dir = r'D:\FYP\DATASETS\FGNET_Masked\Labelled_FGNET_Mask'

# Create the new directory if it doesn't exist
os.makedirs(new_dir, exist_ok=True)

# Function to convert old labels to new format
def convert_label(old_label):
    try:
        # Extract parts from the old label
        age = old_label[4:6]  # A02 -> 02
        gender_code = old_label[7:9]  # _01 or _02
        gender = '0' if gender_code == '01' else '1'  # _01 -> 0 for male, _02 -> 1 for female
        race = '0'  # Assuming race is neutral (0) as in your example
        date_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]  # Current date & time

        # Construct new label
        new_label = f'{int(age)}_{gender}_{race}_{date_time}.jpg'
        return new_label
    except Exception as e:
        print(f"Error converting label for {old_label}: {e}")
        return None

# Check if the image directory exists and is accessible
if not os.path.exists(image_dir):
    print(f"The image directory {image_dir} does not exist.")
else:
    print(f"Processing images in directory: {image_dir}")

    # Rename files and move them to the new directory
    for filename in os.listdir(image_dir):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            print(f"Processing file: {filename}")
            old_label = os.path.splitext(filename)[0]  # Get the filename without extension
            new_label = convert_label(old_label)
            if new_label:
                old_path = os.path.join(image_dir, filename)
                new_path = os.path.join(new_dir, new_label)
                try:
                    os.rename(old_path, new_path)
                    print(f'Renamed and moved: {filename} -> {new_label}')
                except Exception as e:
                    print(f"Error moving file {filename}: {e}")
            else:
                print(f"Skipping file {filename} due to label conversion error.")
        else:
            print(f"Skipping file {filename}, does not end with .jpg or .jpeg")
