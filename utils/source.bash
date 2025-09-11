#!/bin/bash

scripts=${UWRT_PATH}/utils/scripts/source/*.bash

for script in ${scripts}; do
    echo Sourcing ${script}
    source ${script}
done
