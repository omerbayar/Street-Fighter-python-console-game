# Street Fighter Game Ultimate Edition

from random import randint
from os import system, name
import time
import json
try:
    from colorama import init, Fore, Style
    init()
except ImportError:
    Fore = Style = type('obj', (), {'RED': '', 'GREEN': '', 'BLUE': '', 'YELLOW': '', 'RESET_ALL': ''})()

class Player:
    def __init__(self, name, class_type):
        self.name = name
        self.class_type = class_type
        self.max_hp = {'Savaşçı': 120, 'Büyücü': 80, 'Suikastçı': 100}[class_type]
        self.hp = self.max_hp
        self.heal_used = False
        self.dodge_chance = {'Savaşçı': 5, 'Büyücü': 10, 'Suikastçı': 20}[class_type]
        self.crit_chance = {'Savaşçı': 10, 'Büyücü': 20, 'Suikastçı': 15}[class_type]
        self.wins = 0
        self.hits = 0

def clearConsole():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def get_language():
    while True:
        lang = input("Dil seçin / Select language (TR/EN): ").upper()
        if lang in ["TR", "EN"]:
            return lang
        print("Geçersiz seçim. Lütfen TR veya EN girin.")

def get_translations(lang):
    translations = {
        "TR": {
            "coin_toss": "Yazı tura sonucu: {} önce başlar!",
            "attack_prompt": "Saldırı türünü seçin (1-4): ",
            "attack_types": "\n1. Hafif (10-20 hasar, 90% isabet)\n2. Orta (21-35 hasar, 70% isabet)\n3. Ağır (36-50 hasar, 50% isabet)\n4. İyileştir (20 HP, tek kullanımlık)",
            "invalid_attack": "Lütfen 1, 2, 3 veya 4 seçin.",
            "invalid_input": "Geçersiz giriş. Sayı girin.",
            "hit": "{} {} hasar verdi! {}",
            "miss": "HATA! {} saldırıyı kaçırdı!",
            "dodge": "{} saldırıyı savuşturdu!",
            "heal": "{} 20 HP iyileştirdi!",
            "heal_used": "{} zaten iyileştirme kullandı!",
            "win": "\n{0}#{0}\n{1} kazandı!!\n{0}#{0}",
            "play_again": "Tekrar oyna? (Evet/Hayır): ",
            "invalid_play_again": "Geçersiz giriş. Evet veya Hayır girin.",
            "thanks": "Oynadığınız için teşekkürler! Görüşürüz!",
            "name_prompt": "Kahraman adı girin: ",
            "name_taken": "{} alındı, başka bir isim seçin!",
            "name_empty": "İsim boş olamaz!",
            "class_prompt": "Sınıf seçin (1: Savaşçı, 2: Büyücü, 3: Suikastçı): ",
            "invalid_class": "Lütfen 1, 2 veya 3 seçin.",
            "mode_prompt": "Oyun modu seçin (1: İki Oyunculu, 2: Tek Oyunculu): ",
            "invalid_mode": "Lütfen 1 veya 2 seçin.",
            "difficulty_prompt": "Zorluk seçin (1: Kolay, 2: Normal, 3: Zor): ",
            "invalid_difficulty": "Lütfen 1, 2 veya 3 seçin.",
            "save_prompt": "Oyunu kaydet? (Evet/Hayır): ",
            "load_prompt": "Kayıtlı oyunu yükle? (Evet/Hayır): ",
            "no_save": "Kayıtlı oyun bulunamadı!",
            "leaderboard": "Lider Tablosu:\n{}: {} galibiyet, {} başarılı vuruş\n{}: {} galibiyet, {} başarılı vuruş"
        },
        "EN": {
            "coin_toss": "Coin toss result: {} starts first!",
            "attack_prompt": "Choose attack type (1-4): ",
            "attack_types": "\n1. Light (10-20 damage, 90% hit chance)\n2. Medium (21-35 damage, 70% hit chance)\n3. Heavy (36-50 damage, 50% hit chance)\n4. Heal (20 HP, one-time use)",
            "invalid_attack": "Please select 1, 2, 3, or 4.",
            "invalid_input": "Invalid input. Enter a number.",
            "hit": "{} dealt {} damage! {}",
            "miss": "MISS! {} missed the attack!",
            "dodge": "{} dodged the attack!",
            "heal": "{} healed for 20 HP!",
            "heal_used": "{} already used their heal!",
            "win": "\n{0}#{0}\n{1} wins!!\n{0}#{0}",
            "play_again": "Play again? (Yes/No): ",
            "invalid_play_again": "Invalid input. Enter Yes or No.",
            "thanks": "Thanks for playing! See you next time!",
            "name_prompt": "Enter hero name: ",
            "name_taken": "{} is taken, choose another name!",
            "name_empty": "Name cannot be empty!",
            "class_prompt": "Choose class (1: Warrior, 2: Mage, 3: Assassin): ",
            "invalid_class": "Please select 1, 2, or 3.",
            "mode_prompt": "Select game mode (1: Two-Player, 2: Single-Player): ",
            "invalid_mode": "Please select 1 or 2.",
            "difficulty_prompt": "Select difficulty (1: Easy, 2: Normal, 3: Hard): ",
            "invalid_difficulty": "Please select 1, 2, or 3.",
            "save_prompt": "Save game? (Yes/No): ",
            "load_prompt": "Load saved game? (Yes/No): ",
            "no_save": "No saved game found!",
            "leaderboard": "Leaderboard:\n{}: {} wins, {} successful hits\n{}: {} wins, {} successful hits"
        }
    }
    return translations[lang]

def display_ui(p1, p2, sira, lang, t):
    clearConsole()
    print(f"{Fore.BLUE}{'='*40}{Style.RESET_ALL}")
    print(f"{p1.name:>20} ({p1.class_type}) vs {p2.name:<20} ({p2.class_type})")
    print(f"{Fore.GREEN}HP[{p1.hp:3}] {'|' * int(p1.hp / 2)}{' ' * int((p1.max_hp - p1.hp) / 2)}  |  HP[{p2.hp:3}] {'|' * int(p2.hp / 2)}{' ' * int((p2.max_hp - p2.hp) / 2)}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}{'='*40}{Style.RESET_ALL}")
    print(f"Turn: {sira}")
    print(t["leaderboard"].format(p1.name, p1.wins, p1.hits, p2.name, p2.wins, p2.hits))
    print(f"{Fore.YELLOW}{'-'*40}{Style.RESET_ALL}")

def get_attack_choice(sira, lang, t, is_ai=False, difficulty="Normal"):
    if is_ai:
        if difficulty == "Hard":
            return randint(2, 3)  # AI prefers Medium/Heavy in Hard mode
        return randint(1, 3)  # Random attack in Easy/Normal
    print(t["attack_types"])
    while True:
        try:
            choice = int(input(t["attack_prompt"]))
            if choice in [1, 2, 3, 4]:
                return choice
            print(t["invalid_attack"])
        except ValueError:
            print(t["invalid_input"])

def perform_attack(attacker, defender, choice, counter, difficulty, lang, t):
    difficulty_mod = {"Easy": 1.2, "Normal": 1.0, "Hard": 0.8}[difficulty]
    if choice == 1:
        damage = randint(10, 20)
        hit_chance = int(90 * difficulty_mod)
    elif choice == 2:
        damage = randint(21, 35)
        hit_chance = int(70 * difficulty_mod)
    elif choice == 3:
        damage = randint(36, 50)
        hit_chance = int(50 * difficulty_mod)
    else:  # Heal
        if attacker.heal_used:
            print(f"{Fore.RED}{t['heal_used'].format(attacker.name)}{Style.RESET_ALL}")
            time.sleep(2)
            return 0, False
        attacker.heal_used = True
        heal_amount = 20
        attacker.hp = min(attacker.max_hp, attacker.hp + heal_amount)
        print(f"{Fore.GREEN}{t['heal'].format(attacker.name)}{Style.RESET_ALL}")
        time.sleep(2)
        return 0, False

    if randint(1, 100) <= defender.dodge_chance:
        print(f"{Fore.YELLOW}{t['dodge'].format(defender.name)}{Style.RESET_ALL}")
        time.sleep(2)
        return 0, False

    durum = randint(1, 100)
    crit = randint(1, 100) <= attacker.crit_chance
    if crit:
        damage = int(damage * 1.5)
        effect = f"{Fore.RED}(KRİTİK!){Style.RESET_ALL}"
    else:
        effect = ""

    if durum <= hit_chance:
        defender.hp -= damage
        attacker.hits += 1
        print(f"{Fore.GREEN}{t['hit'].format(attacker.name, damage, effect)}{Style.RESET_ALL} BAM!")
        time.sleep(2)
        return damage, True
    else:
        print(f"{Fore.RED}{t['miss'].format(attacker.name)}{Style.RESET_ALL} HATA!")
        time.sleep(2)
        return 0, False

def save_game(p1, p2, counter, difficulty, lang):
    game_state = {
        "p1": {"name": p1.name, "class_type": p1.class_type, "hp": p1.hp, "heal_used": p1.heal_used, "wins": p1.wins, "hits": p1.hits},
        "p2": {"name": p2.name, "class_type": p2.class_type, "hp": p2.hp, "heal_used": p2.heal_used, "wins": p2.wins, "hits": p2.hits},
        "counter": counter,
        "difficulty": difficulty,
        "lang": lang
    }
    return json.dumps(game_state)

def load_game(saved_state):
    state = json.loads(saved_state)
    p1 = Player(state["p1"]["name"], state["p1"]["class_type"])
    p1.hp = state["p1"]["hp"]
    p1.heal_used = state["p1"]["heal_used"]
    p1.wins = state["p1"]["wins"]
    p1.hits = state["p1"]["hits"]
    p2 = Player(state["p2"]["name"], state["p2"]["class_type"])
    p2.hp = state["p2"]["hp"]
    p2.heal_used = state["p2"]["heal_used"]
    p2.wins = state["p2"]["wins"]
    p2.hits = state["p2"]["hits"]
    return p1, p2, state["counter"], state["difficulty"], state["lang"]

def game(p1, p2, mode, difficulty, lang, t):
    counter = randint(0, 1)
    print(t["coin_toss"].format(p1.name if counter == 0 else p2.name))
    time.sleep(2)

    while True:
        sira = p1 if counter % 2 == 0 else p2
        display_ui(p1, p2, sira.name, lang, t)
        print(f"{Fore.YELLOW}———– {sira.name} Saldırıyor! ———–{Style.RESET_ALL}")
        choice = get_attack_choice(sira.name, lang, t, is_ai=(mode == "Single" and sira == p2), difficulty=difficulty)
        damage, hit = perform_attack(sira, p1 if sira == p2 else p2, choice, counter, difficulty, lang, t)
        counter += 1

        if p1.hp <= 0:
            p2.wins += 1
            display_ui(p1, p2, sira.name, lang, t)
            print(t["win"].format('#'*18, p2.name))
            return p2
        if p2.hp <= 0:
            p1.wins += 1
            display_ui(p1, p2, sira.name, lang, t)
            print(t["win"].format('#'*18, p1.name))
            return p1

def main():
    lang = get_language()
    t = get_translations(lang)
    saved_state = None

    while True:
        if saved_state:
            choice = input(t["load_prompt"]).lower()
            if choice == ("evet" if lang == "TR" else "yes"):
                try:
                    p1, p2, counter, difficulty, lang = load_game(saved_state)
                    t = get_translations(lang)
                    mode = "Single" if p2.name == "AI_Opponent" else "Two-Player"
                    break
                except:
                    print(t["no_save"])
                    saved_state = None

        p1_name = input(t["name_prompt"]).strip()
        while not p1_name:
            print(t["name_empty"])
            p1_name = input(t["name_prompt"]).strip()

        while True:
            mode = input(t["mode_prompt"])
            if mode in ["1", "2"]:
                mode = "Two-Player" if mode == "1" else "Single"
                break
            print(t["invalid_mode"])

        if mode == "Single":
            p2_name = "AI_Opponent"
            break
        else:
            while True:
                p2_name = input(t["name_prompt"]).strip()
                if not p2_name:
                    print(t["name_empty"])
                elif p1_name.lower() != p2_name.lower():
                    break
                print(t["name_taken"].format(p1_name))

        while True:
            class_choice = input(t["class_prompt"])
            if class_choice in ["1", "2", "3"]:
                p1 = Player(p1_name, {1: "Savaşçı", 2: "Büyücü", 3: "Suikastçı"}[int(class_choice)])
                break
            print(t["invalid_class"])

        while True:
            class_choice = input(t["class_prompt"])
            if class_choice in ["1", "2", "3"]:
                p2 = Player(p2_name, {1: "Savaşçı", 2: "Büyücü", 3: "Suikastçı"}[int(class_choice)])
                break
            print(t["invalid_class"])

        while True:
            diff = input(t["difficulty_prompt"])
            if diff in ["1", "2", "3"]:
                difficulty = {1: "Easy", 2: "Normal", 3: "Hard"}[int(diff)]
                break
            print(t["invalid_difficulty"])
        break

    print("Oyun başlıyor..." if lang == "TR" else "Game starting...")
    time.sleep(2)
    clearConsole()

    while True:
        winner = game(p1, p2, mode, difficulty, lang, t)
        print(t["leaderboard"].format(p1.name, p1.wins, p1.hits, p2.name, p2.wins, p2.hits))
        while True:
            save = input(t["save_prompt"]).lower()
            if save in ["evet", "hayır"] if lang == "TR" else ["yes", "no"]:
                if save == ("evet" if lang == "TR" else "yes"):
                    saved_state = save_game(p1, p2, counter, difficulty, lang)
                    print("Oyun kaydedildi (JSON):\n", saved_state)
                break
            print(t["invalid_play_again"])

        while True:
            istek = input(t["play_again"]).lower()
            if istek in ["evet", "hayır"] if lang == "TR" else ["yes", "no"]:
                if istek == ("hayır" if lang == "TR" else "no"):
                    print(t["thanks"])
                    exit()
                p1.hp, p2.hp = p1.max_hp, p2.max_hp
                p1.heal_used, p2.heal_used = False, False
                break
            print(t["invalid_play_again"])
        clearConsole()

if __name__ == "__main__":
    main()