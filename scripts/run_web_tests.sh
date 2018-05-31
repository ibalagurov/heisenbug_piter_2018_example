#!/usr/bin/env bash

export PLATFORM=WEB

python3 -m pytest tests/ui/ -l -vv --tb=short
