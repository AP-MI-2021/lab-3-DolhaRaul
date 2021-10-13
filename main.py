def read_list():#citire de lista
    '''
    Introducem intr o lista numerele introduse de utilizator(textul va fi de tip string, deci numerele le separam)
    '''
    lst = []
    sir_numere = input('Dati valorile separate prin spatiu: ')
    sir_numere_split = sir_numere.split(' ')
    for num in sir_numere_split:
        lst.append(int(num))
    return lst

#Problema 1

def get_longest_alternating_signs(lst):
    '''
    Determina cea mai lunga subsecventa de numere cu semne alternante(daca sunt mai multe, se afiseaza oricare)
    Input:
    -o lista de numere intregi
    Output:
    -cea mai lunga subsecventa de numere intregi din lista
    '''
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
    '''
    Functia testeaza diferite exemple pentru subprogramul get_longest_alternating_signs(ca la seminar)
    '''
    assert get_longest_alternating_signs([1, -1, 2, -2]) == [1, -1, 2, -2]
    assert get_longest_alternating_signs([1, -1, 2, 2]) == [1, -1, 2]
    assert get_longest_alternating_signs([1, 1, 1]) == []
    assert get_longest_alternating_signs([3, 4, 5, -6]) == [5, -6]
    assert get_longest_alternating_signs([-1, 1, 10, 20]) == [-1, 1]

#Problema 2

def prime_digit(n):#verifica daca o cfifra e prima
    '''
    Functia verifica daca o cifra este prima sau nu
    Input:
    -O cifra de la 0 la 0
    Output:
    -returneaza True daca cifra e prima sau False in caz contrar
    '''
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
    '''
    Verifica daca un numar esre format doar din cifre prime
    Input:
    -un unmar natural introdus de utilizator
    Output:
    -True daca numarul are doar cifre prime sau False in caz contrar
    :param n:
    '''
    cn = n
    while cn != 0:
        if prime_digit(cn % 10) == False:
            return False
        cn = cn // 10
    return True

def test_only_prime_digits():
    '''
    Functia testeaza diferite exemple pentru subprogramul only_prime_digits(ca la seminar)
    '''
    assert only_prime_digits(3) == True
    assert only_prime_digits(127) == False
    assert only_prime_digits(334) == False
    assert only_prime_digits(35) == True
    assert only_prime_digits(345) == False

def get_longest_prime_digits(lst):
    '''
    Determina cea mai lunga subsecventa de numere cu doar cu cifre prime(daca sunt mai multe, se afiseaza oricare)
    Input:
    -o lista de numere intregi
    Output:
    -cea mai lunga subsecventa de numere intregi doar cu cifre prime din lista
    '''
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
    '''
    Functia testeaza diferite exemple pentru subprogramul get_longest_prime_digits(ca la seminar)
    '''
    assert get_longest_prime_digits([1, 2, 3]) == [2, 3]
    assert get_longest_prime_digits([1, 2, 345]) == [2]
    assert get_longest_prime_digits([1, 1, 1]) == []
    assert get_longest_prime_digits([23, 27, 355]) == [23, 27, 355]


def get_longest_product_is_odd(lst): #Problema in plus
    '''
    Determina cea mai lunga subsecventa de numere impare (daca sunt mai multe, se afiseaza oricare)
    Input:
    -o lista de numere intregi
    Output:
    -cea mai lunga subsecventa de numere intregi impare din lista
    '''
    result = []
    n = len(lst)
    for st in range(n):
        for dr in range(st, n):
            all_numbers_are_odds = True
            for num in range(st, dr + 1):
                if lst[num] % 2 == 0: #am gasit un numar par
                    all_numbers_are_odds = False
            if all_numbers_are_odds == True: #Toate numerele sunt impare
                if dr - st + 1 > len(result):
                    result = lst[st:dr + 1]
    return result

def test_get_longest_product_is_odd():
    '''
    Functia testeaza diferite exemple pentru subprogramul get_longest_product_is_odd(ca la seminar)
    '''
    assert get_longest_product_is_odd([1, 3, 5]) == [1, 3, 5]
    assert get_longest_product_is_odd([2, 4, 6]) == []
    assert get_longest_product_is_odd([1, 3, 4]) == [1, 3]
    assert get_longest_product_is_odd([2 , 4, 3, 5]) == [3, 5]


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
        elif optiune == '4':#Problema in plus
            odds = get_longest_product_is_odd(lst)
            print(odds)
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida")

if __name__ == '__main__':
    test_get_longest_product_is_odd()
    test_get_longest_prime_digits()
    test_only_prime_digits()
    test_get_longest_alternating_signs()
    main()