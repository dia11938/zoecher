# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################


def loadpl(type,source,parameters):
  if not parameters:
    return
  try:
    fp = file(PLUGIN_DIR + '/' + parameters+'.py')
    exec fp in globals()
    fp.close()
    reply(type,source,u'Ok')
  except:
    raise

register(loadpl, Prefix+'loadpl', 9)
