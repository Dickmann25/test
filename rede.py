from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController
from mininet.cli import CLI

class OpenFlowTopo(Topo):
    def build(self):
        s1 = self.addSwitch('s1', cls=OVSSwitch, protocols='OpenFlow13')
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)
        self.addLink(h4, s1)

if __name__ == '__main__':
    topo = OpenFlowTopo()
    net = Mininet(topo, controller=RemoteController, autoSetMacs=True)
    net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)
    net.start()
    CLI(net)
    net.stop()
