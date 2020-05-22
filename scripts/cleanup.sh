#!/usr/bin/env bash

set -euo pipefail

/home/ahellwig/anaconda3/envs/ashhellwig-python/bin/python setup.py develop -u

declare egginfodir
egginfodir='/home/ahellwig/src/github.com/ashellwig/implementations/ashhellwig-python/ashhellwig_python.egg-info'

if [[ -d "${egginfodir}" ]]; then
    echo "Removing egg-info directory..."
    rm -rf "${egginfodir:?}"
    echo "Removed egg-info dir."
else
    echo "The egg-info directory is not present."
fi

declare sitepackagesdir
sitepackagesdir='/home/ahellwig/anaconda3/envs/ashhellwig-python/lib/python3.8/site-packages/ashhellwig-python.egg-link'

if [[ -d "${sitepackagesdir}" ]]; then
    echo "Removing site package dir..."
    rm -rf "${sitepackagesdir:?}"
    echo "Removed site package dir."
else
    echo "The site package directory is not present."
fi
