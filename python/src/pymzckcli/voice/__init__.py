"""语音识别/合成命令行工具."""

import typer

from .ark import app as ark_app

__all__ = [
    "app",
]


app = typer.Typer(
    name="voice",
    help="语音识别/合成",
    no_args_is_help=True,
)

app.add_typer(ark_app)
