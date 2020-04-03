#!/usr/bin/env python3

import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: Enter a domain name\nExample: DomainStalker.py google.com")
    sys.exit(1)

print( ' ')    
print("\033[94mAuthor: Warren Vos <info@redmoonsecurity.com>")
print("GitHub: https://github.com/RedMoon-Security/Headerrabber\033[m")
    
print( ' ')
print( '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print( '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print( '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print( '@@@@@@@                                                                                                         @@@@@@@')
print( '@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@             @@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@               @@@@@@@')
print( '@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@          @@@@@@@')
print( '@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@')
print( '@@@@@@@   @@@@@@@@@         @@@@@@@@@@@      @@@@@@@@@                       @@@@@@@@@       @@@@@@@@@@@@@@     @@@@@@@')
print( '@@@@@@@   @@@@@@@@@           @@@@@@@@@@     @@@@@@@@@                       @@@@@@@@@           @@@@@@@@@@@    @@@@@@@')
print( '@@@@@@@   @@@@@@@@@           @@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@             @@@@@@@@@    @@@@@@@')
print( '@@@@@@@   @@@@@@@@@       @@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@             @@@@@@@@@@   @@@@@@@')
print( '@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@             @@@@@@@@@,   @@@@@@@')
print( '@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@           @@@@@@@@@                       @@@@@@@@@            @@@@@@@@@@    @@@@@@@')
print( '@@@@@@@   @@@@@@@@@    @@@@@@@@@@@           @@@@@@@@@                       @@@@@@@@@          @@@@@@@@@@@     @@@@@@@')
print( '@@@@@@@   @@@@@@@@@      @@@@@@@@@@@         @@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@')
print( '@@@@@@@   @@@@@@@@@        @@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@')
print( '@@@@@@@   @@@@@@@@@         @@@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@            @@@@@@@')
print( '@@@@@@@                                                                                                         @@@@@@@')
print( '@@@@@@@                                                                                                         @@@@@@@')
print( '@@@@@@@                                                                                                         @@@@@@@')
print( '@@@@@@@   @@@@@@@           @@@@@@@            @@@@@@@@@@                  @@@@@@@@@@           @@@@@@@         @@@@@@@')
print( '@@@@@@@   @@@@@@@@@        @@@@@@@@        @@@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@       @@@@@@@@@       @@@@@@@')
print( '@@@@@@@   @@@@@@@@@@     @@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@     @@@@@@@')
print( '@@@@@@@   @@@@@@@@@@@@ @@@@@@@@@@@@    @@@@@@@@          @@@@@@@    @@@@@@@          @@@@@@@    @@@@@@@@@@@@@   @@@@@@@')
print( '@@@@@@@   @@@@@@&@@@@@@@@@@@@@@@@@@    @@@@@@@            @@@@@@@  @@@@@@@            @@@@@@@   @@@@@@@@@@@@@@@ @@@@@@@')
print( '@@@@@@@   @@@@@@& @@@@@@@@@  @@@@@@    @@@@@@@            @@@@@@@  @@@@@@@            @@@@@@@   @@@@@@@  @@@@@@@@@@@@@@')
print( '@@@@@@@   @@@@@@&   @@@@@    @@@@@@    @@@@@@@@          @@@@@@@    @@@@@@@          @@@@@@@@   @@@@@@@    @@@@@@@@@@@@')
print( '@@@@@@@   @@@@@@&     @@     @@@@@@     @@@@@@@@@@    @@@@@@@@@      @@@@@@@@@    @@@@@@@@@     @@@@@@@      @@@@@@@@@@')
print( '@@@@@@@   @@@@@@&            @@@@@@       @@@@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@      @@@@@@@        @@@@@@@@')
print( '@@@@@@@   @@@@@@&            @@@@@@           @@@@@@@@@@@@                @@@@@@@@@@@@          @@@@@@@          @@@@@@')
print( '                                                                                                                       ')
print( '                                                                                                                       ')
print( ' @@@@@@@        @@@@@@@@         @@@@@@@@        @@@   @@@        @@@@@@@@@        @@@       @@@@@@@@@        @@@  @@@ ')
print( '@@@@@@          @@@@@@@@        @@@              @@@   @@@        @@@    @@@       @@@          @@@            @@@@@@  ')
print( '     @@@@       @@@             @@@              @@@   @@@        @@@@@@@          @@@          @@@              @@    ')
print( '@@@@@@@@        @@@@@@@@@        @@@@@@@@         @@@@@@@         @@@   @@@        @@@          @@@              @@    ')
    

print("\n\033[94mGetting Header for: " + sys.argv[1])
print('-' * 50, '\033[m')

req = requests.get("https://" + sys.argv[1])
print(str(req.headers))

gethostby = socket.gethostbyname(sys.argv[1])
print("\n\033[94mGetting the IP Address of: " + sys.argv[1])
print('-' * 50, '\033[m')
print("\n" + gethostby)

#ipinfo.io

req_two = requests.get("https://ipinfo.io/" + gethostby + "/json")
resp = json.loads(req_two.text)

print("\n\033[94mGetting the Regional Info of: " + sys.argv[1]) 
print('-' * 50, '\033[m')
print("\nCity: " + resp["loc"])
print("Region: " + resp["region"])
print("Country: " + resp["country"])
print("Location: " + resp["loc"])
print("Postal Code: " + resp["postal"])
print("Timezone: " + resp["timezone"])
print(" ")
