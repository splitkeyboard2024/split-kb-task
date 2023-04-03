# Napisz funkcję, która wypisuje tekst (podany jako argument) oddzielając każde słowo przecinkiem i wypisując maksymalnie 5 słów w rzędzie.
#

# Input:
# Wlazł kotek na płotek i mruga. Ładna to piosenka, niedługa. Niedługa, niekrótka lecz w sam raz, zaśpiewaj koteczku jeszcze raz.
# Output:
# Wlazł, kotek, na, płotek, i
# mruga, Ładna, to, piosenka, niedługa
# Niedługa, niekrótka, lecz, w, sam
# raz, zaśpiewaj, koteczku, jeszcze, raz


def parse(input):
    res = []
    N = 5
    strip_s = ''.join(filter(lambda x: str.isalnum(x) or x == ' ' or x == '\n', input.strip()))
    # strip_s = input
    words = strip_s.split()
    for i in range(0, len(words), N):
        res.append(', '.join(words[i:i+N]))
    return '\n'.join(res)
