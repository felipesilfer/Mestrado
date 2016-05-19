# Simulador de algorítimos de substituição de página
---
**Autores:** Felipe Ferreira e Guilherme Alves
  
  
  ### Requisitos:
  + Python 2.7
 

### Algoritmos suportados:
+ FIFO
+ LRU
+ RANDOM

### Comandos:

##### sintaxe:
pageReplacement.py [-h] [-alg A] [-cache C] DOCUMENTO

##### Argumentos obrigatórios:
  DOCUMENTO  --  Arquivo **.TXT* contendo as páginas da mémoria em formato alfanumérico.

##### Argumentos opcionais:  
  -h, --help --------- Página de ajuda  
  -alg A ------------- Algoritmo a ser executado (fifo, lru, random) (default = random)
  -cache C ----------- Número de quadros do cache (default = 20 porcento do tamanho do vetor de páginas)
  
### Formatação do documento de entrada
O documento deve armazenar 1 posição de memória por linha.  
  
  *Exemplo:*

dados.txt  

---
7  
0  
1  
2  
0  
3  
0  
4  
2  
3  
0  
3  
2  
1  
2    

---
