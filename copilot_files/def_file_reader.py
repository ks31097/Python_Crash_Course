def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    try:
        with open(file_path) as file:
            content = file.read()    
        return content
    
    except FileNotFoundError:
        return "File not found."
    
    except Exception as e:
        return f"An error occurred: {e}"
    
if __name__ == "__main__":
    """Example usage"""
    file_path = 'copilot_files/example.txt'
    print(read_file(file_path))