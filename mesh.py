from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI

#Cria uma classe encarregada de definir a estrutura da topologia.
class MinhaTopologia(Topo):
    def build(self):
        #Adicona hosts a topologia.
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        #Adiciona switch a topologia.
        s1 = self.addSwitch('s1')

        #adiciona link entre os hosts e os switch.
        self.addLink(h1,s1)
        self.addLink(h2,s1)
        self.addLink(h3,s1)
        self.addLink(h4,s1)

if __name__ == '__main__':
    #Cria uma instância de uma topologia personalizada chamada MinhaTopologia.
    topo = MinhaTopologia()

    #Instancia que inicializa o objeto mininet configurando a rede virtual.
    net = Mininet(Topo)

    #Inicializa os switches e hosts virtuais conforme especificado pela topologia e coloca a rede em funcionamento.
    net.start()

    #Abre uma interface de linha de comando (CLI) para interagir com a rede Mininet em execução.
    CLI(net)

    #Após interagir com a rede por meio da CLI, esta linha encerra a rede Mininet, encerrando os switches e hosts virtuais.
    net.stop()
