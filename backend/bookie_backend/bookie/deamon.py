import shutil
import subprocess
from typing import Optional


import psutil
import typer
from rich import print


app = typer.Typer()

BOOKIED_PATH = shutil.which("bookied")


def _get_bookied_process() -> Optional[psutil.Process]:
    for proc in psutil.process_iter():
        if proc.name() == "bookied":
            return proc


@app.command()
def start():
    """Attempt to start the deamon"""
    proc = _get_bookied_process()
    if proc:
        print("[bold red] Another instance of bookie deamon is running!")
        typer.Exit()
    try:
        subprocess.Popen([BOOKIED_PATH])
        print("[green] bookie deamon started sucessfully")
    except subprocess.CalledProcessError:
        print("[bold red] The deamon was not able to be started sucessfully")


@app.command()
def stop():
    proc = _get_bookied_process()
    if not proc:
        print("[yellow] No instances of bookie deamon running!")
        typer.Exit()

    proc.kill()
    print("[red] bookie deamon stopped sucessfully")


@app.command()
def restart():
    stop()
    start()

if __name__ == "__main__":
    app()
