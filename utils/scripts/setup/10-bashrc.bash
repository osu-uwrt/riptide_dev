#!/bin/bash

export UWRT_PATH="${PWD}"
# Create .bashrc entries
echo "export UWRT_PATH=${PWD}" >> ~/.bashrc
echo 'source ${UWRT_PATH}/utils/source.bash' >> ~/.bashrc
