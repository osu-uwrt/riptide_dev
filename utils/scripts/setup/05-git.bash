#!/bin/bash

# Create Alias to Pull All Submodules
git config --add alias.pull-all "submodule update --recursive --remote --merge"

# Ignore submodule changes for parent repo
git config --add diff.ignoreSubmodules all

# Fetch Multiple Submodules at once using "reasonable default"
git config --add submodule.fetch 0
git config --add fetch.parallel 0

# Setup Submodules
git submodule update --init --remote --recursive --merge

wd=${PWD}
# Old Git includes Key and Value with regexp so filter value with grep
paths=$(git config --get-regexp -f .gitmodules submodule.*.path | grep -Eo '\S*$')

# Reattach HEAD to branch
for path in ${paths}; do
    branch=$(git config --get -f .gitmodules submodule.${path}.branch)

    cd ${path}
    git checkout ${branch}
    cd ${wd}
done
