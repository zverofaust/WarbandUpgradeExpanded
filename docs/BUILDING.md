# Experimental Tomb Kings build

This first builder is committed but has **not been tested on your Windows PC**.

Requirements: Python 3, `rpfm_cli.exe` (RPFM's separate command-line tool), and an up-to-date Warhammer III `schema_wh3.ron`.

Double-click `build.bat` in the repository root. It stages the two modified Tomb Kings TSV tables, creates a new pack, and imports the tables as binary. Output: `dist/warband_upgrade_expanded.pack`.

If CLI or schema discovery fails, run from a terminal:
```bat
build.bat --cli "C:\path\to\rpfm_cli.exe" --schema "C:\path\to\schema_wh3.ron"
```

Open the output in RPFM before installation; confirm it is type **Mod** and has the two expected DB tables with correctly decoded rows. After validation, `build.bat --install` copies the pack to `D:\Steam\steamapps\common\Total War WARHAMMER III\data`.

Enable the new pack and Warband Upgrade Ultimate in the launcher. **Important:** load-order and DB override behavior, particularly the deleted chariot upgrade, are not yet validated. Do not assume successful conversion means the game has applied every change.

RPFM CLI syntax varies by version. If it fails, share the error and CLI help output so the script can be adapted.
