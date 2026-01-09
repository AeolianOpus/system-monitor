# Utility to create ASCII bar graphs
def bar(label: str, value: int, max_width: int = 30) -> str:


    # Ensures that values stay between 0 and 100
    value = max(0, min(100, int(value)))

    # Calculate amount of characters that should be filled
    filled = int((value / 100) * max_width)

    # Calculates amount of characters that should be empty
    empty = max_width - filled

    # The bar string
    graph = "█" * filled + "-" * empty

    # Formatted bar with label
    return f"{label:<10} |{graph}| {value}%"