import sys
import subprocess

# Default values
default_size = "1336x768"
default_password = "Academy_student_AD!"

# Parse arguments
if len(sys.argv) < 2:
    print("Usage: python rdp.py <host> [size] [password]")
    sys.exit(1)

host = sys.argv[1]

# Use custom size if provided, else default
size = sys.argv[2] if len(sys.argv) > 2 else default_size

# Use custom password if provided, else default
password = sys.argv[3] if len(sys.argv) > 3 else default_password

# Prepare the command
command = f"xfreerdp /u:htb-student /p:'{password}' /v:{host} /size:{size}"

# Run the command
try:
    subprocess.run(command, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running xfreerdp: {e}")
