# Imports the SystemMonitor class
from monitor.system_monitor import SystemMonitor

# Main function
def main():

    monitor = SystemMonitor()

    # Main program loop
    while True:
        print("\n===== THE SUPERDUPER SYSTEM MONITOR =====")
        print("1. Show system status (single run)")
        print("2. Save report to file")
        print("3. Live auto-refresh mode (2s interval)")
        print("4. Export graph (PNG format)")
        print("5. Exit")

        # User input
        choice = input("Select an option: ").strip()

        # User choices and exceptions
        if choice == "1":
            monitor.show_status()

        elif choice == "2":
            monitor.save_report()

        elif choice == "3":
            interval_input = input("Refresh interval in seconds (default 2): ").strip()

            # Validates the interval input
            if interval_input.isdigit() and int(interval_input) > 0:
                interval = int(interval_input)
            else:
                interval = 2

            monitor.live_monitor(interval)

        elif choice == "4":
            monitor.export_graph()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Bruh learn to read, try again.")


# Runs the main function
if __name__ == "__main__":
    main()