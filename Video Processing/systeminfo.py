from pytorchmodel import systemInfo

if __name__ == "__main__":
    try:
        from pytorchmodel import systemInfo
    except ImportError:
        print("Error importing required libraries. Please install the required libraries and try again.")
    
    try:
        systemInfo()
    except Exception as e:
        print(f"An error occurred: {e}\n\nSuggestion: Check if the required libraries are installed and try again.")