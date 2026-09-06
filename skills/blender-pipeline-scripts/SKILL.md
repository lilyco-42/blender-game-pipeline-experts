---
name: blender-pipeline-scripts
description: Programmatic Blender pipeline orchestration. Batch low-poly + UV + PBR baking + FBX export using Python scripts inspired by DLR-RM/BlenderProc.
---

# Blender 管线脚本（程序化批量处理）

> 参考 DLR-RM/BlenderProc（3,699⭐）的程序化管线思路。
> 用 Python 脚本批量跑"低模拓扑 → UV → PBR 烘焙 → FBX 导出"全流程。

## 适用场景

- 一组资产（道具 / 角色）需要按相同流程批量处理
- 每晚跑一次"过一遍"所有资产，把新版本全部重导到引擎
- 资产命名规范、面数预算、贴图尺寸已经标准化的产线

## 工作流

1. **配置阶段**：在 `config.yaml` 写清资产清单 + 面数预算 + 引擎格式
2. **预处理**：清理未 Apply 的变换、合并 by-distance、删除无用 modifier
3. **拓扑检查**：自动检测 N-gon、三角化比例、极位置，输出报告
4. **UV 检查**：自动检测重叠、拉伸、超界
5. **烘焙**：批量跑 Cycles Normal/AO/Cavity 烘焙，输出到引擎规范路径
6. **导出**：按引擎规范导出 FBX（UE Send-to-Unreal / Unity 通用 / Godot 专用轴）

## 怎么用

参见 `references/usage.md` 的完整示例。

## 模板

- `templates/batch_config.yaml` — 一组资产的批量配置模板
- `templates/asset_template.blend` — 一个空的资产模板工程（含 Collection 结构）

## 脚本

- `scripts/run_pipeline.py` — 主入口：读取 config → 跑全流程
- `scripts/topology_check.py` — 拓扑质量自检
- `scripts/uv_check.py` — UV 质量自检
- `scripts/bake_all.py` — 批量 Cycles 烘焙
- `scripts/export_fbx.py` — 引擎 FBX 导出

## 输出

- `output/{asset_name}/` 每个资产一份
- `output/report.html` 整批资产的质检报告
- `output/logs/` 详细执行日志