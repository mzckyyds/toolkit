"""Python CLI Toolkit."""

import typer

from .asr import app as asr_app
from .image import app as image_app
from .tts import app as tts_app
from .video import app as video_app

app = typer.Typer(
    help="Python CLI Toolkit",
    no_args_is_help=True,
)

app.add_typer(asr_app)
app.add_typer(tts_app)
app.add_typer(image_app)
app.add_typer(video_app)


def main() -> None:
    """入口函数."""
    app()


if __name__ == "__main__":
    main()
