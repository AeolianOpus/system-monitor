import os

import time

# System statistic functions
from monitor.stats import (
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
    get_gpu_usage
)

# Import logger function
from utils.logger import get_logger

# Import ASCII bar function
from utils.ascii_graph import bar

# Import file saving function
from utils.file_handler import save_report as save_report_file

# Import plotter function
from utils.plotter import export_usage_chart


# Main class for system monitoring
class SystemMonitor:

    # Create logger for this class
    def __init__(self):
        self.logger = get_logger("SystemMonitor")

    # Method to build status lines
    def _build_status_lines(self):

        # CPU usage
        cpu = get_cpu_usage()

        # RAM usage
        memory = get_memory_usage()

        # DISK usage
        disk = get_disk_usage()

        # GPU usage (if available)
        gpu = get_gpu_usage()

        # Logging the data that were collected
        self.logger.info("Collected system stats")

        # ASCII bars
        lines = [
            bar("CPU", cpu),
            bar("Memory", memory),
            bar("Disk", disk),
        ]

        # GPU bar if GPU exists
        if gpu is not None:
            lines.append(bar("GPU", gpu))
        else:
            lines.append("GPU        | Not detected")

        return lines, cpu, memory, disk, gpu

    # Returns system status as text
    def get_status_text(self) -> str:
        lines, *_ = self._build_status_lines()
        return "\n".join(lines)

    # Prints system status to terminal
    def show_status(self) -> None:
        print("\n--- System Monitor ---\n")
        print(self.get_status_text())
        print()

    # Saves system report to file
    def save_report(self) -> None:
        text = self.get_status_text()
        save_report_file(text)
        self.logger.info("Saved system report to file")
        print("Report saved to data/report.txt")

    # Exports system usage graph as PNG image
    def export_graph(self) -> None:
        _, cpu, memory, disk, gpu = self._build_status_lines()
        path = export_usage_chart(cpu, memory, disk, gpu)
        self.logger.info(f"Exported matplotlib chart to {path}")
        print(f"Graph exported to {path}")

    # Live monitoring in terminal
    def live_monitor(self, interval: int = 2) -> None:
        self.logger.info(f"Started live monitor (interval={interval}s)")

        try:
            while True:
                # Clears the terminal screen
                os.system("cls" if os.name == "nt" else "clear")

                # Prints the header
                print("=== LIVE SYSTEM MONITOR (Ctrl+C to stop) ===\n")

                # Prints the current system status
                print(self.get_status_text())

                # Waits before refreshing
                time.sleep(interval)

        # Keyboard interrupt to stop live monitoring
        except KeyboardInterrupt:
            self.logger.info("Stopped live monitor")
            print("\nLive monitoring stopped.")
