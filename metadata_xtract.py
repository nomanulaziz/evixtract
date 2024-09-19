import os
import time

def extract_metadata(file_path):
    """
    Extracts metadata from a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        dict: A dictionary containing extracted metadata information.
    """
    metadata = {}
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return metadata

    try:
        stat_result = os.stat(file_path)
        metadata["creation_time"] = time.ctime(stat_result.st_ctime)  # Use st_ctime for creation time
        metadata["modification_time"] = time.ctime(stat_result.st_mtime)  # Use st_mtime for modification time
        metadata["access_time"] = time.ctime(stat_result.st_atime)  # Use st_atime for access time
        metadata["file_size"] = stat_result.st_size
        metadata["permissions"] = oct(stat_result.st_mode)  # Convert mode to octal string
    except Exception as e:
        print(f"Error extracting metadata from {file_path}: {e}")
    return metadata
