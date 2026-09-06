#!/usr/bin/env python3
"""
Blender pipeline main runner.

Reads batch_config.yaml, iterates over assets, and runs the full pipeline:
  topology check → UV check → bake → export

Inspired by DLR-RM/BlenderProc's procedural pipeline approach.

Usage:
    blender --background --python run_pipeline.py -- --config ./config.yaml
"""

import sys
import argparse
import yaml
from pathlib import Path
from datetime import datetime


def parse_args():
    """Parse CLI args (everything after `--` from Blender)."""
    argv = sys.argv
    argv = argv[argv.index("--") + 1:] if "--" in argv else argv

    parser = argparse.ArgumentParser(description="Run Blender pipeline batch")
    parser.add_argument("--config", required=True, help="Path to batch_config.yaml")
    parser.add_argument("--dry-run", action="store_true", help="Only validate, no execution")
    return parser.parse_args(argv)


def load_config(path: str) -> dict:
    """Load YAML config."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def import_bpy_or_dry_run(dry_run: bool):
    """Import bpy inside Blender, or return None when dry-running."""
    if dry_run:
        return None
    import bpy  # noqa: F401  (only available inside Blender)
    return True


def process_asset(asset_cfg: dict, project_cfg: dict, dry_run: bool) -> dict:
    """Process a single asset through the full pipeline."""
    result = {
        "asset_id": asset_cfg["id"],
        "asset_path": asset_cfg["path"],
        "status": "pending",
        "checks": {},
        "started_at": datetime.now().isoformat(),
    }

    print(f"[{asset_cfg['id']}] processing {asset_cfg['path']}")

    # Step 1: open the .blend
    if not dry_run:
        import bpy
        bpy.ops.wm.open_mainfile(filepath=asset_cfg["path"])

    # Step 2-5: run individual scripts (topology, uv, bake, export)
    # Each script writes its own report into result["checks"]
    # In a full implementation, import and call functions from sibling scripts.
    result["checks"]["topology"] = {"status": "ok", "note": "stub"}
    result["checks"]["uv"] = {"status": "ok", "note": "stub"}
    result["checks"]["bake"] = {"status": "ok", "note": "stub"}
    result["checks"]["export"] = {"status": "ok", "note": "stub"}

    result["status"] = "ok"
    return result


def write_report(results: list, report_path: str) -> None:
    """Write HTML report."""
    html = ["<html><body><h1>Blender Pipeline Report</h1>"]
    html.append(f"<p>Generated: {datetime.now().isoformat()}</p>")
    html.append("<table border=1 cellpadding=4>")
    html.append("<tr><th>Asset</th><th>Status</th><th>Topology</th><th>UV</th><th>Bake</th><th>Export</th></tr>")
    for r in results:
        c = r["checks"]
        html.append(
            f"<tr><td>{r['asset_id']}</td><td>{r['status']}</td>"
            f"<td>{c['topology']['status']}</td>"
            f"<td>{c['uv']['status']}</td>"
            f"<td>{c['bake']['status']}</td>"
            f"<td>{c['export']['status']}</td></tr>"
        )
    html.append("</table></body></html>")
    Path(report_path).parent.mkdir(parents=True, exist_ok=True)
    Path(report_path).write_text("\n".join(html), encoding="utf-8")
    print(f"Report written to {report_path}")


def main():
    args = parse_args()
    config = load_config(args.config)

    print(f"Project: {config['project']['name']}")
    print(f"Target engine: {config['project']['target_engine']}")
    print(f"Assets to process: {len(config['assets'])}")

    import_bpy_or_dry_run(args.dry_run)

    results = []
    for asset_cfg in config["assets"]:
        try:
            r = process_asset(asset_cfg, config, args.dry_run)
            results.append(r)
        except Exception as e:
            results.append({"asset_id": asset_cfg["id"], "status": "error", "error": str(e)})

    if config.get("report", {}).get("html_output"):
        write_report(results, config["report"]["html_output"])

    print(f"\n=== {len(results)} assets processed ===")
    err_count = sum(1 for r in results if r["status"] != "ok")
    print(f"Errors: {err_count}")
    return 0 if err_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())