#!/bin/bash

files=$(grep -o '\S*$' ${UWRT_PATH}/utils/uwrt-cli/source/.source_files)

for file in $files; do
    source $file
done
