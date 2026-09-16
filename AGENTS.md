# AGENTS.md

个人工具集仓库：存放跨项目复用的 skills 与脚本。仓库为单一 git 仓库，各子目录不单独建仓。

## 目录与约定

* `skills/` — Agent skills。每个 skill 一个子目录，遵循标准 skill 结构（`SKILL.md` + 所需资源）。
* `python/` — Python 工具。使用 [uv](https://docs.astral.sh/uv/) 管理（Python >= 3.12）：
  * 依赖变更用 `uv add` / `uv remove`，不要手改 `pyproject.toml` 依赖后不更新 lockfile。
  * 运行代码用 `uv run`，不要手动创建 venv 或用 pip 安装。
  * 每个工具一个包或一个子项目，入口通过 `[project.scripts]` 暴露 CLI。
* `javascript/` — JS/TS 工具。每个工具独立子目录，自带 `package.json`。
