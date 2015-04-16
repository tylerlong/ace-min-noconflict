import json
from fabric.api import local


def update():
    local('rm -rf *.js')
    local('rm -rf snippets')
    local('wget https://github.com/ajaxorg/ace-builds/archive/master.zip')
    local('unzip master.zip && rm master.zip')
    f = open('ace-builds-master/package.json')
    latest_version = json.loads(f.read())['version']
    print 'latest version: {0}'.format(latest_version)
    local('cp -r ace-builds-master/src-min-noconflict/* .')
    local('rm -rf ace-builds-master/')
    local('rm worker-*')
