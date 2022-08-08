import shutil
import subprocess
from typing import Optional


import psutil
import typer
from rich import print


app = typer.Typer()

BOOKIED_PATH = str(shutil.which("bookied"))


def _get_bookied_process() -> Optional[psutil.Process]:
    for proc in psutil.process_iter():
        if proc.name() == "bookied":
            return proc


@app.command()
def start() -> None:
    """Attempt to start the deamon"""
    proc = _get_bookied_process()
    if proc:
        print("[bold red] Another instance of bookie deamon is running!")
        raise typer.Exit(1)
    try:
        subprocess.Popen([BOOKIED_PATH])
        print("[green] bookie deamon started sucessfully")
    except subprocess.CalledProcessError:
        print("[bold red] The deamon was not able to be started sucessfully")
        raise typer.Exit(1)


@app.command()
def stop() -> None:
    """Stop a currently running daemon process"""
    proc = _get_bookied_process()
    if not proc:
        print("[red] No instances of bookie deamon running!")
        raise typer.Exit(1)

    proc.kill()
    print("[yellow] bookie deamon stopped sucessfully")


@app.command()
def restart() -> None:
    """Restart the daemon"""
    stop()
    start()


if __name__ == "__main__":
    app()
