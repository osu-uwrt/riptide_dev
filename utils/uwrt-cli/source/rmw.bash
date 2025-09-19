#!/bin/bash

export RMW_IMPLEMENTATION=rmw_zenoh_cpp
export ZENOH_ENDPOINTS=
export ZENOH_SHM=false
export ZENOH_CONFIG_OVERRIDE="connect/endpoints=[${ZENOH_ENDPOINTS}];transport/shared_memory/enabled=${ZENOH_SHM}"