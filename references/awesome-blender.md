# Awesome Blender 插件 / 工具索引

> 建模师 / 材质师 / 绑定师选型时的参考目录。来源：agmmnn/awesome-blender（7,286⭐）及相关高星仓库。

## 建模（拓扑 / Retopo / 硬表面）

| 插件 | Stars | 用途 | 适合角色 |
|------|-------|------|---------|
| CGCookie/retopoflow | 3,218 | 手绘 retopo（Polystrips / Strokes / Contours） | 建模师 |
| BoxCutter / HardOps | — | 硬表面布尔 + 卡边 | 建模师 |
| Quad Remesher | — | 自动四边面重拓扑 | 建模师 |
| hlorus/CAD_Sketcher | 3,407 | 参数化约束几何（草图建模） | 建模师 |

## 材质 / 贴图 / 烘焙

| 插件 | Stars | 用途 | 适合角色 |
|------|-------|------|---------|
| carson-katri/dream-textures | 8,197 | Stable Diffusion 生成 base color 贴图 | 材质师 |
| Cycles / Eevee（内置） | — | GPU/CPU 渲染 + 烘焙 | 材质师 |

## 绑定 / 动画 / 导入

| 插件 | Stars | 用途 | 适合角色 |
|------|-------|------|---------|
| Rigify（内置） | — | Blender 自动人形骨骼模板 | 绑定师 |
| Mixamo Auto-Rigger | — | 一键骨骼绑骨 + 动作库 | 绑定师 |
| absolute-quantum/cats-blender-plugin | 4,088 | Mixamo / MMD / Rigify / XNALara / DAZ 多源模型清洗与重定向 | 绑定师 |
| animate1978/MB-Lab | 2,024 | Blender 4.0+ 角色自动生成 | 建模师 + 绑定师 |
| EpicGames/BlenderTools | 3,287 | Blender→Unreal 导出（骨骼命名 / 碰撞体 / LOD） | 绑定师 |

## 引擎对接 / 导出

| 插件 | Stars | 用途 | 适合角色 |
|------|-------|------|---------|
| EpicGames/BlenderTools | 3,287 | UE Send-to-Unreal 完整桥 | 绑定师 |
| xavier150/Blender-For-UnrealEngine-Addons | 2,652 | 完整 Unreal 导入（动画 / 相机 / 碰撞 / Sequencer） | 绑定师 |
| nutti/fake-bpy-module | 1,808 | Blender Python API stub（IDE 自动补全） | 任意 |

## 数据 / 程序化生成

| 插件 | Stars | 用途 | 适合角色 |
|------|-------|------|---------|
| DLR-RM/BlenderProc | 3,699 | Python 程序化批量管线（合成数据） | 主理人（用于批量管线） |
| JacquesLucke/animation_nodes | 2,378 | 节点化动画 / 运动图形 | 绑定师 |
| domlysz/BlenderGIS | 9,349 | GIS 数据 → Blender（地形 / 城市 / OSM） | 主理人（场景资产） |

## MCP / AI 控制 Blender

| 插件 | Stars | 用途 | 适合角色 |
|------|-------|------|---------|
| ahujasid/blender-mcp | 27,187 | LLM 直接操控 Blender（via MCP） | 主理人（自动化） |

---

## 选型原则

1. **角色资产**：retopoflow（建模）+ cats-blender-plugin（绑骨）+ EpicGames/BlenderTools（UE 导出）这一套是工业级标配
2. **道具资产**：BoxCutter（硬表面建模）+ Cycles 烘焙（材质）+ Quad Remesher（自动 retopo）足够覆盖 90% 场景
3. **场景资产**：BlenderGIS（地形 / 城市）+ BlenderProc（批处理）+ armory3d / UPBGE（实时引擎）
4. **AI 自动化**：优先 blender-mcp 接入 WorkBuddy 的 MCP，让 Agent 直接操控 Blender

## 维护建议

每季度 review 一遍 stars 数量变化；stars < 500 且超过 6 个月没更新的插件考虑替换。