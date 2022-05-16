#Jesper Lundberg
#TEINF20
#Wordle a fun game - main

from lib2to3.pytree import convert
from typing import List
from resources import LetterCondition, Wordle
from colorama import Fore
import random

def main():
    
    word_machine = load_word_machine("Wordlist.txt")
    secretw = random.choice(list(word_machine))
    wordle = Wordle(secretw)

    while wordle.can_attempt:
        x = input("\nSkriv in din gissning: ")

        if len(x) != wordle.Word_length:
            print(Fore.RED + f"Ordet måste vara {wordle.Word_length} bokstäver långt! Testa igen." + Fore.RESET)
            continue

        wordle.attempt(x)
        display_results(wordle)

    if wordle.correct_guess:
            print("Du gissade rätt!")
    else:
        print("Du klarade tyvärr inte att lösa ut det ord som söktes.")
        print(f"Ordet som söktes var: {wordle.secretw}")
    

def display_results(wordle: Wordle):
    print("\nDina resultat hittills...\n")
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
    word_machine = []
    with open(path, "r", encoding="utf8") as f:
        for line in f.readlines():
            # word = line.strip().upper()
            # word_machine.add(word)
            word = line.split(",")
            i = Wordle(word[0])
            word_machine.append(i)
    return word_machine


def convert_result_to_color(result: List[LetterCondition]):
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

if __name__ == "__main__":
    main()