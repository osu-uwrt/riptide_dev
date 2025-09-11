#!/bin/bash

# Create .bashrc entries
echo "export UWRT_PATH=${PWD}" >> ~/.bashrc
echo 'source ${UWRT_PATH}/utils/source.bash' >> ~/.bashrc
