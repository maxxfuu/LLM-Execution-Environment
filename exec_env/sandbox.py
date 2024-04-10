# Potential Packages & Dependencies multiprocessing, threading, logging, 
import subprocess
import os

untrusted_script = "./dummy_code.py"

# Prepare the execution environment for the separate user
# (e.g., set up the file system, resource limits, security policies)

# Execute the untrusted script in a separate process
try:
    subprocess.run(["python3", untrusted_script],
                  check=True, timeout=10)
except subprocess.CalledProcessError as e:
    print(f"Error executing the untrusted script: {e}")
except subprocess.TimeoutExpired:
    print("Untrusted script timed out") 