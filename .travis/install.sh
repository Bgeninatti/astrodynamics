#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    brew update || brew update
    brew install pyenv
    brew outdated pyenv || brew upgrade pyenv

    if which -s pyenv; then
        eval "$(pyenv init -)"
    fi

    case "${TOXENV}" in
        py27)
            curl -O https://bootstrap.pypa.io/get-pip.py
            python get-pip.py --user
            ;;
        py33)
            pyenv install 3.3.6
            pyenv global 3.3.6
            ;;
        py34)
            pyenv install 3.4.3
            pyenv global 3.4.3
            ;;
        py35)
            pyenv install 3.5.0
            pyenv global 3.5.0
            ;;
    esac
    pyenv rehash
    python -m pip install --user virtualenv
else
    pip install virtualenv
fi

python -m virtualenv ~/.venv
source ~/.venv/bin/activate
pip install tox codecov
