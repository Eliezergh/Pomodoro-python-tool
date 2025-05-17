#Imports
import typer
import logging
from enum import Enum
from cmds.timer import pomodoro_cmd

app = typer.Typer(help="A simple Pomodoro timer")

#Logging level enum
class LoggingLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

@app.callback()
def common(
    ctx: typer.Context,
    log_level: LoggingLevel = typer.Option(LoggingLevel.INFO,help="Set the logging level")):
    """
    Common options for the Pomodoro timer.
    """
    #Logging setup
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=log_level.value)

@app.command()
def pomodoro(minutes: int, pause: int, loops: int):
    """
    Start a Pomodoro timer, WORK PAUSE LOOPS. E.G.: pomodoro 25 5 4
    """
    pomodoro_cmd(minutes, pause, loops)

#Main function to run the Pomodoro timer
if __name__ == "__main__":
    app()