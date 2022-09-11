import rich
from rich.panel import Panel


def success(msg):
    """Print success message."""
    return rich.print(Panel(msg, style="green bold"))


def information(msg):
    """Print informational message."""
    return rich.print(Panel(msg, style="blue bold"))


def warn(msg):
    """Print warning message."""
    return rich.print(Panel(msg, style="yellow bold"))


def error(msg):
    """Print error message."""
    return rich.print(Panel(msg, style="red bold"))
