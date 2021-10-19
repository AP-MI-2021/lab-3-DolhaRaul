def read_list():
    '''
    Functia retunreaza o lista de numere intregi pe care utilizatorul le introduce separate prin spatiu
    :return: O lista de int
    '''
    lst = []
    numere = input('Introduceti numere separate prin spatiu aici: ')
    numere_sir = numere.split(' ')
    for num in numere_sir:
        lst.append(int(num))
    return lst

def list_with_no_duplicates(lst):
    '''
    Functia returneaza lista numerelor din lista, fara duplicate. in ordinea in care apar
    :param lst: O lista de numere intregi
    :return: Lista initiala din care se elimina duplicatele(in ordine)
    '''
    result = []
    n = len(lst)
    for dr in range(n):
        unique = True #nu apare de mai multe ori
        for st in range(dr):
            if lst[dr] == lst[st]:#se repeta
                unique = False
        if unique == True:#e unicat
            result.append(lst[dr])
    return result

def test_list_with_no_duplicates():
    assert list_with_no_duplicates([10, 25, 13, 25, 48, 10, 25]) == [10, 25, 13, 48]
    assert list_with_no_duplicates([25]) == [25]
    assert list_with_no_duplicates([10, 25, 10, 25]) == [10, 25]
    assert list_with_no_duplicates([]) == []

def sum_first_n_positive_numbers(lst, n):
    '''
    Functia returneaza suma primelor n numere pozitive din lista sau mesajul din cerinta in caz ca nu avem n numere pozitive
    :param lst: O lista de numere (float) transmisa ca parametru
    :param n: Un numar natural n introdus de utlizator
    :return: Suma primelor n numere pozitive din lista sau mesajul "Dimensiunea listei este prea mica"
    '''
    cnt = 0
    sum = 0
    size = len(lst)
    for i in range(size):
        if lst[i] > 0: #am gasit un nr pozitiv
            cnt += 1
            sum += lst[i]
        if cnt == n:
            break# am gasit cele n numere
    if cnt < n:
        return "Dimensiunea listei este prea mica"#nu am gasit n nr pozitive
    elif cnt >= n:
        return sum

def test_sum_first_n_positive_numbers():
    assert sum_first_n_positive_numbers([10, -3, 25, -1, 3, 25, 18], 3) == 38
    assert sum_first_n_positive_numbers([3, 25, -1, 3, 25, 18], 3) == 31
    assert sum_first_n_positive_numbers([-1, 3, 25, 18], 3) == 46
    assert sum_first_n_positive_numbers([-1, 3, 25], 3) == "Dimensiunea listei este prea mica"


def list_positive_numbers_are_in_growing_order(lst):
    '''
    Functia returneaza mesajul "DA" daca numere pozitive din lista sunt in ordine crescatoare sau "NU" in caz contrat
    :param lst: O lista de numere(float, fiindca nu se epcifica)
    :return: Mesajul "DA" sau "NU" in fucntie de caz
    '''
    all_in_order = True
    n = len(lst)
    for st in range(n):
        if lst[st] > 0:
            for dr in range(st, n):
                if lst[dr] > 0 and lst[dr] < lst[st]:#lista nu e in ordine crescatoare
                    all_in_order = False
    if all_in_order == True:
        return "DA"
    return "NU"

def test_list_positive_numbers_are_in_growing_order():
    assert list_positive_numbers_are_in_growing_order([10, 13, -1, 24, 33, 45]) == "DA"
    assert list_positive_numbers_are_in_growing_order([10, 13, -1, 24, 23, 45]) == "NU"
    assert list_positive_numbers_are_in_growing_order([]) == "DA"
    assert list_positive_numbers_are_in_growing_order([7, 5, -1, -2]) == "NU"

def is_unique(lst, poz):
    '''
    Functia retunreaza True sau False daca numarul de pe pozitia poz din lista este unica sau nu
    :param lst: O lista de numere(float)
    :param poz: Pozitia elementului in lista
    :return: True sau False in functie de caz
    '''
    only_one = 0
    n = len(lst)
    for i in range(n):
        if lst[i] == lst[poz]:
            only_one += 1
    if only_one != 1:#apare de mai mult ori
        return False#nu e unic
    return True

def test_is_unique():
    assert is_unique([1, 2, 3, 4, 4], 3) == False
    assert is_unique([1, 2, 3, 4], 3) == True
    assert is_unique([1, 2, 3, 4, 1], 0) == False
    assert is_unique([1, 2, 3, 2, 1], 2) == True

def numbers_of_divisors(n):
    '''
    Functia retunreaza numarul de divizori al unui numar(cei diferiti de 1 si el insusi) al unui numar n
    :param n: Un numar natural n introdus de utulizator
    :return: Numarul de divizori proprii al acestuia
    '''
    numbers_of_div = 0
    for i in range(2, n):
        if n % i == 0:#este divizor propriu
            numbers_of_div += 1
    return numbers_of_div

def test_numbers_of_divisors():
    assert numbers_of_divisors(5) == 0
    assert numbers_of_divisors(6) == 2
    assert numbers_of_divisors(12) == 4
    assert numbers_of_divisors(1) == 0


def swap_unique_numb_with_their_divisors(lst):
    '''
    Functia inlocuieste nr care apar o singura data cu nr lor de divizori proprii
    :param lst: O lista de numere intregi(chiar naturale)
    :return:O lista in care fiecare numar "unic" este inlocuit in lista initiala cu nr lui de divizori
    '''
    result = []
    n = len(lst)
    for i in range(n):
        if is_unique(lst, i):
            result.append(numbers_of_divisors(lst[i]))
        else:
            result.append(lst[i])
    return result

def test_swap_unique_numb_with_their_divisors():
    assert swap_unique_numb_with_their_divisors([25, 13, 26, 13, 19]) == [1, 13, 2, 13, 0]
    assert swap_unique_numb_with_their_divisors([25, 13, 26, 13, 19, 25]) == [25, 13, 2, 13, 0, 25]
    assert swap_unique_numb_with_their_divisors([25, 13, 26, 13, 18]) == [1, 13, 2, 13, 4]
    assert swap_unique_numb_with_their_divisors([]) == []

def main():
    lst = []
    while True:
        optiune = input("Introduceti problema/cerinta dorita aici: ")
        if optiune == '1':
            lst = read_list()
        elif optiune == '2':
            print(list_with_no_duplicates(lst))
        elif optiune == '3':
            n = int(input("Introduceti numarul de numere aici: "))
            print(sum_first_n_positive_numbers(lst, n))
        elif optiune == '4':
            print(list_positive_numbers_are_in_growing_order(lst))
        elif optiune == '5':
            print(swap_unique_numb_with_their_divisors(lst))
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida")

if __name__ == '__main__':
    test_swap_unique_numb_with_their_divisors()
    test_numbers_of_divisors()
    test_is_unique()
    test_list_positive_numbers_are_in_growing_order()
    test_sum_first_n_positive_numbers()
    test_list_with_no_duplicates()
    main()
