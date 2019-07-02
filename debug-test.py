import os
import socket
hostname = socket.gethostname()

build_repos = (
    'mozharness',
)

conversion_repos = []
remote_targets = {}

for repo in build_repos:
    conversion_repos.append({
        "repo": "https://hg.mozilla.org/build/%s" % repo,
        "repo_name": "build-%s" % repo,
        "conversion_dir": "build-%s" % repo,
        "targets": [{
            "target_dest": "build-%s-github" % repo,
            "force_push": True
        }],
        "vcs": "hg",
        "test_mappings": 1,
        "mapper": {
            "url": "https://stage.mapper.mozilla-releng.net",
            "project": "build-%s" % repo,
        },
        "branch_config": {
            "branches": {
                "default": "master",
            },
            "branch_regexes": [
                "^.*$"
            ]
        },
# Bug 1036819 - build/* repos currently not able to push tags to github
# temporarily disable tags in conversion.
# When bug 1020613 is resolved, this tag_config below can be enabled again.
#       "tag_config": {
#           "tag_regexes": [
#               "^.*$"
#           ]
#       },
    })
    remote_targets["build-%s-github" % repo] = {
        "repo": "git@github.com:davehouse/build-%s.git" % repo,
        #"ssh_key": "~/.ssh/github-id_rsa",
        "vcs": "git",
    }

config = {
    "log_name": "build-repos",
    "log_max_rotate": 99,
    "job_name": "build-repos",
    "env": {
        "PATH": "%(PATH)s:/usr/libexec/git-core",
        "PIP_TRUSTED_HOST": "pypi.pub.build.mozilla.org pypi.python.org pypi.org",
    },

    "conversion_repos": conversion_repos,
    "remote_targets": remote_targets,
    "virtualenv_cache_dir": "./mozharness_deps/",
    "virtualenv_modules": [
        "dulwich==0.9.0",
        "ordereddict==1.1",
        "hg-git==0.4.0-moz2",
        "mapper==0.1",
        "mercurial==3.7.3",
        "mozfile==0.9",
        "mozinfo==0.5",
        "mozprocess==0.11",
        "requests==2.8.1",
    ],
    "find_links": [
        "http://pypi.pub.build.mozilla.org/pub",
        "https://pypi.python.org/simple"
    ],
    #"pip_index": False,

    "default_notify_from": "developer-services+%s@mozilla.org" % hostname,
    "notify_config": [{
        "to": "dhouse@mozilla.com",
        "failure_only": False,
        "skip_empty_messages": False,
    }],

    # Disallow sharing, since we want pristine .hg and .git directories.
    "vcs_share_base": None,
    "hg_share_base": None,

    # any hg command line options
    "hg_options": (
        "--config",
        "web.cacerts=/etc/ssl/certs/ca-certificates.crt",
        #"web.cacerts=/etc/pki/tls/certs/ca-bundle.crt"
    ),

    "default_actions": [
        #'list-repos',
        #'create-virtualenv',
        #'update-stage-mirror',
        #'update-work-mirror',
        'publish-to-mapper',
        #'push',
        'combine-mapfiles',
        #'notify',
    ],
}
