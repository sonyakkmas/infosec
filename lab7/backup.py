#!/usr/bin/env python3
import tarfile
from datetime import datetime
from pathlib import Path

BASE = Path("/home/sonya/dev/auca/infosec/infosec")
SOURCE = BASE / "data"
DEST = BASE / "backups"
KEEP = 5

DEST.mkdir(exist_ok=True)
stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
archive = DEST / f"backup_{stamp}.tar.gz"

with tarfile.open(archive, "w:gz") as tar:
    tar.add(SOURCE, arcname=SOURCE.name)

old = sorted(DEST.glob("backup_*.tar.gz"))[:-KEEP]
for f in old:
    f.unlink()

print(f"{datetime.now():%F %T} created {archive.name}, removed {len(old)} old")
