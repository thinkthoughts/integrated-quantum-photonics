from pathlib import Path

def find_root() -> Path:
    cwd = Path.cwd().resolve()
    if cwd.name == "notebooks":
        return cwd.parent
    if (cwd / "notebooks").exists():
        return cwd
    return cwd

ROOT = find_root()
FIGURES_DIR = ROOT / "figures"
RESULTS_DIR = ROOT / "results"
CSV_DIR = RESULTS_DIR / "csv"
JSON_DIR = RESULTS_DIR / "json"

def ensure_dirs():
    for path in [FIGURES_DIR, RESULTS_DIR, CSV_DIR, JSON_DIR]:
        path.mkdir(parents=True, exist_ok=True)
    return ROOT
