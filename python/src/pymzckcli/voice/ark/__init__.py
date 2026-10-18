"""火山引擎语音识别/合成命令行工具.

密钥使用环境变量 ARK_API_KEY.
"""

import typer

from .asr import recognize
from .tts import synthesize

__all__ = [
    "app",
]


app = typer.Typer(
    name="ark",
    help="语音识别/合成(火山引擎)",
    no_args_is_help=True,
)
app.command()(recognize)
app.command()(synthesize)
