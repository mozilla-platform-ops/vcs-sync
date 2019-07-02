#!/bin/bash

git clone https://github.com/mozilla/release-services.git
hg clone https://hg.mozilla.org/build/mozharness

docker-compose up || \
    printf "# vcssync.env must contain variables like:
RELENGAPI_INSERT_HGGIT_MAPPINGS_TASKCLUSTER_CLIENT_ID=project/releng/services/mapper/bug1555970
RELENGAPI_INSERT_HGGIT_MAPPINGS_TASKCLUSTER_ACCESS_TOKEN=tokenstring\n"

