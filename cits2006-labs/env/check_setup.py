"""CITS2006 Lab 0 setup check. Run inside your activated venv:  python check_setup.py"""
import importlib
import shutil
import subprocess
import sys

ok = True


def report(name, passed, hint=""):
    global ok
    ok &= passed
    print(f"[{'OK' if passed else '!!'}] {name}" + ("" if passed else f"  -> {hint}"))


report("Python 3.12 or 3.13", sys.version_info[:2] in ((3, 12), (3, 13)),
       f"you have {sys.version.split()[0]}; recreate the venv with: uv venv --python 3.13 ~/cits2006/.venv")
report("running inside a virtual environment", sys.prefix != sys.base_prefix,
       "activate it: source ~/cits2006/.venv/bin/activate")
for module in ("flask", "requests", "numpy", "pandas", "sklearn", "bcrypt", "phe"):
    try:
        importlib.import_module(module)
        report(f"python package {module}", True)
    except ImportError:
        report(f"python package {module}", False, "uv pip install -r requirements.txt")
for tool in ("git", "curl", "docker"):
    report(f"command {tool}", shutil.which(tool) is not None, f"install {tool} (see Lab 0)")
if shutil.which("docker"):
    images = subprocess.run(["docker", "image", "ls", "-q", "cits2006-env"], capture_output=True, text=True)
    if images.returncode != 0:  # the docker command ran but could not reach Docker itself
        report("Docker is running", False,
               "start Docker Desktop (or the docker service) and run this again "
               "(on Ubuntu, also check that you ran the usermod step and logged in again)")
    else:
        report("lab container cits2006-env built", bool(images.stdout.strip()), "run the docker build command in Lab 0")
print("\nAll good - you are ready for the labs." if ok else "\nFix the items marked !! and run this again.")
sys.exit(0 if ok else 1)
