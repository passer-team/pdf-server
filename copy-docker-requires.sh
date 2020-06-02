#! /bin/bash
SHELL_FOLDER="`dirname $0`"
cd "${SHELL_FOLDER}"
echo "script location: ${SHELL_FOLDER}"
cd docker/workplace
rm -rf pdf-generator templates Pipfile*
cd ../..
cp -r pdf-generator templates Pipfile* docker/workplace