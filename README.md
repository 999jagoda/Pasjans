1. Wymagania:

- python 3.12 lub wyższy
- terminal/środowisko obsługujące bibliotekę colorama

2. Uruchomienie projektu:

- zainstaluj zależności:
   requirements.txt

- uruchom program:
   pasjans-projekt.py

3. Zasady gry:

Użytkownik najpierw wprowadza swoją nazwę i wybiera poziom trudności. 
Następnie wybiera ruch poprzez wprowadzenie odpowieniej litery:
- r: włącza grę od nowa
- q: wyświetla liczbę ruchów i kończy program
- u: cofa ruch (do 3 w tył)
- m: przesuwa karty w stosie głównym; należy wprowadzić współrzędne karty, którą chce się przesunąć (lub górnej karty jeśli przesuwa się ich kilka naraz) oraz karty na którą chce się położyć powyższe w formacie x,y
- d: przesuwa odkrytą kartę ze stosu dodatkowego na stos główny; należy wprowadzić współrzędne karty, na którą chce się ją położyć w formacie x,y
- a: odkłada kartę na stos końcowy; należy wprowadzić tekst "stos" jeśli jest ona na stosie dodatkowym, współrzędne karty jeśli jest ona na stosie głównym w formacie x,y oraz numer stosu końcowego (0-3)
- n: dobiera po 1 karcie ze stosu dodatkowego w trybie łatwym lub 3 karty w trybie trudnym
Po ułożeniu wszystkich kart na stosy końcowe gra się kończy i wyświetla się ranking.
