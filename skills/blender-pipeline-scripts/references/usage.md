# 使用方法：批量管线

## 1. 准备 config.yaml

```bash
cp templates/batch_config.yaml ./my_config.yaml
# 编辑 my_config.yaml，填好你的资产清单
```

## 2. （可选）干跑一遍

不进入 Blender，只检查 config 格式是否合法：

```bash
python scripts/run_pipeline.py --config my_config.yaml --dry-run
```

## 3. 真实跑全流程

```bash
blender --background --python scripts/run_pipeline.py -- --config my_config.yaml
```

> Blender 必须安装并可在命令行调用（4.0+）。

## 4. 单步运行（调试用）

```bash
# 仅拓扑检查
blender --background --python scripts/run_pipeline.py -- --config my_config.yaml

# 仅烘焙（不跑全流程）
blender --background --python scripts/bake_all.py -- \
    --config my_config.yaml \
    --maps normal ao cavity \
    --samples 128 \
    --output ./output/textures/

# 仅 FBX 导出
blender --background --python scripts/export_fbx.py -- \
    --input ./assets/character_hero_rigged.blend \
    --output ./output/character_hero_unreal.fbx \
    --engine unreal
```

## 5. 看报告

跑完后打开 `output/report.html` 看每个资产的状态。

## 6. 接入 CI / 定时任务

最常见的用法：
- 每天凌晨 3 点跑一次全量（cron / Windows Task Scheduler）
- 资产文件 commit 后自动跑（GitHub Actions / GitLab CI）
- 跑完把 `report.html` 推送到 Slack / 钉钉

## 依赖

- Python 3.11+
- PyYAML
- Blender 4.0+（仅真实跑时需要）

安装 Python 依赖：
```bash
pip install pyyaml
```