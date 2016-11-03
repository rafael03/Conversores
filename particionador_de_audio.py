#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from os import walk
import sys
# print sys.argv[1]

lista_de_arquivos = []
for (dirpath, dirnames, filenames) in walk(os.getcwd()):
    lista_de_arquivos.extend(filenames)
    break

for arquivo in lista_de_arquivos:
	if arquivo[-4:] == ".mp3":
		os.system("mp3splt %s -S 7" % arquivo)
		os.system("rm %s" % arquivo)

lista_particionada = []
for (dirpath, dirnames, filenames) in walk(os.getcwd()):
    lista_particionada.extend(filenames)
    break

lista_particionada.sort()

print "lista normal", lista_particionada
for arquivo in range(0, len(lista_particionada)):
	if lista_particionada[arquivo][-4:] == ".mp3":
		os.system("mv %s %s" % (lista_particionada[arquivo], str(arquivo)))
