#Jesper Lundberg
#TEINF20
#Wordle a fun game - main

from typing import List
from resources import LetterCondition, Wordle
from colorama import Fore
import random
import os

def main():
    
    word_machine = load_word_machine("words.txt")
    secretw = random.choice(list(word_machine))
    wordle = Wordle(secretw)

    while wordle.can_attempt:
        print("\nInstruktioner: Detta är ett spel där du ska gissa dig fram till ett hemligt ord.")
        print("""Ordet ska vara 5 bokstäver långt och just nu används en ordlista på engelska,
så endast ord på engelska är tillåtna ;)
        """)
        print("Lycka till!")
        x = input("\nSkriv in din gissning: ")
        x = x.upper()

        if len(x) != wordle.Word_length:
            print(Fore.RED + f"Ordet måste vara {wordle.Word_length} bokstäver långt! Testa igen." + Fore.RESET)
            continue

        if not x in word_machine:
            print(Fore.RED + f"{x} är inte ett riktigt ord! Testa igen." + Fore.RESET)
            continue

        wordle.attempt(x)
        display_results(wordle)

    if wordle.correct_guess:
            print("Du gissade rätt!")
    else:
        print("Du klarade tyvärr inte att lösa ut det ord som söktes.")
        print(f"Ordet som söktes var: {wordle.secretw}")
    

def display_results(wordle: Wordle):
    print("\nDina resultat hittills...")
    print(f"Du har {wordle.attempts_left} försök kvar.\n")
    
    lines = []

    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)
    
    for _ in range(wordle.attempts_left):
        #print("_ " * wordle.Word_length)
        lines.append(" ".join(["_"] * wordle.Word_length))

    border_around_wordle(lines)

def load_word_machine(path : str):
    word_machine = set()
    with open(path, "r", encoding="utf8") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_machine.add(word)
    return word_machine


def convert_result_to_color(result: List[LetterCondition]):
    """_summary_

    Args:
        result (List[LetterCondition]): _description_

    Returns:
        _type_: _description_
    """
    result_w_color = []
    for letter in result:
        if letter.in_position:
            color = Fore.GREEN
        elif letter.in_word:
            color = Fore.YELLOW
        else:
            color = Fore.RED
        colored_letter = color + letter.character + Fore.RESET
        result_w_color.append(colored_letter)
    return " ".join(result_w_color)

def border_around_wordle(lines : List[str], size: int=9, pad : int=1):
    content_length = size + pad * 2
    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘"
    space = " " * pad
    print(top_border)

    for line in lines:
        print("│" + space + line + space + "│")
        
    print(bottom_border)

def clear():
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)

if __name__ == "__main__":
    clear()
    enter = input("Välkommen till Wordle! Tryck enter för att starta spelet: ")
    if "" in enter:
        pass
    while True:
        main()
        choice = input("Vill du spela igen? [ja, nej]: ")
        if "ja".casefold() in choice.casefold():
            clear()
            continue
        elif "nej".casefold() in choice.casefold():
            break
        else:
            break
    clear()
    print("Tack för att du spelat!")