import os
import shutil

def organize_folder(target_path):
    # Define file categories and their extensions
    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Scripts': ['.py', '.js', '.html', '.css', '.cpp'],
        'Audio_Video': ['.mp3', '.mp4', '.mkv', '.wav']
    }

    if not os.path.exists(target_path):
        print("Path does not exist!")
        return

    for filename in os.listdir(target_path):
        file_path = os.path.join(target_path, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)
        
        # Find the correct category
        moved = False
        for category, exts in extensions.items():
            if ext.lower() in exts:
                dest_dir = os.path.join(target_path, category)
                
                # Create category folder if it doesn't exist
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                
                shutil.move(file_path, os.path.join(dest_dir, filename))
                print(f"Moved: {filename} -> {category}/")
                moved = True
                break
        
        if not moved:
            print(f"Skipped (Unknown type): {filename}")

if __name__ == "__main__":
    path = input("Enter the full path of the folder to organize: ")
    organize_folder(path)
    print("\nCleanup complete!")
