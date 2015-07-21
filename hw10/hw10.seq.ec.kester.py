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
import netifaces

def get_ip():
    addrs = netifaces.ifaddresses('en0')
    for i in addrs[netifaces.AF_INET]:
        ip_address = i.get('addr')
        return ip_address

def do_something(x, args):
    try:
        subprocess.check_output(args.split(' '))
        print x.strNormal() + " is reachable"
    except CalledProcessError as e:
        print x.strNormal() + " is unreachable"


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
    for x in ip:
        args = "ping -W 3 -c 2 " + x.strNormal()
        do_something(x, args)

    finishtime = time.time()
    print "Elapsed time is ", (finishtime - starttime)

if __name__ == "__main__":
    main()