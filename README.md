# vcs-sync

https://wiki.mozilla.org/ReleaseEngineering/How_To/VCSSync#Machines

https://docs.mozilla-releng.net/projects/mapper.html

## Testing vcs-sync

1. Create a file "vcssync.env" containing variables with taskcluster auth
   credentials:

    ```
    RELENGAPI_INSERT_HGGIT_MAPPINGS_TASKCLUSTER_CLIENT_ID=project/releng/services/mapper/bug1555970
    RELENGAPI_INSERT_HGGIT_MAPPINGS_TASKCLUSTER_ACCESS_TOKEN=tokenstring
    ```

2. Run the test script
    ```
    ./test.sh
    ```
    * clones mozharness
    * run in python2.7 in a docker container
    * converts build-tools hg repo to git
    * tests pushing mappings to stage.mapper
    
