#!/bin/bash

files=$(grep -o '\S*$' .source_files)

for file in $files; do
    source $file
done
