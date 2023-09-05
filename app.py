import os

def print_file_tree(root_dir, indent=0):
    # Get a list of all files and subdirectories in the current directory
    items = os.listdir(root_dir)

    # Sort the items alphabetically
    items.sort()

    for item in items:
        item_path = os.path.join(root_dir, item)

        # Skip the .env folder and its contents
        if item == ".env" and os.path.isdir(item_path):
            continue
        
        # Print the current item with proper indentation
        print("  " * indent + "|-- " + item)

        # If the item is a directory, recursively print its tree
        if os.path.isdir(item_path):
            print_file_tree(item_path, indent + 1)

if __name__ == "__main__":
    # Get the directory where the script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))

    print(f"File Tree for: {script_directory}")
    print_file_tree(script_directory)
