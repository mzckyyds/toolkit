# python

个人 Python 工具集, CLI 入口为 `pymzckcli`. 使用 [uv](https://docs.astral.sh/uv/) 管理 (Python >= 3.12).

## 命令

```bash
uv run pymzckcli --help
```

### asr — 火山引擎 SAUC 流式语音识别

```bash
uv run pymzckcli asr recognize <音频文件>
```

基于官方 demo (`src/pymzckcli/asr/protocol.py` 与 `sauc_websocket_demo.py` 为官方源码原样拷贝).

### tts — 火山引擎 Seed-TTS 语音合成

```bash
uv run pymzckcli tts synth "要合成的文本" [-o 输出文件]
```

基于官方 demo (`src/pymzckcli/tts/protocols.py` 与 `__init__.py` 为官方源码原样拷贝).

### 鉴权

两个命令默认从仓库根目录 `.env` 读取连接配置:

- `ARK_ASR_API_KEY` / `ARK_ASR_ENDPOINT` / `ARK_ASR_API_RESOURCE_ID` — SAUC 语音识别
- `ARK_TTS_API_KEY` / `ARK_TTS_ENDPOINT` / `ARK_TTS_API_RESOURCE_ID` — Seed-TTS 语音合成

也可通过 `--api-key` / `--url` / `--resource-id` 显式指定.

NOTE: 官方 `asr/protocol.py` 转换非 WAV 音频后会删除原始文件.

## 开发

```bash
uv run ruff format .     # 格式化
uv run ruff check .      # 质量检查
uv run pyright           # 类型检查 (strict)
uv run pytest            # 测试
```
