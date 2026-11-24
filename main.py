import os
from pathlib import Path

ENTRY = "Introducing QueueBack, the app that sells your place in line to the person behind you, then texts you when you reach the front: that's your cue to start over."

out = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")
