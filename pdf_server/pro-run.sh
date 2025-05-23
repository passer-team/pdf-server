#!/bin/bash
SHELL_FOLDER=$(dirname "$0")
cd "${SHELL_FOLDER}/.."
cd "${SHELL_FOLDER}"
pipenv run python3 main.py
