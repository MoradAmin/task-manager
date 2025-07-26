#!/bin/bash
# backup.sh - Backup a directory to a zip file
dir_to_backup=${1:-"./"}
timestamp=$(date +"%Y%m%d_%H%M%S")
zip_file="backup_$timestamp.zip"
zip -r $zip_file $dir_to_backup
