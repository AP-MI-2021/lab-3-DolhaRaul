def read_list():#citire de lista
    lst = []
    sir_numere = input('Dati valorile separate prin spatiu: ')
    sir_numere_split = sir_numere.split(' ')
    for num in sir_numere_split:
        lst.append(int(num))
    return lst

#Problema 1

def get_longest_alternating_signs(lst):
    result = []
    n = len(lst)
    for st in range(n):
        for dr in range(st + 1, n):
            alternating_signs = True
            for v in range(st + 1, dr + 1):
                if lst[v] * lst[v - 1] >= 0: #au acelasi semn
                    alternating_signs = False
            if alternating_signs == True:#am gasit o secventa
                if dr - st + 1 > len(result):
                    result = lst[st:dr + 1]#am gasit o noua cea mai lunga secventa
    return result

def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([1, -1, 2, -2]) == [1, -1, 2, -2]
    assert get_longest_alternating_signs([1, -1, 2, 2]) == [1, -1, 2]
    assert get_longest_alternating_signs([1, 1, 1]) == []
    assert get_longest_alternating_signs([3, 4, 5, -6]) == [5, -6]
    assert get_longest_alternating_signs([-1, 1, 10, 20]) == [-1, 1]

#Problema 2

def prime_digit(n):#verifica daca o cfifra e prima
    if n == 2:
        return True
    if n == 3:
        return True
    if n == 5:
        return True
    if n == 7:
        return True
    return False

def only_prime_digits(n):#verifica daca numarul e format doar din cifre prime
    cn = n
    while cn != 0:
        if prime_digit(cn % 10) == False:
            return False
        cn = cn // 10
    return True

def test_only_prime_digits():
    assert only_prime_digits(3) == True
    assert only_prime_digits(127) == False
    assert only_prime_digits(334) == False
    assert only_prime_digits(35) == True
    assert only_prime_digits(345) == False

def get_longest_prime_digits(lst):
    result = []
    n = len(lst)
    for st in range(n):
        for dr in range(st, n):
            all_only_prime_digits = True
            for v in range(st, dr + 1):
                if only_prime_digits(lst[v]) == False:
                    all_only_prime_digits = False
            if all_only_prime_digits == True:#am mai gasit inca o secventa ce verifica
                if dr - st + 1 == len(result):
                    result = lst[st:dr + 1]  # secventa de lungime egala cu cea maxima
                if dr - st + 1 > len(result):
                    result = lst[st:dr + 1] #secenta de lung maxima
    return result

def test_get_longest_prime_digits():
    assert get_longest_prime_digits([1, 2, 3]) == [2, 3]
    assert get_longest_prime_digits([1, 2, 345]) == [2]
    assert get_longest_prime_digits([1, 1, 1]) == []
    assert get_longest_prime_digits([23, 27, 355]) == [23, 27, 355]



def main():
    lst = []
    while True:
        optiune = input("Selectati ce optiune doriti: ")
        if optiune == '1':#Citirea datelor
            lst = read_list()
        elif optiune == '2':#Prima problema
            print(get_longest_alternating_signs(lst))
        elif optiune == '3':#Problema a 2-a
            primes =  get_longest_prime_digits(lst)
            print(primes)
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida")
if __name__ == '__main__':
    test_get_longest_prime_digits()
    test_only_prime_digits()
    test_get_longest_alternating_signs()
    main()