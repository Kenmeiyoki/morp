# -*- coding: UTF-8 -*-
from __future__ import print_function

import os
import time

Start = 5
Tableau = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
ArrowR = [" ", " ", " "]
Tour = 2
Gagner = 0
col = 0
lin = 0
Signe = " "

for i in range(5):
	os.system("clear")
	print("Le jeu commence dans ", Start, " sec!")
	Start = Start-1
	time.sleep(0.1)
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
	time.sleep(0.02)
	print("╔═╦═╦═╗")
	time.sleep(0.02)
	print("║", Tableau[0], "║", Tableau[1], "║", Tableau[2], "║", ArrowR[0], sep="")
	time.sleep(0.02)
	print("╠═╬═╬═╣")
	time.sleep(0.02)
	print("║", Tableau[3], "║", Tableau[4], "║", Tableau[5], "║", ArrowR[1],sep="")
	time.sleep(0.02)
	print("╠═╬═╬═╣")
	time.sleep(0.02)
	print("║", Tableau[6], "║", Tableau[7], "║", Tableau[8], "║", ArrowR[2],sep="")
	time.sleep(0.02)
	print("╚═╩═╩═╝")
def err_col_2(col):
	os.system("clear") 
	time.sleep(0.1)
	os.system("clear")
	print("")
	dis_tab(col)
	print("")
	col=input("Entrez le numéro de la colonne : ")
	if(col != 1 and col != 2 and col != 3):
		err_col_1(col)

def err_col_1(col):
	os.system("clear") 
	print("ERREUR : Cononne inconnue")
	time.sleep(1)
	os.system("clear")
	print("")
	dis_tab(col)
	print("")
	col=input("Entrez le numéro de la colonne : ")
	if(col != 1 and col != 2 and col != 3):
		err_col_1(col)

def ind(row, col):
	return (row-1)*3+col-1

def display(row, col):
	indice = ind(row, col)
	if(Tableau[indice] == " "):
		Tableau[indice] = Signe
	else:
		os.system("clear")
		print("ERREUR : Un signe à déjà été définis ici !")
		time.sleep(1)
		print("Veuillez réessayer une autre case")
		time.sleep(2)
		err_col_2(col)

def err_lin_1(lin):
	os.system("clear") 
	print("ERREUR : Ligne inconnue")
	time.sleep(1)
	os.system("clear")
	print("")
	dis_tab(lin)
	print("")
	lin=input("Entrez le numéro de la ligne : ")
	if(lin != 1 and lin != 2 and lin != 3):
		err_lin_1(col)
time.sleep(1)
os.system("clear") 
time.sleep(0.1)
dis_tab(col)
# if(tour1 == 1):
while(Gagner != 1 or Gagner != 2):
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
	col=input("Entrez le numéro de la colonne : ")
	if(col != 1 and col != 2 and col != 3):
		err_col_1(col)
	os.system("clear") 
	dis_tab(col)
	print("")
	lin=input("Entrez le numéro de la ligne : ")
	if(lin != 1 and lin != 2 and lin != 3):
		err_lin_1(lin)
	display(lin, col)
	print("salut")
	
	if Tableau[0] == Tableau[1] == Tableau[2]:
		os.system("clear")
		print("Le joueur", Tour, "à gagner")
		break