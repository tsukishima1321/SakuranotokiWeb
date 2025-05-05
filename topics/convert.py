import os
import codecs

# Define the source and target directories
source_dir = os.path.dirname(__file__)
target_dir = os.path.join(source_dir, "converted")

# Create the target directory if it doesn't exist
os.makedirs(target_dir, exist_ok=True)

# Iterate through all files in the source directory
for filename in os.listdir(source_dir):
    if filename.endswith(".htm"):
        source_path = os.path.join(source_dir, filename)
        target_path = os.path.join(target_dir, filename)

        # Read the file with gb2312 encoding and write it with utf-8 encoding
        with codecs.open(source_path, 'r', encoding='gbk',errors="ignore") as source_file:
            content = source_file.read()
        with codecs.open(target_path, 'w', encoding='utf-8') as target_file:
            target_file.write(content)

print("Conversion completed. Files saved in:", target_dir)