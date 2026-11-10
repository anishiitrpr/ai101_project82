import subprocess
import sys
import os

def run_script(script_path, root_dir):
    print(f"\n--- Running: {os.path.basename(script_path)} ---")
    # cwd=root_dir ensures the scripts always find the data/ folder correctly
    result = subprocess.run([sys.executable, script_path], cwd=root_dir, capture_output=False)
    if result.returncode != 0:
        print(f"Failed to run {os.path.basename(script_path)}")
        sys.exit(1)

if __name__ == "__main__":
    # Get the directory where this main.py is located (src/)
    src_dir = os.path.dirname(os.path.abspath(__file__))
    # Get the main project folder (one level up from src/)
    root_dir = os.path.dirname(src_dir)
    
    scripts = [
        os.path.join(src_dir, "preprocessing.py"),
        os.path.join(src_dir, "visualization.py"),
        os.path.join(src_dir, "model.py")
    ]
    
    for script in scripts:
        run_script(script, root_dir)
        
    print("\nAll steps completed successfully!")
