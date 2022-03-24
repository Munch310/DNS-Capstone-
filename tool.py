#-*-coding:utf-8-*-

import os
from socket import *
import time
import struct
import binascii
import IPy
import sys
import gevent
import argparse
import time
import requests
import dns.resolver
from imp import reload
from gevent import monkey
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing.dummy import Lock
import threading
from multiprocessing import Process, Queue
import collections
import re

def scan(t_IP, port, start, end):

    s = socket(AF_INET, SOCK_STREAM)
    for i in range(start,end,1):
        conn = s.connect_ex((t_IP, port[i]))
        if(conn == 0) :
            print ('Port %d: OPEN' % (port[i]))
        s.close()

def out_bound_freq():
    for i in range(0,100): 
        os.system('netstat -n >> out_bound.txt')

    time.sleep(1)
    ipnPort = re.findall(r'\d+[.]\d+[.]\d+[.]\d+[:]\d+', open("out_bound.txt").read().lower())

    print("OUT BOUND ADRR"+'\t\t'+"FREQ")
    for x, y in collections.Counter(ipnPort).most_common():
        if str(x).rpartition(':')[0] == '127.0.0.1': # localhost
            pass
        else:
            print(str(x)+'\t'+str(y))

def banner():
    banner = '''
1. Port Scan
2. out bound ip frequency extraction
3. ##################################
    '''
    print ('\033[1;34m'+ banner +'\033[0m')
    print ('-'*90)

def main():
    banner()

    port=[80, 20, 21, 22, 23, 25, 53, 5357, 110, 123, 161, 443, 1433, 3306, 1521, 8080, 135, 139, 137, 138, 445, 514, 8443, 3389, 8090, 42, 70, 79, 88, 118, 156, 220]
    target = input('Enter the host or url to be scanned: ')
    t_IP = gethostbyname(target)
    print ('Starting scan on host: ', t_IP)
    startTime = time.time()
    th1 = Process(target=scan, args=(t_IP,port,0,len(port)//2))
    th2 = Process(target=scan, args=(t_IP,port,len(port)//2,len(port)))
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print('Time taken:', time.time() - startTime)
    

if __name__ == '__main__':
    main()
