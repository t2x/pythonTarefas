import os

for x, diretorios, arquivos in os.walk(os.getcwd()):
    for diretorio in diretorios:
        print ('\nDiretorio: %s' %(diretorio))
    for arquivo in arquivos:
        print ('Arquivo: %s' %(arquivo))
