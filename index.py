import os

def list_index_files(directory):
    index_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file == "index.py":
                index_files.append(os.path.join(root, file))
    return index_files

def display_menu(index_files):
    print("Select an index.py file to launch:")
    for i, file in enumerate(index_files, start=1):
        print(f"{i}. {file}")

def launch_selected_file(index_files, choice):
    try:
        choice = int(choice)
        if 1 <= choice <= len(index_files):
            file_to_launch = index_files[choice - 1]
            os.system(f"python {file_to_launch}")
        else:
            print("Invalid choice. Please select a valid option.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    root_directory = "."
    index_files = list_index_files(root_directory)

    if not index_files:
        print("No index.py files found in the specified directory.")
    else:
        while True:
            display_menu(index_files)
            choice = input("Enter the number of the file you want to launch (q to quit): ")
            
            if choice.lower() == "q":
                break
            else:
                launch_selected_file(index_files, choice)
