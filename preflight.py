import json, sys
d = "design/"
W = json.load(open(d+"weapons.json"))
A = json.load(open(d+"audio.json"))
H = json.load(open(d+"granny-hooks.json"))
audio_ids = {r["id"] for r in A["rows"]}
weapon_ids = {r["id"] for r in W["rows"]}
out = []
unfilled = []
broken = []

for sheet, name in ((W,"weapons"),(A,"audio"),(H,"granny-hooks")):
    for r in sheet["rows"]:
        for c in sheet["columns"]:
            v = r.get(c)
            if v is None:
                unfilled.append(f"{name}.{r['id']}.{c}")
            if name == "audio" and c == "verified" and v is False:
                unfilled.append(f"{name}.{r['id']}.verified (sound event name is a guess)")

for r in W["rows"]:
    for c in ("soundFire","soundReload","soundEquip","soundDry"):
        v = r[c]
        if v not in ("none", None) and v not in audio_ids:
            broken.append(f"weapons.{r['id']}.{c} -> '{v}' not in audio sheet")
for r in H["rows"]:
    for s in r["usesSound"]:
        if s not in audio_ids: broken.append(f"hooks.{r['id']}.usesSound -> '{s}' not in audio sheet")
    for w in r["usesWeapon"]:
        if w not in weapon_ids: broken.append(f"hooks.{r['id']}.usesWeapon -> '{w}' not in weapons sheet")

print(f"rows: weapons={len(W['rows'])} audio={len(A['rows'])} hooks={len(H['rows'])}")
print(f"unresolved references: {len(broken)}")
for b in broken: print("  BROKEN", b)
print(f"unfilled or unverified cells: {len(unfilled)}")
from collections import Counter
cnt = Counter(u.split(".")[0] + "." + u.split(".")[2].split(" ")[0] for u in unfilled)
for k,v in sorted(cnt.items()): print(f"  {k}: {v}")
