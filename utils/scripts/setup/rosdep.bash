#!/bin/bash

# Install dependencies for dependencies
uwrt rosdep dependencies/src

# Install software dependencies
uwrt rosdep software/src
