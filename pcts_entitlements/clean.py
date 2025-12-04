import shutil, os

for root, dirs, files in os.walk("."):
    for f in files:
        if f.endswith((".pyc", ".pyo")):
            os.remove(os.path.join(root, f))
    for d in dirs:
        if d == "__pycache__":
            shutil.rmtree(os.path.join(root, d))