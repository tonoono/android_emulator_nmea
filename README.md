# android_emulator_nmea

Send a GPS log file (NMEA) via telnet (Python) to the Android emulator.

## Inspiration
I found this project [android-gps-emulator](http://code.google.com/p/android-gps-emulator/) 
and was inspired to write a script that would read a GPS log file (NMEA format) 
and send it over telnet to the android-emulator.

## NMEA messages
If you log NMEA messages, $GPRMC is the minimum needed for navigation information. 
See resources for a link to a bigger list of NMEA messages and formats

## Requirements
Python 2.7+

## Usage
    usage: android_emulator_nmea.py [options] FILE

    Send an NMEA log file to the android emulator.

    optional arguments:
      -h, --help       show this help message and exit
      --host HOST      address of telnet host, DEFAULT: localhost
      --port PORT      port of telnet host, DEFAULT: 5554
      --file FILENAME  FILE that contains NMEA data

## Links
[NMEA messages](http://www.gpsinformation.org/dale/nmea.htm#nmea)


