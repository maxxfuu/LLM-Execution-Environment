# Potential Packages & Dependencies multiprocessing, threading, logging, 

import subprocess, os 

sandbox_directory = "/Users/maxfu/Desktop/AI/Research/LLM-Execution-Environment"
os.chdir(sandbox_directory) 

def execute_in_sandbox(command): 
    try: 
        result =subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
        if result.returncode == 0: 
            return result.stdout.decode().strip()
        else:
            return f"Error executing command: {result.stderr.decode().strip()}"
    except subprocess.TimeoutExpired: 
        return "Error: Command Timed Out" 
    
output = execute_in_sandbox("ls")
print(output)