def calculate_counts(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            word_count = sum(len(line.split()) for line in lines)
            line_count = len(lines)
        print(f"Lines: {line_count}, Words: {word_count}")
    except FileNotFoundError:
        print("File not found. Please check the file path.")

file_path = "example.txt"  
calculate_counts(file_path)