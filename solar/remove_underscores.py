import os

# 1. Rename files in the assets folder
asset_dir = "assets"
for filename in os.listdir(asset_dir):
    if filename.startswith("_"):
        if filename[2] == "_":  # If filename starts with two underscores.
            new_name = filename[2:]
        else:
            new_name = filename[1:]  # Remove the leading underscore
        os.rename(os.path.join(asset_dir, filename), os.path.join(asset_dir, new_name))
        print(f"Renamed: {filename} -> {new_name}")

# 2. Update the HTML file to point to the new names
with open("index.html", "r") as f:
    content = f.readlines()

# Replace "_assets/" with "assets/" or just "_filename" with "filename"
# This regex looks for strings starting with _ in quotes
fixed_content = [
    line.replace("assets/__", "assets/").replace("assets/_", "assets/")
    for line in content
]

with open("index.html", "w") as f:
    f.writelines(fixed_content)

print("HTML updated!")
