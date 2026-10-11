# Granny: Armed Escape (Granny x Counter-Strike 2)

Single-player mashup. The player is in Granny (host, role "primary"). Counter-Strike 2 is a companion (role "companion"): its weapons and sounds are read from the player's own CS2 install at runtime and never shipped. Melty installs no loader for CS2 and never mods it, so it is never launched.

## Design (decided with the author)
- Escape Granny's house as usual, with CS2 weapons and sounds.
- Guns can put Granny down for good. She stays down once her health reaches zero.
- First minute: start with the knife, find the first gun and ammo soon after. Every shot makes noise Granny hears.
- First version: one house, knife, Glock-18, Desert Eagle, Nova, AK-47, ammo hidden around the house.
- License: MIT (mod code only). Others may remix it.

## Status
Design sheets only. Nothing is built, tested, uploaded or published, and no Melty lookups have been made.

| Sheet | File | Rows |
|---|---|---|
| Weapons | design/weapons.json | 5 |
| Audio | design/audio.json | 17 |
| Granny hooks | design/granny-hooks.json | 7 |
| Draft listing | design/listing.json | n/a |

Preflight (design/preflight.py, result in design/preflight-result.txt): 0 broken references, 50 unfilled or unverified cells. All 50 need the games' real files:
- audio.cs2VpkPath and audio.verified (34): CS2 sound event names are guesses until read from the VPK.
- granny-hooks.hookTarget (7): needs Granny's code inspected.
- weapons.cs2ViewModel (5) and weapons.pickupLocation (4): need CS2's models and Granny's house scene.

## Known risks to settle on the PC
1. Granny has no loader in Melty's catalog, so the mod loader (likely BepInEx for a Unity game, Mono or IL2CPP build decided by the game's files) must be bundled in the release, credited, if its license allows. one_click_check decides whether that reaches one-click play.
2. Reading CS2 sounds and models at runtime needs a Source 2 archive reader inside the mod (candidate: SteamDatabase's ValveResourceFormat; confirm its license). Sounds first, models second. No look-alike stand-in models: if models can't be read at runtime, agree the change with the author first.
3. Granny's AI hearing: reuse the game's own noise input if it has one.

## Run order on a machine with Melty and both games
1. Connect to Melty. Call game_info for both games and search_mashups; call mashup_info on the closest result.
2. Find both install folders. Inspect Granny (engine build, existing mod support, noise and AI classes).
3. Fill the sheets from the real files, preflight until clean, then build the plugin.
4. Test in the running game (shoot, reload, Granny reacts, Granny stays down).
5. inspect_package, validate_recipe, one_click_check, create_mod, upload, submit_release, real screenshot, test_release, then ask before publish.
