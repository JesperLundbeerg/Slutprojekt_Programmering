#Jesper Lundberg
#TEINF20
#Wordle a fun game - main

from resources import Wordle

def main():
    print("Hello Wordle!")
    wordle = Wordle("APPLE")

    while wordle.can_attempt:
        x = input("Skriv in din gissning: ")

        if len(x) != wordle.Word_length:
            print(f"Ordet måste vara {wordle.Word_length} bokstäver långt! Testa igen.")
            continue

        wordle.attempt(x)
        result = wordle.guess(x)
        print(*result, sep="\n")

    if wordle.correct_guess:
            print("Du gissade rätt!")
    else:
        print("Du klarade tyvärr inte att lösa ut det ord som söktes.")
    





if __name__ == "__main__":
    main()