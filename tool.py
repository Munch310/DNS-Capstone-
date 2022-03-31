#-*-coding:utf-8-*-
import sys
import os
from socket import *
import time
from bs4 import BeautifulSoup

import collections
import re
from math import ceil 
from sig import *
import itertools
import argparse

# 1 포트스캔 (1분 정도 소요?)
def scan():
    
    port=[80, 20, 21, 22, 23, 25, 53, 5357, 110, 123, 161, 443, 1433, 3306, 1521, 8080, 135, 139, 137, 138, 445, 514, 8443, 3389, 8090, 42, 70, 79, 88, 118, 156, 220]
    start = 0
    end = len(port)

    target = input('Enter the ip or url : ')
    t_IP = gethostbyname(target)

    print ('Starting scan on host: ', t_IP)

    startTime = time.time()

    s = socket(AF_INET, SOCK_STREAM) 
    for i in range(start,end,1):
        conn = s.connect_ex((t_IP, port[i])) 
        if(conn == 0) :
            print ('Port %d IS OPEN!' % (port[i]))
        s.close() 

    print('Time taken:', time.time() - startTime)

# 2 out_bound 통신 처리
# 현재 localhost에서 어디랑 제일 통신을 많이 하는지 확인
def out_bound_freq():
    for i in range(0,100): 
        os.system('netstat -n >> ../out_bound.txt') # netstat 명령어 써서 현재 outbound 하는 패킷 가져와서 텍스트로 저장

    time.sleep(1)
    ipnPort = re.findall(r'\d+[.]\d+[.]\d+[.]\d+[:]\d+', open("../out_bound.txt").read().lower()) # 위에서 가져온거 ip만 읽음

    print("OUT BOUND ADRR"+'\t\t'+"FREQ") 
    for x, y in collections.Counter(ipnPort).most_common(): # x는 주소 찾고 y는 갯수
        if str(x).rpartition(':')[0] == '127.0.0.1': # localhost이면 패스
            pass
        else:
            print(str(x)+'\t'+str(y))

def banner(): 
    banner = '''
1. Port Scan
2. out bound ip frequency extraction
3. file extraction
    '''
    print ('\033[1;34m'+ banner +'\033[0m')
    print ('-'*90)

def main():
    banner()
    scan()

    

if __name__ == '__main__':
    main()
