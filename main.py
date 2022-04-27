#Jesper Lundberg
#TEINF20
#Wordle a fun game - main

from resources import Wordle

def main():
    print("Hello Wordle!")
    wordle = Wordle("APPLE")

    while True:
        x = input("Skriv in din gissning: ")
        if x == wordle.secretw:
            print("Du gissade rätt!")
            break
        print("Din gissning var tyvärr fel.")

    





if __name__ == "__main__":
    main()