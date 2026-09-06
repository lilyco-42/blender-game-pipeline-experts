# Blender 游戏资产管线团

> 面向游戏美术的 Blender 全链路团队：低模拓扑 + UV → PBR 材质 + 烘焙 → 骨骼绑定 + 动画，资产可直接交付 Unity / UE / Godot。

一个 **WorkBuddy Team 型专家团**（4 个角色协同）：主理人 + 建模师 + 材质师 + 绑定师。

## 团队构成

| 成员 ID | 中文花名 | 职业 | 职责 |
|---------|---------|------|------|
| `blender-game-pipeline-team-lead` | 齐活林 | 交付总监 | 拆单、调度、汇编交付包 |
| `blender-game-pipeline-modeler` | 寇豆码 | 低模建模师 | 拓扑、UV、面数规划 |
| `blender-game-pipeline-texturer` | 严过关 | PBR 材质与灯光师 | 节点编程、烘焙、灯光、贴图导出 |
| `blender-game-pipeline-rigger` | 高见远 | 绑定师与动画师 | 骨骼、蒙皮、动作、FBX 导出 |

## 适用场景

- 你已经会 Blender 基础操作，想走通"做出能进游戏引擎的资产"这条管线
- 目标引擎：Unity / Unreal / Godot（导出规范三套都覆盖）
- 资产类型：角色 / 道具 / 场景物件

## 工作流

1. **完整资产交付**：拆单 → 建模师 → 材质师 → 绑定师（仅角色） → 交付包
2. **单环节优化**：直接调对应角色（建模/材质/绑定）

## 在 WorkBuddy 中安装

**通过 marketplace（推荐）：**

```bash
/plugin marketplace add lilyco-42/blender-game-pipeline-experts
/plugin install blender-game-pipeline@blender-game-pipeline-experts
```

**直接安装（不需要 marketplace 注册）：**

```bash
/plugin install blender-game-pipeline@lilyco-42/blender-game-pipeline-experts
```

## 子 Skill

包含 `blender-pipeline-scripts` 子 skill，提供：
- 程序化批量管线编排（基于 DLR-RM/BlenderProc 思路）
- 4 个 Python 脚本：topology_check / uv_check / bake_all / export_fbx
- `batch_config.yaml` 配置模板

详见 `skills/blender-pipeline-scripts/SKILL.md`。

## 参考资源

`references/awesome-blender.md` 收录了 10 个高星 Blender 插件/工具（含 EpicGames/BlenderTools、CGCookie/retopoflow、DLR-RM/BlenderProc、cats-blender-plugin 等），按"建模/材质/绑骨/导出/数据/MCP"分类，可供选型参考。

## 头像

5 张头像由 ImageGen 自动生成（PNG 1024×1024），可用任意 PNG/JPG 手动替换。

## 许可证

MIT
