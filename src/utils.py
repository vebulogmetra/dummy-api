import os
from src.settings import SCRIPTS_DIR, INIT_DB_SCRIPT


def initdb():
    try:
        import subprocess

        subprocess.run(["bash", os.path.join(SCRIPTS_DIR, INIT_DB_SCRIPT)])
    except Exception as e:
        print("[x] Init db error: ", e)
