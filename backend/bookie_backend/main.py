import typer
import subprocess

if __name__ == "__main__":
    def main():
        subprocess.run("uvicorn bookie_backend.deamon:app",shell=True)
    main()