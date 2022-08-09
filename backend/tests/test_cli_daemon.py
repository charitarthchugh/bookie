import time
from typing import Optional

import psutil
from typer.testing import CliRunner

from bookie_backend.bookie.main import app

runner = CliRunner()


def get_running_proc(proc_name: str) -> Optional[psutil.Process]:
    """Get a currently running process

    Args:
        proc_name (str): Name of process

    Returns:
        Optional[psutil.Process]: process information
    """
    for proc in psutil.process_iter():
        if proc.name() == proc_name:
            return proc


def test_start():
    out = runner.invoke(app, ["daemon", "start"])
    assert get_running_proc("bookied") and out.exit_code == 0


def test_restart():
    out = runner.invoke(app, ["daemon", "restart"])
    assert (
        out.exit_code == 0
        and out.output.strip()
        == "bookie daemon stopped sucessfully\n bookie daemon started sucessfully"
    )


def test_stop():
    out = runner.invoke(app, ["daemon", "stop"])
    assert (
        out.output.strip() == "bookie daemon stopped sucessfully"
        and get_running_proc("bookied").status()
        == "zombie"  # Status is zombie because it has completed but the PID is still in memory
        and out.exit_code == 0
    )
