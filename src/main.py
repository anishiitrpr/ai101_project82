import subprocess
import sys
import time

def run_script(script_path):
    print(f"\nRunning: {script_path}")
    start_time = time.time()
    
    result = subprocess.run([sys.executable, script_path], capture_output=False)
    
    if result.returncode != 0:
        print(f"\nError encountered while executing {script_path}. Execution stopped.")
        sys.exit(result.returncode)
        
    elapsed = time.time() - start_time
    print(f"Finished {script_path} successfully in {elapsed:.2f} seconds.\n")

if __name__ == "__main__":
    print("Starting Renewable Energy ML Pipeline...")
    
    pipeline_scripts = [
        "src/preprocessing.py",
        "src/visualization.py",
        "src/model.py"
    ]
    
    for script in pipeline_scripts:
        run_script(script)
        
    print("Entire pipeline executed successfully.")