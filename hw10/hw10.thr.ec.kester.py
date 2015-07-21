#---------------------------------------------------------
# April Dawn Kester
# akester@ischool.berkeley.edu
# Homework #10
# November 17, 2014
# Threding
#---------------------------------------------------------

import time
from IPy import IP #I refuse to parse with regex
import subprocess
from subprocess import CalledProcessError
import sys
import threading
import socket
import netifaces

ip_list = []

def get_ip():
    addrs = netifaces.ifaddresses('en0')
    for i in addrs[netifaces.AF_INET]:
        ip_address = i.get('addr')
        return ip_address

def do_something(x, args):
    try:
        subprocess.check_output(args.split(' '))
        ip_list.append([x.strNormal(), 0])
    except CalledProcessError:
        ip_list.append([x.strNormal(), 1])
    except OSError:
        ip_list.append([x.strNormal(), 1])

def main():
    starttime = time.time()
    ip_address = get_ip() #raw_input("What is your IP address: ")
    print "My IP address is " + ip_address
    try:
        ip_test = IP(ip_address)
    except ValueError:
        print "Not a valid IP address"
        sys.exit()

    ip_mask = (IP(ip_address).make_net('255.255.255.0'))
    ip = IP(ip_mask)

    thread_list = []

    for x in ip:
        args = "ping -W 3 -c 2 " + x.strNormal()
        t = threading.Thread(target=do_something, args = (x, args))
        thread_list.append(t)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    new_ip_list = sorted(ip_list, key=lambda item: socket.inet_aton(item[0]))

    for i, k in new_ip_list:
        if k == 0:
            s = " is reachable"
        if k == 1:
            s = " is unreachable"
        print i + s

    finishtime = time.time()
    print "Elapsed time is ", (finishtime - starttime)

if __name__ == "__main__":
    main()