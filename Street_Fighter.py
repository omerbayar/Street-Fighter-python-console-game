# Street Fighter Game
from random import randint
from os import system, name
import time

def game():
	yt = randint(0, 1)
	if yt == 0 :
		print("Yazı tura sonucu:", k1, "önce başlar!")
	else :
		print("Yazı tura sonucu:", k2, "önce başlar!")
	time.sleep(3)

	hpk1 = 100
	hpk2 = 100
	counter = yt
	while True :
		bosluk1 = 100 - hpk1
		print(bosluk1)
		bosluk2 = 100 - hpk2
		print(bosluk2)
		clearConsole()
		if yt == 0 :
			print(5 * " " + k1 + 70 * " " + k2 + "\n")
			print("HP[" + str(hpk1) + "]:" + int(hpk1 / 2) * "|" + int(bosluk1 / 2 + 1) * " " + " " * 5 + "HP[" + str(hpk2) + "]:" + int(hpk2 / 2) * "|" + bosluk2 * " ")
		else :
			print(k2 + 60 * " " + k1 + "\n")
			print("HP[" + str(hpk2) + "]:" + int(hpk2 / 2) * "|" + int(bosluk2 / 2 + 1) * " " + " " * 5 + "HP[" + str(hpk1) + "]:" + int(hpk1 / 2) * "|" + bosluk1 * " ")
		if counter % 2 == 0 :
			sira = k1
		else :
			sira = k2
		print("  ———–" + sira + " Saldırı !! ———–")
		while True :
			istekSaldiri = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin: "))
			if istekSaldiri < 1 or istekSaldiri > 50 :
				print("Saldırı Saldırı büyüklüğü 1 ile 50 arasında olmalıdır.")
			else :
				break
		sans = 100 - istekSaldiri
		durum = randint(1, 100)
		if durum <= sans :
			print(sira, istekSaldiri, "hasar verdi!!")
			if counter % 2 == 0 :
				hpk2 = hpk2 - istekSaldiri
			else :
				hpk1 = hpk1 - istekSaldiri
			time.sleep(2)
		else :
			print("Ooopsy!", sira, "saldırıyı kaçırdı!")
			time.sleep(2)
		counter += 1
		if hpk1 <= 0 :
			print(36 * "#" + "\n" + "#" * 10 + k2, "kazandı!!" + "#" * 10 + "\n" + 36 * "#")
			while True :
				istek = input("Bir tur daha oynamak ister misiniz (Evet veya Hayır)? :")
				if istek.lower() == "evet" or istek.lower() == "hayır" :
					if istek.lower() == "evet" :
						game()
					elif istek.lower() == "hayır" :
						exit("Oynadığınız için teşekkürler! Tekrar görüşürüz!")
					break
				else :
					print("hatalı giriş.")
		if hpk2 <= 0 :
			print(36 * "#" + "\n" + "#" * 10 + k1, "kazandı!!  " + "#" * 10 + "\n" + 36 * "#")
			while True :
				istek = input("Bir tur daha oynamak ister misiniz (Evet veya Hayır)? :")
				if istek.lower() == "evet" or istek.lower() == "hayır" :
					if istek.lower() == "evet" :
						game()
					elif istek.lower() == "hayır" :
						exit("Oynadığınız için teşekkürler! Tekrar görüşürüz!")
					break
				else :
					print("hatalı giriş.")

def clearConsole() :
	if name == "nt" :
		_ = system("cls")
	else :
		_ = system("clear")

k1 = input("  ———– İlk Kahraman ———– \nLütfen kahramanınızın adını yazın: ")
while True :
	k2 = input("  ———– İkinci Kahraman ———– \nLütfen kahramanınızın adını yazın: ")
	if k1.lower() != k2.lower():
		break
	else :
		print(k1 + " alındı, lütfen başka bir isim seçin!")

print("Oyun başladı...\n")
time.sleep(2)
clearConsole()
game()
