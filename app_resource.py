#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup

def get_resource(url):
  html = urllib.urlopen(url).read()
  soup = BeautifulSoup(html, features="html.parser")

  # kill all script and style elements
  for script in soup(["script", "style"]):
    script.extract()    # rip it out

  # get text
  text = soup.get_text()

  # break into lines and remove leading and trailing space on each
  lines = (line.strip() for line in text.splitlines())
  # break multi-headlines into a line each
  chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
  # drop blank lines
  text = '\n'.join(chunk for chunk in chunks if chunk)
  #print(text)

  cpu = 0
  memory = 0
  gpu = 0
  app_info_block = ''

  begin = False
  for line in text.split('\n'):
    if not begin and line != u"任务数量":
      continue
    elif not begin:
      begin = True
      continue
    if line != u"任务信息":
      app_info_block = app_info_block + '\n' + line
    else:
      break
  #print(app_info_block)
  tokens = app_info_block.strip('\n').split('\n')
  for i in range(0, len(tokens)/8):
    memory += int(tokens[8 * i + 4].replace(',', ''))
    cpu += int(tokens[8 * i + 5])
    gpu += int(tokens[8 * i + 6]) 
  result = 'memory:' + str(memory) + ' cpu:' + str(cpu) + ' gpu:' + str(gpu)
  return result
