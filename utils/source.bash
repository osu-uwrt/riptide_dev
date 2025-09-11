#!/bin/bash

scripts=${UWRT_PATH}/utils/scripts/source/*.bash

for script in ${scripts}; do
    source ${script}
done
