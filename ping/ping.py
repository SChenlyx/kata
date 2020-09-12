#!/home/schenlyx/anaconda3/bin/python3

import os
import threading

netaddr = "192.168.252."

def ping_test(netaddr, ip):
	"针对一台主机的ping探测"
	data = os.system("ping -c2 -i0.2 -W2 %s%s > /dev/null" %(netaddr, ip))

	if (data == 0):
		print("%s%s is \033[32mup\033[0m"%(netaddr, ip))
	else:
		print("%s%s is \033[31mdown\033[0m" %(netaddr, ip))

if __name__ == "__main__":
	for ip in range(1,255):
		t = threading.Thread(target=ping_test,args=(netaddr,ip))
		t.start()
