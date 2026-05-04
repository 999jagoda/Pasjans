# -*- coding: utf-8 -*-

from random import shuffle
from copy import deepcopy
from colorama import init, Fore, Style

init()


# funkcja deal tasuje i zwraca pełną talię
def deal():
    random_cards = ["2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "D♠", "K♠", "A♠",
                    "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "D♦", "K♦", "A♦",
                    "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "D♣", "K♣", "A♣",
                    "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "D♥", "K♥", "A♥"]
    shuffle(random_cards)
    return random_cards


# funkcja start przydziela karty do poszczególnych stosów
def start():
    t = deal()
    # True to karta odkryta a False zakryta
    k1 = [[t[0], True]]
    k2 = [[t[1], False], [t[2], True]]
    k3 = [[t[3], False], [t[4], False], [t[5], True]]
    k4 = [[t[6], False], [t[7], False], [t[8], False], [t[9], True]]
    k5 = [[t[10], False], [t[11], False], [t[12], False], [t[13], False], [t[14], True]]
    k6 = [[t[15], False], [t[16], False], [t[17], False], [t[18], False], [t[19], False], [t[20], True]]
    k7 = [[t[21], False], [t[22], False], [t[23], False], [t[24], False], [t[25], False], [t[26], False],
          [t[27], True]]
    extra = [[t[28], False], [t[29], False], [t[30], False], [t[31], False], [t[32], False],
             [t[33], False], [t[34], False], [t[35], False], [t[36], False], [t[37], False],
             [t[38], False], [t[39], False], [t[40], False], [t[41], False], [t[42], False],
             [t[43], False], [t[44], False], [t[45], False], [t[46], False], [t[47], False],
             [t[48], False], [t[49], False], [t[50], False], [t[51], True]]
    main_cards = [k1, k2, k3, k4, k5, k6, k7]
    return main_cards, extra


# funkcja colored_cards nadaje kolor czerwony kartom karo i kier przy pomocy biblioteki colorama
def colored_cards(card):
    if "♦" in card or "♥" in card:
        return f"{Fore.RED}{card}{Style.RESET_ALL}"
    else:
        return card


# funkcja formatting wyrównuje ilość znaków
def formatting(card):
    card = colored_cards(card)
    no_color = card.replace(Fore.RED, "").replace(Style.RESET_ALL, "")
    padding = 5 - len(no_color)
    return card + " " * padding


# funkcja arrangement służy do wyświetlania kart
def arrangement(main_cards, extra):
    visible_stocks = []
    print("   0    1    2    3    4    5    6   [x]")

    # zamiana kart zakrytych w stosie głównym na "##":
    for stock in main_cards:
        visible = []
        for card, reverse in stock:
            if reverse:
                visible.append(card)
            else:
                visible.append("##")
        visible_stocks.append(visible)

    # wyświetlenie kart jedna pod drugą i formatowanie odkrytych
    for i in range(19):
        line = ""
        for stock in visible_stocks:
            if i < len(stock):
                card = stock[i]
                if card != "##":
                    card = formatting(card)
                else:
                    card = f"{card:<5}"
                line += card
            else:
                line += " " * 5
        if i <= 9:
            print(" " + str(i) + " " + str(line))
        else:
            print(i, line)
    # zamiana kart zakrytych w stosie dodatkowym na "##" i formatowanie odkrytych
    print("[y]")
    if extra:
        stock_str = ""
        for i in range(len(extra)):
            if not extra[i][1]:
                stock_str += "## "
            else:
                stock_str += colored_cards(extra[i][0])
                stock_str += " "
    else:
        stock_str = ""
    print("Stos dodatkowy: " + stock_str)
    return ""


# funkcja end_stocks_arrangement służy do wyświetlania stosu końcowego
def end_stocks_arrangement(end_stocks):
    print("Stosy końcowe:")
    max_height = max(len(stack) for stack in end_stocks)
    for i in range(max_height):
        line2 = ""
        for stack in end_stocks:
            if i < len(stack):
                card = formatting(stack[i])
            else:
                card = "     "
            line2 += card
        print(line2)
    return ""


# funkcja rules sprawdza, czy karta B może zostać położona na karcie A
def rules(card_a, card_b, n):
    # przypisanie wartości liczbowych kartom
    value_a = card_a[:-1]
    value_b = card_b[:-1]
    color_a = card_a[-1]
    color_b = card_b[-1]
    if value_a == "J":
        temp_a = 11
    elif value_a == "D":
        temp_a = 12
    elif value_a == "K":
        temp_a = 13
    elif value_a == "A":
        temp_a = 1
    else:
        temp_a = int(value_a)

    if value_b == "J":
        temp_b = 11
    elif value_b == "D":
        temp_b = 12
    elif value_b == "K":
        temp_b = 13
    elif value_b == "A":
        temp_b = 1
    else:
        temp_b = int(value_b)
    # n = 1 określa zasady dla przesuwania kart po stosie głównym i dodatkowym
    if n == 1:
        # sprawdzenie czy karty są w dobrej kolejności i czy mają różne kolory
        if temp_a - 1 == temp_b:
            if (color_a in ["♣", "♠"]) and (color_b in ["♦", "♥"]):
                return True
            elif (color_a in ["♦", "♥"]) and (color_b in ["♣", "♠"]):
                return True
            else:
                return False
        else:
            return False
    # n = 2 określa zasady kładzenia kart na stos końcowy
    elif n == 2:
        if temp_a + 1 == temp_b:
            if color_a == color_b:
                return True
            else:
                return False
        else:
            return False


# funkcja the_end sprawdza czy wszystkie karty zostały ułożone na stosie końcowym
def the_end(end_stock):
    done = 0
    for i in range(len(end_stock)):
        # sprawdzamy tylko długość tablicy bo program nie pozwala na nieprawidłowy układ kart
        if len(end_stock[i]) == 13:
                done += 1
    if done == 4:
        return True
    else:
        return False


# funkcja top_scores odczytuje wyniki z pliku tekstowego, sortuje je i zwraca ranking
def top_scores():
    points = []
    scores = open("wyniki.txt", "r")
    for i in scores:
        i = i.rstrip().split(" ")
        name = i[0]
        score = i[1]
        points.append((name, int(score)))
    scores.close()
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if points[j][1] > points[i][1]:
                points[i], points[j] = points[j], points[i]
    return points


scores = open("wyniki.txt", "a")
moves_counter = 0
name = input("Wprowadź swoje imię: ")
main_cards, extra_cards = start()
end_stocks = [[". "], [". "], [". "], [". "]]
history = [
    (deepcopy(main_cards), deepcopy(extra_cards),
     deepcopy(end_stocks), deepcopy(moves_counter))
]
temp = moves_counter

# określenie poziomu gry
while True:
    lvl = input("Wprowadź 1 by wybrać tryb łatwy lub 2 by wybrać tryb trudny: ")
    if lvl == "1" or lvl == "2":
        break
    else:
        print(f"{Fore.RED}Niepoprawna wartość{Style.RESET_ALL}")

# gra
while True:
    # sprawdzenie czy gra jest zakończona i jeśli tak to zwrócenie rankingu
    if the_end(end_stocks):
        print("Koniec gry! liczba ruchów: " + str(moves_counter))
        print("Ranking:")
        scores.write(name + " " + str(moves_counter) + "\n")
        points = top_scores()
        for i in range(len(points)):
            print(f"{i + 1}. {points[i][0]}: {points[i][1]} pkt")
            input("Naciśnij Enter, aby zakończyć")
        break

    else:
        print(arrangement(main_cards, extra_cards))
        print(end_stocks_arrangement(end_stocks))
        move = input("Wybierz co chcesz zrobić: r (restart), q (quit), u (undo),"
                     " m (move), d (draw), a (aside), n (next): ")

        # restart gry
        if move == "r":
            end_stocks = [[". "], [". "], [". "], [". "]]
            moves_counter = 0
            temp = moves_counter
            name = input("Wprowadź swoje imię: ")
            while True:
                lvl = input("Wprowadź 1 by wybrać tryb łatwy lub 2 by wybrać tryb trudny: ")
                if lvl == "1" or lvl == "2":
                    break
                else:
                    print(f"{Fore.RED}Niepoprawna wartość{Style.RESET_ALL}")
            main_cards, extra_cards = start()
            history = [
                (deepcopy(main_cards), deepcopy(extra_cards),
                 deepcopy(end_stocks), deepcopy(moves_counter))
            ]

        # wyjście z gry i zwrócenie wyniku
        elif move == "q":
            print("Liczba ruchów: " + str(moves_counter))
            input("Naciśnij Enter, aby zakończyć")
            break

        # cofnięcie ruchu do 3 w tył
        elif move == "u":
            if len(history) > 1:
                history.pop(-1)
                main_cards, extra_cards, end_stocks, moves_counter = deepcopy(history[-1])
                temp = moves_counter
            elif len(history) == 1:
                main_cards, extra_cards, end_stocks, moves_counter = deepcopy(history[-1])
                temp = moves_counter
            else:
                print(f"{Fore.RED}Brak ruchów do cofnięcia{Style.RESET_ALL}")

        # przesunięcie kart na stosie głównym
        elif move == "m":
            out_of = input("Wprowadź współrzędne karty, którą chcesz przesunąć: ")
            to = input("Wprowadź współrzędne karty, na którą chcesz położyć powyższą: ")
            try:
                out_of = out_of.split(",")
                to = to.split(",")
                x1 = int(out_of[0])
                y1 = int(out_of[1])
                x2 = int(to[0])
                y2 = int(to[1])

                # jeśli kolumna jest pusta to można polożyć tylko Króla
                if len(main_cards[x2]) == 0:
                    if "K" in main_cards[x1][y1][0]:
                        main_cards[x2].extend(main_cards[x1][y1:])
                        del main_cards[x1][y1:]
                        moves_counter += 1
                        if main_cards:
                            main_cards[x1][y1 - 1][1] = True
                    else:
                        print(f"{Fore.RED}Ruch niezgodny z zasadami{Style.RESET_ALL}")

                else:
                    b = main_cards[x1][y1][0]
                    a = main_cards[x2][y2][0]
                    # sprawdzenie czy ruch jest mozliwy i jego wykonanie lub zwrócenie błędu
                    if rules(a, b, 1) and main_cards[x1][y1][1] and main_cards[x2][y2][1]:
                        to_move = main_cards[x1][y1:]
                        main_cards[x2].extend(to_move)
                        del main_cards[x1][y1:]
                        moves_counter += 1
                        if main_cards[x1]:
                            main_cards[x1][-1][1] = True
                    else:
                        print(f"{Fore.RED}Ruch niezgodny z zasadami{Style.RESET_ALL}")
            except (IndexError, ValueError):
                print(f"{Fore.RED}Złe współrzędne{Style.RESET_ALL}")

        # przenoszenie kart ze stosu dodatkowego na główny
        elif move == "d":
            to = input("Wprowadź współrzędne karty, na którą chcesz położyć odkrytą "
                       "kartę z dodatkowego stosu: ")
            try:
                to = to.split(",")
                x2 = int(to[0])
                y2 = int(to[1])
                # znalezienie odkrytej karty na stosie dodatkowym
                ind = next((i for i, karta in enumerate(extra_cards) if karta[1]), None)
                if ind is not None:
                    # jeśli kolumna jest pusta to można polożyć tylko Króla
                    if len(main_cards[x2]) == 0:
                        if "K" in extra_cards[ind][0]:
                            main_cards[x2].append(extra_cards[ind])
                            extra_cards.pop(ind)
                            moves_counter += 1
                            if ind - 1 >= 0:
                                extra_cards[ind - 1][1] = True
                        else:
                            print(f"{Fore.RED}Ruch niezgodny z zasadami{Style.RESET_ALL}")
                    else:
                        # sprawdzenie czy ruch jest mozliwy i jego wykonanie lub zwrócenie błędu
                        b = extra_cards[ind][0]
                        a = main_cards[x2][y2][0]
                        if rules(a, b, 1):
                            main_cards[x2].append([b, True])
                            extra_cards.pop(ind)
                            moves_counter += 1
                            if ind - 1 >= 0:
                                extra_cards[ind - 1][1] = True
                        else:
                            print(f"{Fore.RED}Ruch niezgodny z zasadami{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Ruch niezgodny  zasadami lub zła komenda{Style.RESET_ALL}")
            except (IndexError, ValueError):
                print(f"{Fore.RED}Złe współrzędne{Style.RESET_ALL}")

        # odkładanie kart na stos końcowy
        elif move == "a":
            out_of = input(
                "Wprowadź współrzędne karty, którą chcesz odłożyć lub napis 'stos', "
                "jeśli jest ona na stosie dodatkowym: ")
            try:
                to = int(input("Wprowadź numer stosu końcowego (0-3): "))
                if to < 0 or to > 3:
                    print(f"{Fore.RED}Niepoprawna wartość{Style.RESET_ALL}")
                    continue
            except ValueError:
                print(f"{Fore.RED}Niepoprawna wartość{Style.RESET_ALL}")
                continue

            # przenoszenie ze stosu dodatkowego
            if out_of == "stos":
                # znalezienie odkrytej karty na stosie dodatkowym
                ind = next((i for i, karta in enumerate(extra_cards) if karta[1]), None)
                if ind is not None:
                    card = extra_cards[ind][0]
                    # jeśli stos końcowy jest pusty to można położyć tylko Asa
                    if end_stocks[to] == [". "]:
                        if card[0] == "A":
                            end_stocks[to] = []
                            end_stocks[to].append(card)
                            extra_cards.pop(ind)
                            moves_counter += 1
                            if ind - 1 >= 0:
                                extra_cards[ind - 1][1] = True
                        else:
                            print(f"{Fore.RED}Ruch niezgodny z zasadami{Style.RESET_ALL}")
                    else:
                        last = end_stocks[to][-1]
                        if rules(last, card, 2):
                            end_stocks[to].append(card)
                            extra_cards.pop(ind)
                            moves_counter += 1
                            if ind - 1 >= 0:
                                extra_cards[ind - 1][1] = True
                        else:
                            print(f"{Fore.RED}Ruch niezgodny z zasadami{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Ruch niezgodny z zasadami lub zła komenda{Style.RESET_ALL}")

            # przenoszenie ze stosu głównego
            else:
                try:
                    out_of = out_of.split(",")
                    x1 = int(out_of[0])
                    y1 = int(out_of[1])
                    card = main_cards[x1][y1][0]
                    if not main_cards[x1][y1][1]:
                        print(f"{Fore.RED}Ta karta nie jest odwrócona{Style.RESET_ALL}")
                        continue

                    # jeśli stos końcowy jest pusty to można położyć tylko Asa
                    if end_stocks[to] == [". "]:
                        if card[0] == "A" and main_cards[x1][y1] == main_cards[x1][-1]:
                            end_stocks[to] = []
                            end_stocks[to].append(card)
                            main_cards[x1].pop(y1)
                            moves_counter += 1
                            if main_cards[x1]:
                                main_cards[x1][-1][1] = True
                        else:
                            print(f"{Fore.RED}Ruch niezgodny z zasadami{Style.RESET_ALL}")
                    else:
                        last = end_stocks[to][-1]
                        if rules(last, card, 2) and main_cards[x1][y1] == main_cards[x1][-1]:
                            end_stocks[to].append(main_cards[x1][y1][0])
                            main_cards[x1].pop(y1)
                            moves_counter += 1
                            if main_cards[x1]:
                                main_cards[x1][-1][1] = True
                        else:
                            print(f"{Fore.RED}Ruch niezgodny z zasadami{Style.RESET_ALL}")

                except (IndexError, ValueError):
                    print(f"{Fore.RED}Złe współrzędne{Style.RESET_ALL}")

        # dobieranie koljnych kart na różnych poziomach trudności
        elif move == "n" and len(extra_cards) > 0:
            moves_counter += 1
            # tryb łatwy
            if lvl == "1":
                current = None
                for i in range(len(extra_cards)):
                    # znalezienie odkrytej karty
                    if extra_cards[i][1]:
                        # wymieszanie kart jeśli wszystkie zostaną odkryte lub pokazanie kolejnej
                        current = extra_cards[i]
                        if i == 0:
                            shuffle(extra_cards)
                            for j in range(len(extra_cards)):
                                extra_cards[j][1] = False
                            extra_cards[-1][1] = True
                        else:
                            extra_cards[i][1] = False
                            extra_cards[i - 1][1] = True
                        break
                if current is None:
                    extra_cards[-1][1] = True
            # tryb trudny
            elif lvl == "2":
                current = None
                # znalezienie odkrytej karty
                for i, card in enumerate(extra_cards):
                    if card[1]:
                        current = i
                        break

                if current is None:
                    extra_cards[-1][1] = True
                # wymieszanie kart jeśli wszystkie zostaną odkryte lub pokazanie kolejnej z przesunięciem o 3
                else:
                    extra_cards[current][1] = False
                    new = current - 3
                    if new < 0:
                        shuffle(extra_cards)
                        new = len(extra_cards) - 1 - (len(extra_cards) % 3)
                    extra_cards[new][1] = True

        else:
            print(f"{Fore.RED}Zła komenda{Style.RESET_ALL}")
        # sprawdzenie czy wykonano ruch i zapisanie go
        if moves_counter > temp:
            history.append(
                (deepcopy(main_cards), deepcopy(extra_cards),
                 deepcopy(end_stocks), deepcopy(moves_counter))
            )
            temp = moves_counter
        # usunięcie starych ruchów z historii
        if len(history) > 4:
            history.pop(0)

scores.close()
