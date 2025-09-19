#!/bin/bash

if [[ -e ~/.setup ]]; then
    echo "Setup has already been ran"
fi

touch ~/.setup

# Install Click for uwrt cli
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-click python3-termcolor python3-pip

# Install Packages that aren't shipped in devcontainer
sudo apt install -y fuse3 openssh-client

# Install Supported RMWs
sudo apt install -y ros-humble-rmw-zenoh-cpp ros-humble-rmw-fastrtps-cpp

# Add utils to path
export PATH=${PWD}/utils/bin:${PATH}

for script in ./utils/scripts/setup/*.bash; do
    source $script
done
