#!/usr/bin/env bash

export PLATFORM=IOS

python3 -m pytest tests/ui/ -l -vv --tb=short
