#Jesper Lundberg
#TEINF20
#Wordle a fun game - main

from resources import Wordle

def main():
    print("Hello Wordle!")
    wordle = Wordle("APPLE")

    while wordle.can_attempt:
        x = input("Skriv in din gissning: ")
        wordle.attempt(x)
        result = wordle.guess(x)
        print(result)

    if wordle.correct_guess:
            print("Du gissade rätt!")
    else:
        print("Du klarade tyvärr inte att lösa ut det ord som söktes.")
    





if __name__ == "__main__":
    main()