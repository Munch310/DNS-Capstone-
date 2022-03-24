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

def scan(t_IP, start, end, result):

    s = socket(AF_INET, SOCK_STREAM)
    for i in range(50, 52):
        conn = s.connect_ex((t_IP, i))
        if(conn == 0) :
            print ('Port %d: OPEN' % (i,))
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
배너 넣을곳

1. Port Scan
2. out bound ip frequency extraction
3. ##################################
    '''
    print ('\033[1;34m'+ banner +'\033[0m')
    print ('-'*90)

def main():
    banner()

    START, END = 0, 5
    result = Queue()
    target = input('Enter the host to be scanned: ')
    t_IP = gethostbyname(target)
    print ('Starting scan on host: ', t_IP)
    startTime = time.time()
    th1 = Process(target=scan, args=(t_IP, START, END//2, result))
    th2 = Process(target=scan, args=(t_IP, END//2, END, result))
    
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print('Time taken:', time.time() - startTime)

if __name__ == '__main__':
    main()


