import os

data_dir = "data"
for file in os.listdir(data_dir):
    if file.startswith("user.."):   # wrong format
        parts = file.split("..")
        if len(parts) == 2:
            new_name = "user.1." + parts[1]   # replace with correct ID (example 1)
            os.rename(os.path.join(data_dir, file), os.path.join(data_dir, new_name))
            print(f"Renamed: {file} → {new_name}")
