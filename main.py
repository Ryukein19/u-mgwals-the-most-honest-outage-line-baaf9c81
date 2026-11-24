import os
# One-liner entry (160 chars max): the line below is the whole submission.
# Output goes to /output/entry.txt.
LINE = "We are down. The database is down, the backups are down, and the status page you're reading is the only thing still alive."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
