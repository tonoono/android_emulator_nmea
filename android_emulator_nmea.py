#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telnetlib
import time
import argparse 
import sys

def main():
  parser = argparse.ArgumentParser(description='Send an NMEA log file to the android emulator.', usage='%(prog)s [options] FILE')
  parser.add_argument('--host', dest='host', default="localhost", help="address of telnet host, DEFAULT: localhost")
  parser.add_argument('--port', dest='port', default="5554", help="port of telnet host")
  parser.add_argument('--file', dest='filename', help="FILE that contains NMEA data")
  args = parser.parse_args()
  
  tn = telnetlib.Telnet(args.host,args.port)
  file = open(args.filename,"r")

  print "Sending %s to Android Emulator at %s:%s" % (args.filename,args.host,args.port)
  i = 0
  for line in file:
    sys.stdout.write('\r')
    # send the nmea 
    tn.write("geo nmea " + line)
    if i % 4 == 0:
      sys.stdout.write('|')
    elif i % 4 == 1:
      sys.stdout.write('/')
    elif i % 4 == 2:
      sys.stdout.write('-')
    elif i % 4 == 3:
      sys.stdout.write('\\')

    sys.stdout.flush()
    # provide a small delay
    time.sleep(0.25)
    i += 1

  sys.stdout.write('\r ')
  print "... Done."

if __name__ == "__main__":
    main()

