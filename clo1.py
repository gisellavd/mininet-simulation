# 1301204469 - Gisella Vania D
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.link import TCLink

def runTopo():
	net = Mininet()
	
	# add host
	h1 = net.addHost('h1')
	h2 = net.addHost('h2')
	r1 = net.addHost('r1')
	r2 = net.addHost('r2')
	r3 = net.addHost('r3')
	r4 = net.addHost('r4')
	
	# add link
	net.addLink(h1, r1, intfName1='h1-eth0', intfName2='r1-eth0', cls=TCLink, bw=1)
	net.addLink(r1, r3, intfName1='r1-eth1', intfName2='r3-eth1', cls=TCLink, bw=0.5)
	net.addLink(h2, r3, intfName1='h2-eth0', intfName2='r3-eth0', cls=TCLink, bw=1)
	net.addLink(h2, r4, intfName1='h2-eth1', intfName2='r4-eth1', cls=TCLink, bw=1)
	net.addLink(r4, r2, intfName1='r4-eth0', intfName2='r2-eth0', cls=TCLink, bw=0.5)
	net.addLink(r2, h1, intfName1='r2-eth1', intfName2='h1-eth1', cls=TCLink, bw=1)
	net.addLink(r3, r2, intfName1='r3-eth2', intfName2='r2-eth2', cls=TCLink, bw=1)
	net.addLink(r1, r4, intfName1='r1-eth2', intfName2='r4-eth2', cls=TCLink, bw=1)
	
	net.start()
	
	# config IP
	h1.cmd('ifconfig h1-eth0 192.130.0.1 netmask 255.255.255.0')
	h1.cmd('ifconfig h1-eth1 192.130.5.2 netmask 255.255.255.0')
	
	h2.cmd('ifconfig h2-eth0 192.130.2.2 netmask 255.255.255.0')
	h2.cmd('ifconfig h2-eth1 192.130.3.1 netmask 255.255.255.0')
	
	r1.cmd('ifconfig r1-eth0 192.130.0.2 netmask 255.255.255.0')
	r1.cmd('ifconfig r1-eth1 192.130.1.1 netmask 255.255.255.0')
	r1.cmd('ifconfig r1-eth2 192.130.7.1 netmask 255.255.255.0')
	
	r2.cmd('ifconfig r2-eth0 192.130.4.2 netmask 255.255.255.0')
	r2.cmd('ifconfig r2-eth1 192.130.5.1 netmask 255.255.255.0')
	r2.cmd('ifconfig r2-eth2 192.130.6.2 netmask 255.255.255.0')
	
	r3.cmd('ifconfig r3-eth0 192.130.2.1 netmask 255.255.255.0')
	r3.cmd('ifconfig r3-eth1 192.130.1.2 netmask 255.255.255.0')
	r3.cmd('ifconfig r3-eth2 192.130.6.1 netmask 255.255.255.0')
	
	r4.cmd('ifconfig r4-eth0 192.130.4.1 netmask 255.255.255.0')
	r4.cmd('ifconfig r4-eth1 192.130.3.2 netmask 255.255.255.0')
	r4.cmd('ifconfig r4-eth2 192.130.7.2 netmask 255.255.255.0')
	
	# config router
	r1.cmd('sysctl net.ipv4.ip_forward=1')
	r2.cmd('sysctl net.ipv4.ip_forward=1')
	r3.cmd('sysctl net.ipv4.ip_forward=1')
	r4.cmd('sysctl net.ipv4.ip_forward=1')
	
	CLI(net)
	net.stop()
	
if __name__=='__main__':
	setLogLevel('info')
	runTopo()
	
	
	
	
