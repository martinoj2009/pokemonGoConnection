#!/usr/bin/python3
import socket
import urllib.request
import os
import datetime


#Check to see if the server is available
def is_connected():
  try:
      #Try to connect to nvidia's site
    host = socket.gethostbyname("sso.pokemon.com")
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False


def main():
    if is_connected() == False:
        print("POKEMON GO DOWN!")
        f = open('/var/www/html/pokemon.html', 'w')
        f.write('<title>Pokemon GO Status</title>\n')
        f.write('<h1>POKEMON GO IS DOWN</h1>\n')
        f.write('TIME: ' + datetime.datetime.now().time().isoformat())

    else:
        print("POKEMON GO UP!")
        f = open('/var/www/html/pokemon.html', 'w')
        f.write('<title>Pokemon GO Status</title>\n')
        f.write('<h1>POKEMON GO IS UP</h1>\n')
        f.write('TIME: ' + datetime.datetime.now().time().isoformat())

if __name__ == '__main__':
    main()