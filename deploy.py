from pathlib import Path
import sys
import os
import shutil

exclude = [
    ".git",
    ".gitkeep",
    "CNAME",
    "404.html",
    "README.md",
    "css",
    "images",
    "js",
]

target = Path.cwd().parent / "mindviewllc.github.io"

def unknown(item):
    print("UNKNOWN ITEM: {}".format(item))
    sys.exit(1)

for item in target.iterdir():
    if item.name in exclude:
        continue
    print("removing {}".format(item.name))
    # if item.is_file():
    #     item.unlink()
    # elif item.is_dir():
    #     shutil.rmtree(item)
    # else:
    #     unknown(item)

print("end of test")
sys.exit()

for src in (Path.cwd() / "public").iterdir():
    print("copying {}".format(src.name))
    if src.is_file():
        shutil.copy(src, target)
    elif src.is_dir():
        shutil.copytree(src, target / src.name)
    else:
        unknown(src)

CNAME = Path.cwd() / "CNAME"
if CNAME.exists():
    print("copying CNAME")
    shutil.copy(CNAME, target)
