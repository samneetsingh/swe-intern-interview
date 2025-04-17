def save_user_code(code: str, filename: str) -> None:
    """
    Save the user code to a specified file.
    
    Args:
        code (str): The code to save.
        filename (str): The name of the file to save the code in.
    """
    try:
        with open(filename, 'w') as f:
            f.write(code)
        f.close()
        return "Code saved successfully."
    except Exception as e:
        return f"Error saving code: {e}"