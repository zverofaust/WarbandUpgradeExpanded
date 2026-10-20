#!/usr/bin/env python3
"""Stage selected RPFM TSV tables and build a Warhammer III mod pack via RPFM CLI.

Requires Python 3 and an RPFM release containing rpfm_cli.exe.
This initial builder is untested on the user's local RPFM installation.
"""
import argparse
import csv
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PACK_NAME = "warband_upgrade_expanded.pack"
TABLES = ("unit_upgrade_to_unit_groups_tables", "unit_upgrade_group_ui_links_tables")
GAME_DATA = Path(r"D:\Steam\steamapps\common\Total War WARHAMMER III\data")

def locate_cli(explicit):
    options = [explicit, os.environ.get("RPFM_CLI"), str(ROOT / "tools" / "rpfm_cli.exe"), shutil.which("rpfm_cli.exe")]
    for item in options:
        if item and Path(item).is_file():
            return str(Path(item).resolve())
    print("ERROR: rpfm_cli.exe not found. Specify --cli PATH or set RPFM_CLI.")
    sys.exit(2)

def locate_schema(explicit):
    appdata = Path(os.environ.get("APPDATA", ""))
    options = [explicit, os.environ.get("RPFM_SCHEMA"), str(appdata / "FrodoWazEre" / "rpfm" / "config" / "schemas" / "schema_wh3.ron")]
    for item in options:
        if item and Path(item).is_file():
            return str(Path(item).resolve())
    print("ERROR: Warhammer III schema not found. Specify --schema PATH or set RPFM_SCHEMA.")
    sys.exit(2)

def stage():
    folder = ROOT / "build" / "staging"
    if folder.exists():
        shutil.rmtree(folder)
    for table in TABLES:
        src = ROOT / "db" / table / "TLA_upgrade_tmb.tsv"
        if not src.is_file():
            raise RuntimeError(f"Missing source TSV: {src}")
        with src.open("r", encoding="utf-8-sig", newline="") as stream:
            rows = list(csv.reader(stream, delimiter="\t"))
        if len(rows) < 3 or not rows[1][0].startswith("#" + table + ";"):
            raise RuntimeError(f"Invalid RPFM TSV header in {src}")
        width = len(rows[0])
        for i, row in enumerate(rows[2:], 3):
            if len(row) != width:
                raise RuntimeError(f"{src}: row {i} has {len(row)} columns; expected {width}")
        # Preserve original in-pack filename. The TSV metadata describes that same path.
        dst = folder / "db" / table / src.name
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print(f"Staged {src.relative_to(ROOT)} ({len(rows)-2} rows)")
    return folder

def run(cmd):
    print("Running:", subprocess.list2cmdline([str(x) for x in cmd]), flush=True)
    subprocess.run([str(x) for x in cmd], check=True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cli", help="Path to rpfm_cli.exe")
    parser.add_argument("--schema", help="Path to schema_wh3.ron")
    parser.add_argument("--install", action="store_true", help="Copy finished pack to game data folder")
    parser.add_argument("--game-data", type=Path, default=GAME_DATA)
    args = parser.parse_args()
    cli = locate_cli(args.cli)
    schema = locate_schema(args.schema)
    staged = stage()
    out = ROOT / "dist" / PACK_NAME
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        out.unlink()
    try:
        run([cli, "--game", "warhammer_3", "pack", "create", "--pack-path", out])
        run([cli, "--game", "warhammer_3", "pack", "add", "--pack-path", out, "--folder-path", staged, "-tsv-to-binary", schema])
    except subprocess.CalledProcessError as exc:
        print(f"ERROR: RPFM CLI failed (exit code {exc.returncode}). Check your CLI version with --help.")
        return 1
    if not out.is_file() or out.stat().st_size < 64:
        print("ERROR: No nonempty pack was generated.")
        return 1
    print(f"Created {out} ({out.stat().st_size:,} bytes).")
    print("IMPORTANT: Open in RPFM to verify the two DB tables, Mod pack type and converted rows before testing.")
    if args.install:
        if not args.game_data.is_dir():
            print(f"ERROR: Game data directory not found: {args.game_data}")
            return 1
        target = args.game_data / PACK_NAME
        shutil.copy2(out, target)
        print(f"Installed: {target}")
        print("Enable the local mod and Warband Upgrade Ultimate in the game launcher.")
    else:
        print("To install after verification, rerun build.bat --install")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, RuntimeError) as exc:
        print(f"ERROR: {exc}")
        sys.exit(1)
