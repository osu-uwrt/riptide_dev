#!/bin/bash

scripts=${UWRT_PATH}/utils/scripts/source/*.bash
uwrt_scripts=${UWRT_PATH}/utils/uwrt-cli/source/*.bash

for script in ${scripts}; do
    source ${script}
done

for script in ${uwrt_scripts}; do
    source ${script}
done
