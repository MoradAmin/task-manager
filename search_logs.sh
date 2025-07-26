#!/bin/bash
# search_logs.sh - Search for a pattern in log files
pattern=$1
if [ -z "$pattern" ]; then
  echo "Usage: $0 <pattern>"
  exit 1
fi
grep -Rin "$pattern" /var/log
