#!/usr/bin/env bash

export PLATFORM=ANDROID

python3 -m pytest tests/ui/ -l -vv --tb=short
