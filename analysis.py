import pytsk3
import os

def analyze_filesystem(image_path):
    """
    Analyzes the filesystem of a disk image to identify and potentially recover files.

    Args:
        image_path (str): Path to the disk image file.

    Returns:
        list: A list of file paths within the image.
    """
    file_paths = []

    try:
        img_handle = pytsk3.Img_Info(image_path)
        fs = pytsk3.FS_Info(img_handle)

        def process_directory(directory, parent_path=""):
            print(f"Processing directory: {parent_path}")  # Debugging
            for entry in directory:
                # Skip '.' and '..'
                if entry.info.name.name in [b'.', b'..']:
                    continue

                # Decode byte string to string
                file_name = entry.info.name.name.decode('utf-8')
                
                # Ensure parent_path is a string
                if not isinstance(parent_path, str):
                    print(f"Error: parent_path is not a string: {parent_path}")
                    parent_path = str(parent_path)
                
                file_path = os.path.join(parent_path, file_name)
                print(f"File path: {file_path}")  # Debugging

                # Add the file path to the list
                if entry.info.name.type == pytsk3.TSK_FS_NAME_TYPE_REG:
                    file_paths.append(file_path)
                elif entry.info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
                    # Open subdirectories
                    sub_dir = fs.open_dir(entry.info.name.name.decode('utf-8'))
                    process_directory(sub_dir, file_path)

	
        # Start processing from the root directory
        root_dir = fs.open_dir()
        process_directory(root_dir)

    except OSError as e:
        print(f"Error opening image file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return file_paths
