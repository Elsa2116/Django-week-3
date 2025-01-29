def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        print("File content:")
        print(content)
    except FileNotFoundError:
        print("Error: File not found.")
    except UnicodeDecodeError:
        print("Error: File is corrupted or contains unreadable characters.")
    except Exception as e:
        print(f"Unexpected error: {e}")

file_path = "example.txt"  
read_file(file_path)