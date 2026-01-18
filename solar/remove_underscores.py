import os

# 1. Rename files in the assets folder
asset_dir = "assets"
for filename in os.listdir(asset_dir):
    if filename.startswith("_"):
        if filename.startswith("__"):
            new_name = filename[2:]
        else:
            new_name = filename[1:]  # Remove the leading underscore
        os.rename(os.path.join(asset_dir, filename), os.path.join(asset_dir, new_name))
        print(f"Renamed: {filename} -> {new_name}")

files_to_patch = ["index.html"] + [
    os.path.join(asset_dir, f) for f in os.listdir(asset_dir) if f.endswith(".js")
]

for file_path in files_to_patch:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace "_assets/" with "assets/" or just "_filename" with "filename"
    # This regex looks for strings starting with _ in quotes
    fixed_content = content.replace("assets/__", "assets/")
    fixed_content = fixed_content.replace("assets/_", "assets/")
    fixed_content = fixed_content.replace("./__", "./")
    fixed_content = fixed_content.replace("./_", "./")

    if fixed_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(fixed_content)

        print("Replaced underscores in", file_path)
