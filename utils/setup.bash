#!/bin/bash

if [[ -e ~/.setup ]]; then
    echo "Setup has already been ran"
fi

touch ~/.setup

# Install Click for uwrt cli
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-click python3-termcolor python3-pip

# Add utils to path
export PATH=${PWD}/utils/bin:${PATH}

for script in ./utils/scripts/setup/*.bash; do
    bash $script
done
