#!/usr/bin/env bash
pip3 install pipenv

# there is an issue https://github.com/pypa/pipenv/issues/2092
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

pipenv install --three --ignore-pipfile
