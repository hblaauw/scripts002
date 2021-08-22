#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Testje

import psycopg2
import sys

con = None

try:
    con = psycopg2.connect("host='themis' dbname='athena' user='logrtp' password='st03ph03r'")
    cur = con.cursor()
    cur.execute('SELECT version()')
    version = cur.fetchone()[0]
    print(version)

except psycopg2.DatabaseError as e:
    print ('Error %s') % e
    sys.exit(1)

finally:
    if con:
        con.close()
