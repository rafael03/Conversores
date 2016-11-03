#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from os import walk

lista_de_arquivos = []
for (dirpath, dirnames, filenames) in walk(os.getcwd()):
    lista_de_arquivos.extend(filenames)
    break

for arquivo in lista_de_arquivos:
	if arquivo[-4:] == ".mp3":
		os.system("mp3splt %s -S 5" % arquivo)
		os.system("rm %s" % arquivo)

lista_particionada = []
for (dirpath, dirnames, filenames) in walk(os.getcwd()):
    lista_particionada.extend(filenames)
    break

lista_particionada.sort()

print "lista normal", lista_particionada
for arquivo in range(0, len(lista_particionada)):
	if lista_particionada[arquivo][-4:] == ".mp3":
		# os.system("mv %s" % arquivo)
		os.system("mv %s %s" % (lista_particionada[arquivo], str(arquivo)))



# for arquivo in lista_de_arquivos:
# 	if arquivo[-4:] == ".mp3":


# play = open('play.html', 'w+')
# play.write('<!DOCTYPE html>')
# play.write('<html>')
# play.write('<head>')
# play.write('<meta charset="UTF-8">')
# play.write('</head>')
# play.write('<body>')
# for arquivo in lista_de_arquivos:
# 	if arquivo[-4:] == ".mp4":
# 		play.write('<h1>Aula: %s </h1>' %str(arquivo))
# 		play.write('<video width="480" height="300" controls>')
# 		play.write('<source src="%s" type="video/mp4">' % str(arquivo))
# 		play.write('Seu navegador não suporta o elemento <code>video</code>.')
# 		play.write('</video>')
# 		play.write('</br>')
# play.write('</body')
# play.write('</html>')
# play.close()

# print "Página HTML gerada com sucesso!"