# Tomb Kings layout — first implementation pass

Source: user's final revised bottom-to-top diagram (2026-10-19). This is a **partial implementation**, not a validated playable pack.

## Implemented in five TLA_upgrade_tmb TSV tables

- Separate database groups for Skeleton Warriors, Spearmen, Archers, Horsemen, Horse Archers, Nehekhara Warriors, Nehekhara Horsemen, Chariots, Archer Chariots, Tomb Guard variants, Necropolis Knights variants, Ushabti variants, and Screaming Skull Catapult.
- Preserve original Morghast group as a disconnected legacy entry.
- Wide, bottom-to-top coordinates with lower-tier skeleton units at y=760, middle tier y=520, Tomb Guard at y=300 and advanced units at y=100.
- Infantry and cavalry progressions and bidirectional weapon-variant upgrades.
- Both Skeleton Warriors and Skeleton Spearmen can promote to Nehekhara Warriors.
- Both Skeleton Horsemen and Skeleton Horse Archers can promote to Chariots and Archer Chariots.
- Existing Skeleton Chariot to Screaming Skull Catapult upgrade remains removed.

## Outstanding

- Identify authoritative WH3 land-unit keys for Tomb Scorpion, Khemric Titan, Khemrian Warsphinx, Necrosphinx, Bone Giant, Hierotitan, and Casket of Souls. Do not guess keys.
- Add those units, their groups, coordinates, and intended upgrade chains, including Screaming Skull Catapult -> Bone Giant and -> Casket of Souls.
- Verify RPFM DB table override behavior, source table import, game interpretation of split groups, and the UI's position and link direction semantics.
- Original RPFM CLI build.bat remains nonfunctional with RPFM 5.2.0; do not rely on it.

## Manual integration caution

This pass modifies **five** Tomb Kings TSV tables, not the previous two. A pack created from an older snapshot must have all five tables updated together. A mixed old/new pack will reference nonexistent groups. Keep a backup of the last known working pack until this layout is validated.
