#!/usr/bin/env bash

grep -ir --extended-regexp --exclude-dir=.git --exclude-dir=.pixi 'template.*rust|template.*python'
