import os
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
for sub in ("analysis/variant_verification", "analysis/panel_bam_checks", "scripts"):
    sys.path.insert(0, os.path.join(ROOT, sub))
