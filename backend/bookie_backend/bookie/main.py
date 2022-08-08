import typer

from bookie_backend.bookie.daemon import app

app = typer.Typer()
app.add_typer(app, name="daemon")

# if __name__ == "__main__":
#     app()
