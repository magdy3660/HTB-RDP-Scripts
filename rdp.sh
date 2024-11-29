#!/bin/bash

# Default values
DEFAULT_SIZE="1336x768"
DEFAULT_PASSWORD="Academy_student_AD!"

# Check if host is supplied
if [ -z "$1" ]; then
  echo "Usage: rdp.sh <host> [size] [password]"
  exit 1
fi

HOST=$1

# If the user provided a custom size, use it; otherwise, use the default size
SIZE=${2:-$DEFAULT_SIZE}

# If the user provided a custom password, use it; otherwise, use the default password
PASSWORD=${3:-$DEFAULT_PASSWORD}

# Run the xfreerdp command
xfreerdp /u:htb-student /p:"$PASSWORD" /v:$HOST /size:$SIZE

