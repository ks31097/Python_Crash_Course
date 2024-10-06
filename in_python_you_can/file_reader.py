def read_file(file_path):
    try:
        with open(file_path) as file_object:
            lines = file_object.readlines()
    
        return lines

    except FileNotFoundError:
        return "File not found."
    
    except Exception as e:
        return f"An error occurred: {e}"

def print_info(information):
    if type(information) == list:
        for line in information:
            print(line.replace('python', 'C').rstrip())
    else:
        print(information)


# if __name__ == "__main__":
#     """Example usage"""
#     file_path = 'in_python_you_can/learning_python.txt'
#     print_info(read_file(file_path))