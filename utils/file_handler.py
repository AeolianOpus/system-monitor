# Imports the data directory path from config.py file
from config import DATA_DIR

# Function to save report text to a file
def save_report(text: str) -> None:


    # The full path to the report file
    path = DATA_DIR / "report.txt"

    # Opens file and writes text
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)