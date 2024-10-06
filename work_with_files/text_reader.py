def file_reader(filename):
    """Read information from file"""
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
            # breakpoint()
    except FileNotFoundError:
        # pass
        return f"Sorry, the file {filename} does not exist."
    else:
        return content
        # return content.split()