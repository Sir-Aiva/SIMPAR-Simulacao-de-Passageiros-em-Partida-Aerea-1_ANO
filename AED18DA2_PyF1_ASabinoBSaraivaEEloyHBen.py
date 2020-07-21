# -*- coding: utf-8 -*-
"""
Created on Sat May 12 17:17:55 2018

@author: Bruno
"""

#imports


from random import randint
from pythonds.basic import Queue


# Principais classes a considerar -  início 

#PASSAGEIRO 
class Passageiro:
    def __init__(self,bag_pass,ciclo_in):
        self.bag_pass = bag_pass
        self.ciclo_in = ciclo_in
        
    def __str__(self):
        return '[b:' + str(self.bag_pass) + ' t:' + str(self.ciclo_in) + ']'
   
    def obtem_bag_pass(self):
        return self.bag_pass
    
    def obtem_ciclo_in(self):
        return self.ciclo_in
    
#BALCÃO 
class Balcao:
    def __init__(self,n_balcao,bag_utemp):
        self.n_balcao = n_balcao
        self.fila = Queue()
        self.inic_atend = 0
        self.passt_atend = 0
        self.numt_bag = 0
        self.tempt_esp = 0
        self.bag_utemp = bag_utemp
        
    def __str__(self):
        return '[b:' + str(self.n_balcao) + ' t:' + str(self.inic_atend)
        + ' fila:' + str(self.fila.size()) + ']'

    def muda_inic_atend(self, tempoatendimento):
        self.inic_atend += tempoatendimento
        
    def incr_passt_atend(self):
        self.passt_atend += 1
        
    def muda_numt_bag(self, bagpass):
        self.numt_bag += bagpass
    
    def muda_tempt_esp(self,t):
        self.tempt_esp += t

    def obtem_n_balcao(self):
        return self.n_balcao
    
    def obtem_fila(self):
        return self.fila
    
    def obtem_inic_atend(self):
        return self.inic_atend
    
    def obtem_passt_atend(self):
        return self.passt_atend
    
    def obtem_numt_bag(self):
        return self.numt_bag
    
    def obtem_tempt_esp(self):
        return self.tempt_esp
    
    def obtem_bag_utemp(self):
        return self.bag_utemp
    
# Principais classes a considerar -  Fim
    
#Principais funções a considerar - Início 
def mostra_balcoes(list):
    print('\n| Lista de balcões |')
    
    for b in range(len(list)):
        
        print('    '+str(list[b]))

def existem_balcoes_com_fila(list):
    
    for g in range(len(list)):
    
        if not list[g].obtem_fila().isEmpty():
        
            return True


def fila_menor(balcoes):
    
    balcaomenor = 0
    
    menorB = balcoes[0].obtem_fila().size()
    
    for indice in range(1,len(balcoes)):
        
        if balcoes[indice].obtem_fila().size() < menorB:
            
            menorB = balcoes[indice].obtem_fila().size()
            
            balcaomenor = indice 
            
    return balcaomenor

def passl(maxp,list):
    
    passtotal=0
    
    for h in range(len(list)):
        
        passtotal+=list[h].obtem_passt_atend()
        
    return (maxp-passtotal)


def atende_passageiros(tempo,balcoes):
    
    for c in range(len(balcoes)): 
        
        balcao=balcoes[c]
        
        if not balcao.obtem_fila().isEmpty():
            
            for c in range(balcao.obtem_fila().size()):
                
                p = balcao.obtem_fila().items[0]
                
                bagp = p.obtem_bag_pass()
                
                tempo_de_atendimento = tempo - balcao.obtem_inic_atend()
                
                ut_bag = bagp / balcao.obtem_bag_utemp()
                
                if ut_bag < tempo_de_atendimento:
                    
                    tempo_de_espera = tempo - p.ciclo_in
                    
                   
                    balcao.muda_inic_atend((tempo+1))
                    balcao.incr_passt_atend()
                    balcao.muda_numt_bag(bagp)
                    balcao.muda_tempt_esp(tempo_de_espera)
                    
                    balcao.obtem_fila().dequeue()
                    
                else:
                    if balcao.obtem_fila().isEmpty():
                       balcao.muda_inic_atend(tempo)
                       
#Apresenta os resultados finais
def apresenta_resultados(balcoes):
    
    print('\nFim Da Simulação: ')
    
    for k in range(len(balcoes)):
        
        balcao=balcoes[k]
        
        if balcao.obtem_passt_atend() > 0:
            
            bagpciclo = balcao.obtem_bag_utemp()
            atend = balcao.obtem_passt_atend()
            bagppass = (balcao.obtem_numt_bag()/balcao.obtem_passt_atend())
            tme = (balcao.obtem_tempt_esp()/balcao.obtem_passt_atend())
            
            print('\nO Balcão '+str(k)+' teve uma média de bagagens por ciclo de '+ str(bagpciclo) +', e '\
                  + str(atend) + ' passageiros atendidos com estimativa de bagagens: '\
                  + str(round(bagppass, 2)) +\
                  '.\nTempo: '+ str(round(tme, 2)))
        else:
            print('\n O Balcão '+ str(k) +' não despachou bagagens neste simulação')    

             
#Simulação
def simpar_simula(num_pass, num_bag, num_balcoes, ciclos):
    
    balcoes = []
    
    for i in range(num_balcoes):
        balcoes.append(Balcao(i,randint(1,num_bag)))
        i+=1
        
    for i in range(ciclos):
        
        print('\n««« CICLO nº ', i ,' »»»')
        
        atende_passageiros(i,balcoes)
        
        balcaomenor = fila_menor(balcoes)
        if passl(num_pass,balcoes)!=0:
            if (i == (ciclos)/3) or (i < (2*(ciclos))/3):
                balcoes[balcaomenor].fila.enqueue(Passageiro((randint(1,num_bag)),i))
            elif (i == (2*ciclos)/3) or (i < ciclos):
                if randint(0,100) < 80:
                    balcoes[balcaomenor].fila.enqueue(Passageiro((randint(1,num_bag)),i))
            elif (i == (ciclos)):
                if randint(0,100) < 60:
                    balcoes[balcaomenor].fila.enqueue(Passageiro((randint(1,num_bag)),i))
        
        mostra_balcoes(balcoes)
   
    ciclo_atual=ciclos
    
    while existem_balcoes_com_fila(balcoes):
 
        print('\n««« Ciclo nº '+ str(ciclo_atual) +' »»»')
    
        atende_passageiros (ciclo_atual, balcoes)
        
        mostra_balcoes(balcoes)
        ciclo_atual+=1
    apresenta_resultados(balcoes)
    
#Principais funções a considerar - Fim

#Função principal   
def simular():
    
    print("\nSimulação de Passageiros em Partida Aérea\n ")
    
    
    ciclos = int(input('Quantos ciclos para esta simulação ? '))
    num_balcoes = int(input('Número de balcões abertos? '))
    num_pass = int(input('Quantidade de passageiro com bagagens para o voo? '))
    num_bag = int(input('Quantidade máxima de bagagens estipulada ? '))
    simpar_simula(num_pass,num_bag,num_balcoes,ciclos)
    Pergunta = input("Deseja voltar a simular com outros valores?[S/N] ")
    
    if (Pergunta.upper() == 'S'):
        
        simular()
#Função principal

#Execução
if __name__ == '__main__':
    
    simular()
    