#!/usr/bin/env python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info,setLogLevel
from lib.p4_mininet import P4Switch, P4Host

import argparse
import os
import sys
from time import sleep

#sys.path.append('/home/joao/ic/Polkalyzer/lib/p4/bmv2/targets/simple_switch')

parser = argparse.ArgumentParser(description='Mininet demo')
parser.add_argument('--behavioral-exe', help='Path to behavioral executable',
					type=str, action="store", default="simple_switch")
parser.add_argument('--thrift-port', help='Thrift server port for table updates',
					type=int, action="store", default=9090)
parser.add_argument('--pcap-dump', help='Dump packets on interfaces to pcap files',
					type=str, action="store", required=False, default=False)

args = parser.parse_args()

class INTTopo( Topo ):
	"Single switch connected to n (< 256) hosts."
	def __init__(self, sw_path, thrift_port, pcap_dump, n, **opts):
		Topo.__init__( self, **opts )

		self.switch_list = []
		self.host_list = []

		info('*** Adding P4Switches (edge)\n')
		e = 2
		for h in range(e):
			switch = self.addSwitch('e%d' % (h + 1),
				sw_path = sw_path,
				json_path = 'lib/mpolka-int-edge.json',
				thrift_port = thrift_port,
				pcap_dump = pcap_dump,
				log_console = True)
			self.switch_list.append(switch)
			thrift_port = thrift_port + 1

		info('*** Adding P4Switches (core)\n')
		m = 6
		for h in range(m):
			switch = self.addSwitch('s%d' % (h + 1),
				sw_path = sw_path,
				json_path = 'lib/mpolka-int-core.json',
				thrift_port = thrift_port,
				pcap_dump = pcap_dump,
				log_console = True)
			self.switch_list.append(switch)
			thrift_port = thrift_port + 1

		info('*** Adding hosts\n')
		n = 2
		for h in range(n):
			host = self.addHost('h%d' % (h + 1),
				ip = '10.0.1.%d/24' % (h + 1),
				mac = '00:04:00:00:00:%02x' %h)
			self.host_list.append(host)

		info('*** Creating links between hosts and edge switches\n')
		for h in range(n):
			self.addLink('h%d' % (h + 1), 'e%d' % (h + 1))

		info('*** Creating links between edge and core switches\n')
		self.addLink('e1', 's4')
		self.addLink('e2', 's6')
		
		info('*** Creating links between core switches\n')
		self.addLink('s1', 's2')
		self.addLink('s2', 's5')
		self.addLink('s1', 's4')
		self.addLink('s3', 's4')
		self.addLink('s4', 's6')

def main():
	num_hosts = 2
	topo = INTTopo(args.behavioral_exe,
				args.thrift_port,
				args.pcap_dump,
				num_hosts)
	net = Mininet(topo = topo,
				host = P4Host,
				switch = P4Switch,
				controller = None)

	net.start()
	net.staticArp()
	os.system('flow_table/f.sh 2 6')

	for n in range(num_hosts):
		h = net.get('h%d' % (n + 1))
		h.describe()
		if n != 0:
			h.cmd('ethtool --offload eth0 rx off tx off')
			h.cmd('python2 ../packet/receive.py >/dev/null &')
			h.cmd('sysctl -w net.ipv6.conf.all.disable_ipv6=1')
			h.cmd('sysctl -w net.ipv6.conf.default.disable_ipv6=1')
			h.cmd('sysctl -w net.ipv6.conf.lo.disable_ipv6=1')

	for sw in net.switches:
		sw.cmd('sysctl -w net.ipv6.conf.all.disable_ipv6=1')
		sw.cmd('sysctl -w net.ipv6.conf.default.disable_ipv6=1')
		sw.cmd('sysctl -w net.ipv6.conf.lo.disable_ipv6=1')

	sleep(1)

	print( 'Ready !' )

	CLI( net )
	net.stop()



if __name__ == '__main__':
	setLogLevel( 'info' )
	main()
