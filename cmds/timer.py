#Timer CMD
#Imports
import time
from rich.console import Console

console = Console()

def pomodoro_cmd(minutes: int, pause: int, loops: int):
    """
    Countdown timer that takes a number of minutes, pause minutes, and number of loops.
    """
    seconds = minutes * 60
    pause_seconds = pause * 60
    cycles = loops

    #Print settings & metrics
    console.print(f"[bold blue]------------------------[/bold blue]")
    console.print(f"[bold blue]Work time:[/bold blue] {minutes} minutes")
    console.print(f"[bold blue]Pause time:[/bold blue] {pause} minutes")
    console.print(f"[bold blue]Loops:[/bold blue] {loops} times")
    console.print(f" ")
    console.print(f"[bold blue]Total time:[/bold blue] {minutes * loops} minutes")
    console.print(f"[bold blue]Total pause time:[/bold blue] {pause * (loops - 1)} minutes")
    console.print(f"[bold blue]Total time with pauses:[/bold blue] {minutes * loops + pause * (loops - 1)} minutes")
    console.print(f"[bold blue]------------------------[/bold blue]")
    console.print(f"[bold yellow]Starting Pomodoro timer...[/bold yellow]")

    for i in range(cycles):
        console.print(f"[bold blue]Loop {i + 1} of {cycles}[/bold blue]")
        countdown_timer(seconds, "Work time")
        if i < cycles - 1:
            console.print(f"[bold yellow]Pause time:[/bold yellow] {pause} minutes")
            countdown_timer(pause_seconds, "Pause time")

    console.print(f"[bold green]All loops completed![/bold green]")

def countdown_timer(seconds: int, label):
    """
    Countdown timer that takes a number of seconds and a label.
    """
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        console.print(f"[bold green]{label}[/bold green]: {timer}", end="\r")
        time.sleep(1)
        seconds -= 1

    # Print a blank line to clear any leftover characters
    print(" " * 40, end="\r")
    console.print(f"[bold red]Time's up! [/bold red]")
    print('\a')  # Beep sound