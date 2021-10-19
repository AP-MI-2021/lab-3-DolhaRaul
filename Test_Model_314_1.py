from math import sqrt

def read_list():
    lst = []
    numere = input('Introduceti numere separate prin spatiu/virgula aici: ')
    numere_split = numere.split(' ')
    for num in numere_split:
        lst.append(int(num))
    return lst

def is_prime(n):
    '''
    Functia determina daca un numar n este prim sau nu
    :param n: Un nr natural n
    :return: True daca este prim sau False in caz contrar
    '''
    if n < 2: return False
    if n == 2: return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def Test_is_prime():
    assert is_prime(5) == True
    assert is_prime(4) == False
    assert is_prime(3) == True
    assert is_prime(13 * 19) == False
    assert is_prime(1) == False
    assert is_prime(0) == False

def remove_primes(lst):
    result = []
    for num in lst:
        if is_prime(num) == False:
            result.append(num)
    return result

def test_remove_primes():
    assert remove_primes([8, 19, 17, 25]) == [8, 25]
    assert remove_primes([]) == []
    assert remove_primes([19, 17, 25]) == [25]

def number_quantity(lst, n):
    '''
    Functia returneaza nr de aparitii al unui nr intr o lista
    :param lst: O lista de int
    :param n: Un nr natural n
    :return: Nr de aparitii ale lui n in lst
    '''
    cnt = 0
    for num in lst:
        if num == n:
            cnt += 1
    return cnt

def tuple_poz_quantity(lst):
    '''
    Functia returneaza o lista de tuple, in care fiecare element este inlocuit cu (tuple, index, nr de aparitii)
    :param lst: O lista de int
    :return: O lista de tuple uri
    '''
    result = []
    for i in range(len(lst)):
        cnt = number_quantity(lst, lst[i])
        result.append((lst[i], i, cnt))
    return result

def test_tuple_poz_quantity():
    assert tuple_poz_quantity([25, 13, 26, 13]) == [(25, 0, 1), (13, 1, 2), (26, 2, 1), (13, 3, 2)]
    assert tuple_poz_quantity([25, 26, 13]) == [(25, 0, 1), (26, 1, 1), (13, 2, 1)]
    assert tuple_poz_quantity([]) == []

def main():
    lst = []
    while True:
        optiune = input('Introduceti optiunea dorita aici: ')
        if optiune == '1':
            lst = read_list()
        elif optiune == '2':
            print(remove_primes(lst))
        elif optiune == '3':
            pass
        elif optiune == '4':
           pass
        elif optiune == '5':
            print(tuple_poz_quantity(lst))
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')

if __name__ == '__main__':
    test_tuple_poz_quantity()
    test_remove_primes()
    Test_is_prime()
    main()