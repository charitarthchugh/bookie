import subprocess

import deamon
import typer

app = typer.Typer()
app.add_typer(deamon.app, name="deamon")

if __name__ == "__main__":
    app()
