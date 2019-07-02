#!/bin/bash

git clone https://github.com/mozilla/release-services.git
hg clone https://hg.mozilla.org/build/mozharness

docker-compose up
