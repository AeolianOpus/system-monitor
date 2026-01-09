from pathlib import Path

# The base directory of the project
BASE_DIR = Path(__file__).resolve().parent

# The directory where log files are stored
LOG_DIR = BASE_DIR / "logs"

# The directory where data files are stored
DATA_DIR = BASE_DIR / "data"

# Create logs directory if it does not exist
LOG_DIR.mkdir(exist_ok=True)

# Create data directory if it does not exist
DATA_DIR.mkdir(exist_ok=True)