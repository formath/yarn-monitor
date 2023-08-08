#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import os
import time
import app_resource

cur_timestamp = int(round(time.time() * 1000))
print('============================================================================================================================================================================================')
print('========================= app id ========================= app name ================================ app type ================= running hours ================== resource ==================')
for line in sys.stdin:
  line = line.strip('\t\n ')  
  try:
    tokens = line.split('\t')
    app_id = tokens[0].split('>')[1].split('<')[0]
    if not app_id.startswith('application'):
      continue
    app_name = tokens[1].strip('"')
    app_type = tokens[2].strip('"')
    app_start_timestamp = int(tokens[3].strip('"'))
    time_period = (cur_timestamp - app_start_timestamp + 10 * 60 * 1000) * 1.0 / 1000 / 60 / 60
    if time_period > 400000:
      continue
    status = tokens[4]
    url = tokens[5]
    queue = tokens[6]
    if status.strip('"') == 'RUNNING':
      resource = app_resource.get_resource(url.split("='")[1].split("'>")[0])
    else:
      resource = ''
    log_info = '{:25}\t{:80}\t{:10}\t{:20}\t{:20}'.format(app_id, app_name, app_type, time_period, resource)
    print(log_info)
    if queue == 'root.zz01.hadoop-mining.ad-online' and (app_type == 'SPARK' or app_type == 'MAPREDUCE'):
      print('spark/mr job found. kill it now!')
      #os.system("/opt/mt/hadoop/bin/yarn application -kill %s" % (app_id))
  except:
    continue
print('============================================================================================================================================================================================')
