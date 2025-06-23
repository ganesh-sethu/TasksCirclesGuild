import subprocess
import os

def ping_domain(domain):
    
    #nt stands for windows os
    if os.name == "nt":
        param = "-n"
    else:
        param = "-c"
    
    cmd = ['ping', param, '1', domain]

    try:
        #using subprocess.run to execute the ping command
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        
        if result.returncode == 0:
            return f"{domain} is UP and running"
        else:
            return f"{domain} is DOWN and inactive"
    except FileNotFoundError:
        return "Ping command not found. Ensure it's in your Path"
    except Exception as e:
        return f"Error pinging {domain}: {e}"
    

domain_file = "./domains.txt"

try:
    with open(domain_file, 'r') as f:
        domains = [line.strip() for line in f if line.strip()]
    
    for domain in domains:
        print(ping_domain(domain))
        
except FileNotFoundError:
    print(f"Error: Domain list file '{domain_file}' not found.")

except Exception as e:
    print(f"An error occurred: {e}")
    