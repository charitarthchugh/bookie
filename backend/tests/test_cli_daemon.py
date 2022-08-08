from typing import Optional

import psutil
from bookie_backend.bookie.main import app
from typer.testing import CliRunner

runner = CliRunner()


def get_running_proc(proc_name: str) -> Optional[psutil.Process]:
    for proc in psutil.process_iter():
        if proc.name() == proc_name:
            return proc


def test_start():
    output = runner.invoke(app, ["daemon", "start"])
    assert get_running_proc("bookied")


def test_restart():
    previous_instance = get_running_proc("bookied")
    output = runner.invoke(app, ["daemon", "restart"])
    assert output.exit_code == 0
    current_instance = get_running_proc("bookied")
    assert previous_instance != current_instance


def test_stop():
    output = runner.invoke(app, ["daemon", "stop"])
    assert output.exit_code == 0
    assert get_running_proc("bookied") is None
