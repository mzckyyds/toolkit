"""Python CLI Toolkit."""

import typer

from .asr import app as asr_app
from .tts import app as tts_app

app = typer.Typer(help="Python CLI Toolkit", no_args_is_help=True)

app.add_typer(
    asr_app,
    name="asr",
    help="火山引擎单向流式语音识别(reference: https://docs.volcengine.com/docs/6561/2628951?lang=zh).",
    no_args_is_help=True,
)


app.add_typer(
    tts_app,
    name="tts",
    help="火山引擎单向流式语音合成(reference: https://docs.volcengine.com/docs/6561/2534913?lang=zh).",
    no_args_is_help=True,
)


def main() -> None:
    """入口函数."""
    app()


if __name__ == "__main__":
    main()
