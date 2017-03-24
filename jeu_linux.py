# UBUNTU version
# -*- coding: UTF-8 -*-


#
#
#
#

from __future__ import print_function

import os
import time
import random

Start = 60
Tableau = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
ArrowR = [" ", " ", " "]
Tour = 2
Gagner = 0
col = 0
lin = 0
Signe = " "

W_1_det = 0
W_2_det = 0
W_3_det = 0



for i in range(1):
	os.system("clear")
	print("Le jeu commence dans ", Start, " !")
	Start = Start-1
	time.sleep(0.02)
def dis_tab(numcol):
	print("")
	print("Au tour du joueur: ", Tour)
	print("")
	arrow = " "
	if(col == 1 or col == 2 or col == 3):
		arrow = " "
		for i in range(numcol - 1):
			arrow += "  "
		arrow += "↓"
	if(lin == 1):
		ArrowR[0] = "←"
	if(lin == 2):
		ArrowR[1] = "←"
	if(lin == 3):
		ArrowR[2] = "←"

	print(arrow)
	print("╔═╦═╦═╗")
	print("║", Tableau[0], "║", Tableau[1], "║", Tableau[2], "║", ArrowR[0], sep="")
	print("╠═╬═╬═╣")
	print("║", Tableau[3], "║", Tableau[4], "║", Tableau[5], "║", ArrowR[1],sep="")
	print("╠═╬═╬═╣")
	print("║", Tableau[6], "║", Tableau[7], "║", Tableau[8], "║", ArrowR[2],sep="")
	print("╚═╩═╩═╝")

def err_col_2(col):
	os.system("clear") 
	time.sleep(0.1)
	os.system("clear")
	print("")
	dis_tab(col)
	print("")
	print("Please wait...")
	time.sleep(0.3)


def ask_input(txt):
	string = "0"
	verif = False
	veiovroj = "Entrer le numéro de la "+txt+" : "
	vjkdjvjf = "ERREUR : Nombre de la "+txt+" est erroné, (nombre entré : "+string+") Veuillez réessayer"
	os.system("clear")
	print("")
	dis_tab(lin)
	print("")
	while string != '1' and string != '2' and string != '3':
		time.sleep(0.1)
		os.system("clear")
		if(verif == True):
			print("")
			print(vjkdjvjf)
		print("")
		dis_tab(lin)
		print("")
		verif = True
		string=raw_input(veiovroj)
	return int(string)



def win_detect(W_1_det, W_2_det, W_3_det):
	if(Tableau[W_1_det] == Tableau[W_2_det] == Tableau[W_3_det]):
		if Tableau[W_1_det] != " " and Tableau[W_2_det] != " " and Tableau[W_3_det] != " ":
			os.system("clear")
			print("Le joueur", Tour, "a gagné")
			return True
	return False


def random_pick(Tableau):
	empty_indices = []
	for i, value in enumerate(Tableau):
		if value == " ":
			empty_indices.append(i)
	return random.choice(empty_indices)


def ind(row, col):
	return (row-1)*3+col-1

def display(row, col):
	indice = ind(row, col)
	if(Tableau[indice] == " "):
		Tableau[indice] = Signe
	else:
		os.system("clear")
		print("ERREUR : Un signe a déjà été défini ici !")
		time.sleep(0.1)
		print("Veuillez réessayer une autre case")
		time.sleep(2) 
		time.sleep(0.1)
		print("")
		dis_tab(col)
		print("")
		print("Please wait...")
		time.sleep(0.3)

def exe_ia():
	for i in range(3):
		roww = i+1
		coll = 0
		if Tableau[ind(roww, 1)] == Tableau[ind(roww, 2)]:
			if Tableau[ind(roww, 1)] != " " and Tableau[ind(roww, 2)] != " ":
				choix=(ind(roww, 3))
				return choix
	for i in range(3):
		roww = 1+i
		coll = i
		if Tableau[ind(roww, 2)] == Tableau[ind(roww, 3)]:
			if Tableau[ind(roww, 2)] != " " and Tableau[ind(roww, 3)] != " ":
				choix=(ind(roww, 1))
				return choix
	for i in range(3):
		roww = 1+i
		coll = i
		if Tableau[ind(roww, 1)] == Tableau[ind(roww, 3)]:
			if Tableau[ind(roww, 1)] != " " and Tableau[ind(roww, 3)] != " ":
				choix=(ind(roww, 2))
				return choix
	return random_pick(Tableau)

time.sleep(1)
os.system("clear") 
time.sleep(0.1)
dis_tab(col)
# if(tour1 == 1):
while(Gagner != 1 or Gagner != 2):
	ArrowR = [" ", " ", " "]
	if(Tour == 1):
		Tour = 2
		Signe = "O"
	elif(Tour == 2):
		Signe = "X"
		Tour = 1
	os.system("clear") 
	print("")
	print("")
	dis_tab(col)
	print("")
	if Tour == 1 :
		col=ask_input("colonne")
		time.sleep(0.1)
		os.system("clear") 
		dis_tab(col)
		print("")
		lin=ask_input("ligne")
		vfkvnfklv=ind(lin, col)
		Tableau[vfkvnfklv] = Signe
	if Tour == 2 :
		os.system("clear")
		print("")
		dis_tab(col)
		print("")
		print("L'ordinateur est entrain de jouer !")
		calcul = 1

		# ESSAYE DE PERDRE PAR LIGNE

		


		choix = exe_ia()
		Tableau[choix] = Signe
# 1 2 3
# 4 5 6
# 7 8 9






		time.sleep(3)
	#display(lin, col)
	# print("salut")
	#	time.sleep(5)
	if win_detect(0, 1, 2) or win_detect(3, 4, 5) or win_detect(6, 7, 8) or win_detect(0, 3, 6) or win_detect(0, 1, 2) or win_detect(1, 4, 7) or win_detect(2, 5, 8) or win_detect(0, 4, 8) or win_detect(6, 7, 8):
		os.system("clear")
		print("")
		print("Le joueur", Tour, "a gagné!")
		print("")
		break
	if Tableau[0] != " " and Tableau[1] != " " and Tableau[2] != " " and Tableau[3] != " " and Tableau[4] != " " and Tableau[5] != " " and Tableau[6] != " " and Tableau[7] != " " and Tableau[8] != " ":
		os.system("clear")
		print("Vous avez perdu !")
		time.sleep(1)
		print("Fin de la partie !")
		time.sleep(5)
		break
# 0 1 2
# 3 4 5
# 6 7 8
