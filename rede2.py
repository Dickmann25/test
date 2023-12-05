from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

def create_topology():
    net = Mininet(controller=Controller, switch=OVSSwitch)

    # Adiciona o controlador OpenFlow padrão
    c0 = net.addController('c0')

    # Adiciona o switch OpenFlow
    s1 = net.addSwitch('s1')

    # Adiciona os hosts
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')

    # Conecta os hosts ao switch
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)
    net.addLink(h4, s1)

    # Inicia a rede
    net.start()

    # Adiciona as interfaces dos controladores
    s1.start([c0])

    # Abre a interface de linha de comando para interação
    CLI(net)

    # Para limpar a rede após a execução
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_topology()
