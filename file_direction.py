import os

file_path =  "main.py"

if os.path.exists(file_path):
    
    print(f"yes the {file_path} is exist .")
else:
    print("sorry dosn't exist")