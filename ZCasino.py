#!/usr/bin/python
#-*- coding:utf-8 -*-

from random import randrange
from math import ceil

print "Bienvenu à notre JEU ZCasino\n"

quitter = "O"

try:
	avoir = int(raw_input("Quel est votre avoir total ? \n"))
	if avoir < 0:
		raise ValueError("Erreur: L'avoir total doit être un entier positive.\n")
except ValueError:
	print "Erreur : L'avoir total doit être un entier positive.\n"

else:
	while quitter.upper() == "O" and avoir > 0:
		try:
			choix = int(raw_input("Choississez un numéro entre 0 et 49 : \n"))
			if choix < 0 or choix >= 50:
				raise ValueError("Choississez un numéro entre 0 et 49 : \n")
		except ValueError:
			print "Choississez un numéro entre 0 et 49 : \n"
		else:
			try:
				mise = int(raw_input("Quelle est votre mise pour ce numéro : \n"))
				if mise <= 0 or mise > avoir:
					raise ValueError("La mise doit etre inférieur ou égale à votre avoir et strictement positive : \n")
			except ValueError:
				print "La mise doit etre inférieur ou égale à votre avoir et strictement positive : \n"
			else:
				if choix%2 == 0:
					couleur_choix = "Noir"
				else:
					couleur_choix = "Rouge"

				tirage = randrange(50)

				if tirage%2 == 0:
					couleur_tirage = "Noir"
				else:
					couleur_tirage = "Rouge"
				
				print "Vous avez choisir {}. Il a la couleur {}".format(choix,couleur_choix)
				

				print "Le numéro tiré est {}. Il a la couleur {}".format(tirage,couleur_tirage)
				
				if choix == tirage:
					avoir += ceil(mise*3)
					print "Bravo ! Bon numéro.\nVous gagnez 3 fois votre mise : {} Francs.\nVotre avoir est maintenant de {} Francs".format(mise*3,avoir)
				elif couleur_choix == couleur_tirage:
					avoir += ceil(mise*0.5)
					print "Bravo! Bonne couleur.\nVous gagnez 50 pourcent de votre mise : {} Francs.\nVotre avoir est maintenant de {} Francs".format(mise*0.5,avoir)
				
				else:
					avoir -= mise
					print "Perdu! Mauvais numéro et mauvaise couleur.\nVous perdez votre mise : {} Francs.\nVotre avoir est maintenant de {} Francs".format(mise,avoir)
				
			finally:

				if avoir == 0:
					break
				else:
					quitter = raw_input("Voulez-vous continuer ? Tapez 'o' pour 'oui' et tout autre touche pour 'non'\n")
			
		
print("Fin du programme! Au revoir.\n")



