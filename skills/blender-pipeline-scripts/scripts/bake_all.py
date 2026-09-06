#!/usr/bin/env python3
"""
Batch Cycles baking for PBR texture maps.

Bakes (configurable):
- Normal map
- AO (Ambient Occlusion)
- Cavity
- Curvature
- Position
- Thickness

Usage (inside Blender):
    blender --background --python bake_all.py -- --config ./config.yaml
"""

import sys
import argparse


def parse_args():
    argv = sys.argv
    argv = argv[argv.index("--") + 1:] if "--" in argv else argv

    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--maps", nargs="+", default=["normal", "ao", "cavity"])
    parser.add_argument("--samples", type=int, default=64)
    parser.add_argument("--ray-distance", type=float, default=0.1)
    parser.add_argument("--output", default="./output/textures/")
    return parser.parse_args(argv)


def bake_map(map_type: str, samples: int, ray_distance: float, output_path: str) -> dict:
    """
    Bake one PBR map.

    Real implementation:
      1. Set Cycles as render engine
      2. Set bake_type (NORMAL, AO, etc.)
      3. Set ray_distance
      4. Select target mesh
      5. bpy.ops.object.bake(type=map_type.upper())
      6. Save image to output_path
    """
    print(f"  Baking {map_type} → {output_path}")
    return {"map": map_type, "status": "ok", "path": output_path}


def main():
    args = parse_args()
    print(f"Baking {args.maps} with samples={args.samples}, ray_distance={args.ray_distance}")

    # Real impl would iterate over assets from config.yaml
    for m in args.maps:
        bake_map(m, args.samples, args.ray_distance, f"{args.output}/{m}.png")

    print("Bake complete.")


if __name__ == "__main__":
    main()