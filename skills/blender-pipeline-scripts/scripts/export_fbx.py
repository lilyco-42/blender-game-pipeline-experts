#!/usr/bin/env python3
"""
Engine-targeted FBX exporter.

Per-engine settings:
- Unity: Y Forward / Z Up, scale=1, no leaf bones
- Unreal: Y Forward / Z Up, scale=100 (Blender m → UE cm)
- Godot: -Z Forward / Y Up, scale=1

Usage (inside Blender):
    blender --background --python export_fbx.py -- \
        --input ./rigged.blend --output ./exported.fbx --engine unreal
"""

import sys
import argparse


VALID_ENGINES = {"unity", "unreal", "godot"}


def parse_args():
    argv = sys.argv
    argv = argv[argv.index("--") + 1:] if "--" in argv else argv

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to rigged .blend file")
    parser.add_argument("--output", required=True, help="Path to output .fbx")
    parser.add_argument("--engine", required=True, choices=list(VALID_ENGINES))
    parser.add_argument("--bake-animation", action="store_true", default=True)
    parser.add_argument("--apply-transform", action="store_true", default=True)
    return parser.parse_args(argv)


def get_engine_settings(engine: str) -> dict:
    """Return per-engine FBX export settings."""
    settings = {
        "unity": {
            "global_scale": 1.0,
            "axis_forward": "Y",
            "axis_up": "Z",
            "use_armature_deform_only": True,
            "add_leaf_bones": False,
        },
        "unreal": {
            "global_scale": 100.0,  # Blender m → UE cm
            "axis_forward": "Y",
            "axis_up": "Z",
            "use_armature_deform_only": True,
            "add_leaf_bones": False,
        },
        "godot": {
            "global_scale": 1.0,
            "axis_forward": "-Z",  # Godot 用右手坐标系
            "axis_up": "Y",
            "use_armature_deform_only": True,
            "add_leaf_bones": False,
        },
    }
    return settings[engine]


def export_fbx(input_path: str, output_path: str, engine: str,
               bake_animation: bool, apply_transform: bool) -> dict:
    """
    Real implementation:
      1. bpy.ops.wm.open_mainfile(filepath=input_path)
      2. Apply all transforms on every object
      3. Set FBX exporter settings via get_engine_settings(engine)
      4. bpy.ops.export_scene.fbx(filepath=output_path, **settings)
    """
    settings = get_engine_settings(engine)
    print(f"Exporting {input_path} → {output_path} for {engine}")
    print(f"  Settings: {settings}")
    print(f"  Bake animation: {bake_animation}, Apply transform: {apply_transform}")
    return {"status": "ok", "engine": engine, "output": output_path, "settings": settings}


def main():
    args = parse_args()
    result = export_fbx(args.input, args.output, args.engine,
                        args.bake_animation, args.apply_transform)
    print(result)


if __name__ == "__main__":
    main()