#!/bin/bash
if [[ $EUID -ne 0 ]]; then echo 'This script must be run as root' ; exit 1 ; fi
NO='\033[0;33m' ; OK='\033[0;32m' ; NC='\033[0m'
