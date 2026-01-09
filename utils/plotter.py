import matplotlib.pyplot as plt

# Imports the data directory path from config.py file
from config import DATA_DIR

# Function to create and save a bar chart image
def export_usage_chart(cpu: int, memory: int, disk: int, gpu: int | None):
    """
    Creates and saves a bar chart image showing system usage.
    """

    # Creates labels and values
    labels = ["CPU", "Memory", "Disk"]
    values = [cpu, memory, disk]

    # Exception for GPU usage, meaning if GPU is present
    if gpu is not None:
        labels.append("GPU")
        values.append(gpu)

    # Creates a figure
    plt.figure()

    # Creates a bar chart
    plt.bar(labels, values)

    # The Y-axis with values from 0 to 100
    plt.ylim(0, 100)

    # The chart title
    plt.title("System Usage")

    # The label of Y-axis
    plt.ylabel("Percent")

    # The output path for the image file
    path = DATA_DIR / "system_usage.png"

    # Saves the figure to a file
    plt.savefig(path)

    # Closes to free memory
    plt.close()

    return path