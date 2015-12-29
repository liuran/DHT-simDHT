#!/usr/bin/python
#coding=utf-8
"""
magnet:?xt=urn:btih:B298DD7E3BF7B300FF1F235B90FD5441002FE440
magnet:?xt=urn:btih:506F4F0BE4D982E2E45711B7FA9BD4B03D3908CF
magnet:?xt=urn:btih:2F2D9E0C41B0CDB7B5B565532C3DB4F8EDB61E01
magent:?xt=urn:btih:A0A5DA0B0EEA900ACE855D885931416575424C49
"""

import sys, os, urllib
from btdht import Parser

def magnet_to_bt(magnet_address):
  beg = magnet_address.rfind(':')
  str = magnet_address[beg+1:]
  b_word = str[0:2]
  e_word = str[-2:]
  bt_address = 'http://bt.box.n0808.com/' + b_word + '/' + e_word + '/' + str + '.torrent'
  return bt_address

if __name__ == '__main__':

  if len(sys.argv) > 2:
    print("Usage:\n\t%s \nor\n\t%s [read from stdin]" % (sys.argv[0], sys.argv[0]))
    sys.exit()

  if len(sys.argv) == 2:
    magnet = sys.argv[1]
    if -1 == magnet.find(':'):
      sys.exit('invalid magnet address')

    bt_url = magnet_to_bt(magnet)
    os.system("wget " + bt_url)
    
    pos = bt_url.rfind('/')
    file_name = bt_url[pos+1:]

    parser = Parser.Parser(file_name)
    print parser.getName()
    print parser.getEncoding()


  else:
      
    for line in sys.stdin:
      if -1 == line.find(':'):
        continue
        
    url = magnet_to_bt(line[0:-1])
    pos = url.rfind('/')
    file_name = url[pos+1:]
    urllib.urlretrieve(url, file_name)
