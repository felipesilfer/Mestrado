#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import argparse
from random import randrange as rand

def printCache(pagina,cache,pageHit=False,index=None):
	
	print "\n%s -> [" % (pagina),
	for j in range(len(cache)):# printa cada posicao do cache na tela
		if cache[j] != None: 
			print cache[j],
		
		else:
			print "-", # printa cache vazio na tela

	if pageHit:
		print "] (hit)", #printa page hit

	else:
		print "] (page fault)", #printa page fault

	if index!=None:
		print "- Posicao aleatoria: %d" % index, #printa valor aleatorio do indice no algoritmo RANDOM


def fifo(tamanhoCache, paginas):
	faltas = 0
	cache = [None] * tamanhoCache

	print "\nAlgoritmo FIFO\n\n",

	for i in range(len(paginas)): # percorre todas as paginas
		pageHit = False
		for j in range(len(cache)):# verifica se pagina ja existe no cache
			if(cache[j] == paginas[i]):
				pageHit = True #caso exista, marca page hit
				break
				
		if pageHit == False: # se o valor corrente nao for page hit, entao e page fault
			cache[faltas % len(cache)] = paginas[i]
			faltas+=1
			printCache(paginas[i],cache,pageHit) #printa page fault

		else: # senao o valor e page hit
			printCache(paginas[i],cache,pageHit) #printa page hit

	percent = ((faltas * 100)/len(paginas))
	print "\n\nTotal de Page Faults : %d (%d%%)" % (faltas, percent),
	print "\n\nTotal de Page Hits : %d (%d%%)" % (len(paginas)-faltas,100-percent)


def lru(tamanhoCache, paginas):

	faltas=0
	cache = [None] * tamanhoCache
	stack = []

	print "\nAlgoritmo LRU\n\n",

	for i in range(len(paginas)): # percorre todas as paginas
		pageHit = False
		for j in range(len(cache)):# verifica se pagina ja existe no cache
			if cache[j] == paginas[i]:
				pageHit = True #caso exista, marca page hit
				stack += [stack.pop(stack.index(cache[j]))] #remove o valor de hit para o topo do stack, usando o indice do cache[j], pois o valor existe no stack
				break

		if i < len(cache): #preenche o cache enquanto houver espaço vazio
			cache[faltas % len(cache)] = paginas[i]
			faltas+=1
			stack.append(paginas[i]) 
			printCache(paginas[i],cache,pageHit) #printa page fault inicial

		elif pageHit == False: # se o valor corrente nao for page hit, entao e page fault
			cache[cache.index(stack[0])] = paginas[i]
			faltas+=1
			stack.pop(0)
			stack.append(paginas[i])
			printCache(paginas[i],cache,pageHit) #printa page fault

		else: # senao o valor e page hit
			printCache(paginas[i],cache,pageHit) #printa page hit

	percent = ((faltas*100)/len(paginas))
	print "\n\nTotal de Page Faults : %d (%d%%)" % (faltas, percent),
	print "\n\nTotal de Page Hits : %d (%d%%)" % (len(paginas)-faltas,100-percent)


def random(tamanhoCache, paginas): #paginas e um vetor com os valores das paginas de memória. cache e o cache
	faltas = 0
	cache = [None] * tamanhoCache
	index = None

	

	print "\nAlgoritmo RANDOM\n\n",

	for i in range(len(paginas)): # percorre todas as paginas
		pageHit = False
		for j in range(len(cache)): # verifica se pagina ja existe no cache
			if(cache[j] == paginas[i]):
				pageHit = True #caso exista, marca page hit
				break

		if i < len(cache): #preenche o cache enquanto houver espaço vazio
			cache[faltas % len(cache)] = paginas[i]
			faltas+=1
			printCache(paginas[i],cache,pageHit) #printa page fault inicial

		elif pageHit == False: # se o valor corrente nao for page hit, entao e page fault
			index = rand(len(cache))
			cache[index] = paginas[i]
			faltas+=1
			printCache(paginas[i],cache,pageHit,index) #printa page fault

		else: # senao o valor e page hit
			printCache(paginas[i],cache,pageHit) #printa page hit

	percent = ((faltas * 100)/len(paginas))
	print "\n\nTotal de Page Faults : %d (%d%%)" % (faltas, percent),
	print "\n\nTotal de Page Hits : %d (%d%%)" % (len(paginas)-faltas,100-percent)


def main():

	# parse dos argumentos
	opt=['fifo', 'lru', 'random']
	parser = argparse.ArgumentParser(description="Simulador de Algoritmos de substituicao de pagina")
	parser.add_argument("doc", metavar="DOCUMENTO", type=argparse.FileType(), help="Arquivo contendo as paginas da memoria")
	parser.add_argument("-alg", metavar="A", type=str, choices=opt, default=opt[2] ,required = False, help="Algoritmo a ser executado (%(choices)s)")
	parser.add_argument("-cache", metavar="C", type=int, default=0, required=False, help="Numero de quadros do cache (default = 20 porcento do tamanho do vetor de paginas)")

	argumentos = vars(parser.parse_args()) #recebe uma biblioteca de argumentos
	paginas = argumentos["doc"].readlines() #le o documento e cria um vetor onde cada posicao eh uma linha do arquivo

	for i in range(len(paginas)):
		paginas[i]=paginas[i].strip('\n')
		paginas[i]=paginas[i].strip('\r')

	if argumentos["cache"] <= 0:
		tamanhoCache = len(paginas)*20/100
	else:
		tamanhoCache = argumentos["cache"]

	algoritmos = { 
		"fifo" : fifo,
		"lru": lru,
		"random": random
	}

	print paginas

	chamarAlgoritmo = algoritmos[argumentos["alg"]]

	chamarAlgoritmo(tamanhoCache, paginas)

if __name__ == "__main__":
	main()