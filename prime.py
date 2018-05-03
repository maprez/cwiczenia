dolnaGranica = 10
gornaGranica = 300
#dolnaGranica = int(input("Dolny zakres to: "))
#gornaGranica = int(input("Gorny zakres to: "))

def liczbyPierwsze (dolnaGranica, gornaGranica):
    print("Liczby pierwsze od ",dolnaGranica," do",gornaGranica,"to:")
    for liczba in range(dolnaGranica,gornaGranica + 1):
       # prime numbers are greater than 1
       if liczba > 1:
           for i in range(2,liczba):
               if (liczba % i) == 0:
                   break
           else:
               print(liczba)

def main():
   dGranica = int(input('Podaj dolna granice '))
   gGranica = int(input('Podaj gorna granice '))

   print(liczbyPierwsze(dGranica, gGranica))

main()