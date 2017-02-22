import time, os, sys, svn_config

dist = svn_config.setting['dist']
# os.chdir(svn_config.setting['svn'])

def checkout():
    cmd = 'svn checkout %(url)s %(dist)s --username %(user)s --password %(pwd)s' % svn_config.setting
    print "execute %s" % cmd
    try:
	return os.system(cmd)
    except:
        return "fail"

