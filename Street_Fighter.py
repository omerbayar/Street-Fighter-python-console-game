# Street Fighter Game

from random import randint
from os import system, name
import time

def clearConsole():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def display_ui(k1, k2, hpk1, hpk2, sira, successful_hits):
    bosluk1 = 100 - hpk1
    bosluk2 = 100 - hpk2
    clearConsole()
    print(f"\n{'='*40}")
    print(f"{k1:>20} vs {k2:<20}")
    print(f"HP[{hpk1:3}] {'|' * int(hpk1 / 2)}{' ' * int(bosluk1 / 2)}  |  HP[{hpk2:3}] {'|' * int(hpk2 / 2)}{' ' * int(bosluk2 / 2)}")
    print(f"{'='*40}")
    print(f"Turn: {sira}")
    print(f"Successful Hits - {k1}: {successful_hits[k1]}, {k2}: {successful_hits[k2]}")
    print(f"{'-'*40}")

def get_attack_choice():
    print("\nAttack Types:")
    print("1. Light (10-20 damage, 90% hit chance)")
    print("2. Medium (21-35 damage, 70% hit chance)")
    print("3. Heavy (36-50 damage, 50% hit chance)")
    print("4. Heal (Restores 20 HP, one-time use)")
    while True:
        try:
            choice = int(input("Choose attack (1-4): "))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Please select 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid input. Enter a number.")

def perform_attack(sira, choice, hpk1, hpk2, heal_used, counter):
    if choice == 1:
        damage = randint(10, 20)
        hit_chance = 90
    elif choice == 2:
        damage = randint(21, 35)
        hit_chance = 70
    elif choice == 3:
        damage = randint(36, 50)
        hit_chance = 50
    else:  # Heal
        if heal_used[sira]:
            print(f"{sira} already used their heal!")
            time.sleep(2)
            return hpk1, hpk2, heal_used, 0
        heal_used[sira] = True
        heal_amount = 20
        print(f"{sira} heals for {heal_amount} HP!")
        if counter % 2 == 0:
            hpk1 = min(100, hpk1 + heal_amount)
        else:
            hpk2 = min(100, hpk2 + heal_amount)
        time.sleep(2)
        return hpk1, hpk2, heal_used, 0

    durum = randint(1, 100)
    if durum <= hit_chance:
        print(f"{sira} hits for {damage} damage!")
        if counter % 2 == 0:
            hpk2 -= damage
            return hpk1, hpk2, heal_used, damage
        else:
            hpk1 -= damage
            return hpk1, hpk2, heal_used, damage
    else:
        print(f"Ooopsy! {sira} missed!")
        time.sleep(2)
        return hpk1, hpk2, heal_used, 0

def game(k1, k2):
    yt = randint(0, 1)
    print("Yazı tura sonucu:", k1 if yt == 0 else k2, "önce başlar!")
    time.sleep(2)

    hpk1, hpk2 = 100, 100
    counter = yt
    heal_used = {k1: False, k2: False}
    successful_hits = {k1: 0, k2: 0}

    while True:
        sira = k1 if counter % 2 == 0 else k2
        display_ui(k1, k2, hpk1, hpk2, sira, successful_hits)
        print(f"———– {sira} Attacks! ———–")
        choice = get_attack_choice()
        hpk1, hpk2, heal_used, damage = perform_attack(sira, choice, hpk1, hpk2, heal_used, counter)
        if damage > 0:
            successful_hits[sira] += 1
        counter += 1

        if hpk1 <= 0:
            display_ui(k1, k2, 0, hpk2, sira, successful_hits)
            print(f"\n{'#'*36}\n{k2} wins!!\n{'#'*36}")
            return k2, successful_hits
        if hpk2 <= 0:
            display_ui(k1, k2, hpk1, 0, sira, successful_hits)
            print(f"\n{'#'*36}\n{k1} wins!!\n{'#'*36}")
            return k1, successful_hits

def main():
    k1 = input("———– First Hero ———–\nEnter hero name: ").strip()
    while not k1:
        print("Name cannot be empty!")
        k1 = input("Enter hero name: ").strip()

    while True:
        k2 = input("———– Second Hero ———–\nEnter hero name: ").strip()
        if not k2:
            print("Name cannot be empty!")
        elif k1.lower() != k2.lower():
            break
        else:
            print(f"{k1} is taken, choose another name!")

    print("Game starting...\n")
    time.sleep(2)
    clearConsole()

    while True:
        winner, successful_hits = game(k1, k2)
        print(f"Final Score - {k1}: {successful_hits[k1]} hits, {k2}: {successful_hits[k2]} hits")
        while True:
            istek = input("Play another round (Evet or Hayır)? : ").lower()
            if istek in ["evet", "hayır"]:
                if istek == "hayır":
                    print("Thanks for playing! See you next time!")
                    exit()
                break
            else:
                print("Invalid input. Enter 'Evet' or 'Hayır'.")
        clearConsole()

if __name__ == "__main__":
    main()
