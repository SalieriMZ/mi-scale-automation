import subprocess
import sys

def install_dependencies():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "bleak==0.21.1"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "black==23.10.1"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "isort==5.12.0"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "ruff==0.1.3"])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")
        sys.exit(1)

def run_script():
    try:
        subprocess.check_call([sys.executable, "scan.py"])
    except subprocess.CalledProcessError as e:
        print(f"Failed to run script: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_dependencies()
    run_script()