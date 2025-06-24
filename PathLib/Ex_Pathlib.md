# ✅ Full Example Using pathlib :
```
from pathlib import Path

# 1. Create a Path to a file
file_path = Path("example_folder") / "file.txt"

# 2. Make sure the directory exists
file_path.parent.mkdir(parents=True, exist_ok=True)
print(f"Directory created: {file_path.parent}")

# 3. Write some text to the file
file_path.write_text("Hello from Faizan!\nThis is pathlib demo.")
print(f"File written: {file_path}")

# 4. Check if the file exists
if file_path.exists():
    print("✅ File exists!")

# 5. Check if it's a file or directory
print("Is file:", file_path.is_file())      # True
print("Is directory:", file_path.is_dir())  # False

# 6. Read the content of the file
content = file_path.read_text()
print("\n📄 File content:")
print(content)

# 7. List all `.txt` files in the folder using glob
print("\n📂 .txt files in folder:")
for txt_file in file_path.parent.glob("*.txt"):
    print(" -", txt_file.name)

```

## 🧪 Output (example):
```
Directory created: example_folder

File written: example_folder/file.txt

✅ File exists!

Is file: True
Is directory: False

📄 File content:
Hello from Faizan!
This is pathlib demo.

📂 .txt files in folder:
 - file.txt

``` 
