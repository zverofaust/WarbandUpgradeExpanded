# Tomb Kings layout — complete source-data draft (2026-10-19)

All five Tomb Kings TSV tables have been updated to implement the user's final bottom-to-top diagram, including the construct and artillery branches. **Not yet compiled or validated in-game.**

## Construct and artillery upgrades

- Tomb Scorpion -> Khemric Titan
- Khemrian Warsphinx -> Necrosphinx
- Screaming Skull Catapult -> Bone Giant
- Screaming Skull Catapult -> Casket of Souls
- Bone Giant -> Hierotitan

Unit IDs were checked against Warhammer III 9.0.4 data (twdatabase.com). The new Khemric Titan requires Lords of the End Times DLC.

## Other branches

Separate unit cards and upgrade groups for skeleton infantry, cavalry, chariots, Tomb Guard, Necropolis Knights, Ushabti and their weapon variants. Two skeleton infantry variants promote to Nehekhara Warriors; both basic horsemen variants have both chariot destinations. Old chariot -> catapult upgrade remains removed.

## Validation needed

- All five tables must be imported together; importing only two leaves dangling group references.
- RPFM 5.2.0's spreadsheet Import TSV has been unreliable in the user's tests; direct table editing/pasting worked.
- Original `build.bat` still targets the removed RPFM CLI and is not a working pack builder.
- Test whether group IDs and bidirectional upgrade entries render as intended, whether x/y coordinates and UI link positions match the reference, and whether DLC-gated units appear.
- Upgrade costs and required/subtracted ranks are provisional, particularly construct paths.
- Existing Morghast unit group retained but disconnected from the reference diagram.
- The last known working test pack should be backed up before integration.

## Source references

- https://twdatabase.com/units/khemric-titan
- https://twdatabase.com/units/bone-giant
- https://twdatabase.com/units/casket-of-souls
- https://twdatabase.com/units/tomb-scorpion
- https://twdatabase.com/units/khemrian-warsphinx
- https://twdatabase.com/units/necrosphinx
- https://twdatabase.com/units/hierotitan
