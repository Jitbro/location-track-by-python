import os
import shutil
from pathlib import Path

def organize_files(source_dir):
    # Define file categories and their extensions
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Music': ['.mp3', '.wav', '.flac'],
        'Archives': ['.zip', '.rar', '.7z'],
        'Scripts': ['.py', '.js', '.sh']
    }

    # Convert source_dir to Path object
    source_path = Path(source_dir)
    
    # Create source directory if it doesn't exist
    source_path.mkdir(parents=True, exist_ok=True)

    # Iterate through files in the source directory
    for file in source_path.iterdir():
        if file.is_file():  # Process only files, not directories
            # Get file extension in lowercase
            extension = file.suffix.lower()
            
            # Find the appropriate category for the file
            destination_folder = 'Others'  # Default folder for uncategorized files
            for category, extensions in file_types.items():
                if extension in extensions:
                    destination_folder = category
                    break
            
            # Create destination folder if it doesn't exist
            dest_path = source_path / destination_folder
            dest_path.mkdir(exist_ok=True)
            
            # Move the file to its destination folder
            try:
                shutil.move(str(file), str(dest_path / file.name))
                print(f"Moved {file.name} to {destination_folder}")
            except Exception as e:
                print(f"Error moving {file.name}: {e}")

def main():
    # Get the source directory from user input
    source_dir = input("Enter the directory path to organize (e.g., ~/Downloads): ")
    
    # Expand user directory (~) if present
    source_dir = os.path.expanduser(source_dir)
    
    # Check if directory exists
    if not os.path.exists(source_dir):
        print("Directory does not exist!")
        return
    
    print(f"Organizing files in {source_dir}...")
    organize_files(source_dir)
    print("File organization completed!")

if __name__ == "__main__":
    main()
