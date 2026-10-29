import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s", 
)
logger = logging.getLogger("ingestor")

INPUT_DIR = "/data/input"
OUTPUT_FILE = "/data/ingested.txt"

def ingest():
    content = ""
    files_processed = 0
    for fileName in sorted(os.listdir(INPUT_DIR)):
        filePath = os.path.join(INPUT_DIR, fileName)
        if os.path.isfile(filePath):
            try:
                with open(filePath, "r", encoding="utf-8") as f:
                    content += f"\n-- {fileName} ---\n"
                    content += f.read()
                    content += "\n"
                    files_processed += 1
            except Exception as e:
                logger.error(f"Error reading file {fileName}: {e}")

    if files_processed == 0:
        logger.warning("No input files found in /data/input")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write(content)

    logger.info(f"Ingested {files_processed} files -> {OUTPUT_FILE}")

if __name__ == "__main__":
    ingest()