#!/bin/bash
if [[ $EUID -ne 0 ]]; then echo 'This script must be run as root' ; exit 1 ; fi
NOCOLOR='\033[0m'
GREEN='\033[0;32m'
RED='\033[0;33m'
BLUE='\033[0;34m'
CURRENT=$(dirname $(readlink -f $0))
[ -z $ROOTDIR ] && PWD=$(dirname `dirname $CURRENT`) || PWD=$ROOTDIR

#-----------------------------------------------------------------------------------------
echo -e "\n${BLUE}Installing Nodejs + Yarn...${NOCOLOR}"
#-----------------------------------------------------------------------------------------
! [[ -z $(which nodejs) ]] && echo -e "${BLUE}Already installed...${NOCOLOR}" && exit 1

# Install packages
#-----------------------------------------------------------------------------------------
apt update -qq ; apt full-upgrade -yqq ; apt -yqq install xxxxxxxxxxxxxxxx

# Configure packages
#-----------------------------------------------------------------------------------------