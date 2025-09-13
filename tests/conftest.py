import os, sys

# project_root = .../week-2-assignment-1-rsvp-manager-notyouradhee
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Ensure both the root and src are importable
sys.path.insert(0, project_root)
sys.path.insert(0, os.path.join(project_root, "src"))
