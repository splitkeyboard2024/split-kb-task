# Napisz funkcję, która zwraca tekst (podany jako argument) oddzielając każde słowo przecinkiem i wypisując maksymalnie 5 słów w rzędzie.
# UWAGA! Przypadki testowe mogą zawierać znaki .,?!, znaki nowej linii \n i spacje na początku i końcu tekstu.

# Input example 1:
# Wlazł kotek na płotek i mruga. Ładna to piosenka, niedługa
# Output:
# Wlazł, kotek, na, płotek, i
# mruga, Ładna, to, piosenka, niedługa

# Input example 2:
# To be, or not to be?\nThat is the question!
# Output:
# To, be, or, not, to
# be, That, is, the, question


def parse_text(input: str) -> str:
    input = input.strip().replace('?', ' ').replace('!', ' ').replace('\n', ' ').replace('.', ' ').replace(',', ' ')
    words = input.split()
    output = []
    for i in range(0, len(words), 5):
        output.append(', '.join(words[i:i+5]))
    return '\n'.join(output)


def parse_generator(input: str) -> str:
    input = input.strip().replace('?', ' ').replace('!', ' ').replace('\n', ' ').replace('.', ' ').replace(',', ' ')
    words = input.split()

    def group_words(words, n):
        for i in range(0, len(words), n):
            yield words[i:i+n]

    output = [', '.join(group) for group in group_words(words, 5)]
    return '\n'.join(output)

def parse_comprehensions(input: str) -> str:
    input = input.strip().replace('?', ' ').replace('!', ' ').replace('\n', ' ').replace('.', ' ').replace(',', ' ')
    words = input.split()
    output = [', '.join(words[i:i+5]) for i in range(0, len(words), 5)]
    return '\n'.join(output)

def parse_one_liner(input: str) -> str:
    return '\n'.join([', '.join(input.strip().replace('?', ' ').replace('!', ' ').replace('\n', ' ').replace('.', ' ').replace(',', ' ').split()[i:i+5]) for i in range(0, len(input.split()), 5)])
