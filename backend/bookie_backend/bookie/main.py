import typer

from bookie_backend.bookie import daemon 

app = typer.Typer()
app.add_typer(daemon.app, name="daemon")

if __name__ == "__main__":
    app()
