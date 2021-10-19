from math import sqrt
def read_list():
    lst = []
    numere = input('Introduceti numere separate prin spatiu/virgula aici: ')
    numere_split = numere.split(', ')
    for num in numere_split:
        lst.append(int(num))
    return lst

def number_10_power(n):
    '''
    Functia returneaza numarul 10 ridicat puterea rerezentata de numarul de cifre ale numarului n
    :param n: Un nr n, n >= 0
    :return: Puterea lui 10 formata din numarul de cifre ale lui n
    '''
    p = 10
    cn = n
    while cn >= 9:#cat timp nu are inca o cifra
        cn //= 10
        p *= 10
    return p

def test_number_10_power():
    assert number_10_power(5) == 10
    assert number_10_power(0) == 10
    assert number_10_power(12) == 100
    assert number_10_power(123) == 1000

def concatenare_lista(lst):
    '''
    Functia retunreaza numarul concatenat din lista, format doar din cele pozitive
    :param lst:O lista de int
    :return:Numarul fomrat din concatenarea numerelor pozitive
    '''
    n = len(lst)
    result = 0
    for i in range(n):
        if lst[i] >= 0:#e un numar pozitiv
            result *= number_10_power(lst[i])
            result += lst[i]
    return result

def test_concatenare_lista():
    assert  concatenare_lista([0, 8, 23, -13, 25]) == 82325
    assert  concatenare_lista([0, 8, 23, 13, 25]) == 8231325
    assert  concatenare_lista([5]) == 5
    assert  concatenare_lista([0, -1, -2, -3]) == 0

def min_in_list(lst):
    '''
     Functia retunreaza cel mai mic nr din lista
    :param lst: O lista de numere intregi
    :return: Cel mai mic nr din lista
    '''
    min = lst[0]
    for i in range(len(lst)):
        if lst[i] < min:
            min = lst[i]
    return min

def max_in_list(lst):
    '''
    Functia retunreaza cel mai mare nr din lista
   :param lst: O lista de numere intregi
   :return: Cel mai mare nr din lista
   '''
    max = lst[0]
    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
    return max

def test_min_in_list():
    assert min_in_list([0, 2, -2]) == -2
    assert min_in_list([0, 1, 0]) == 0
    assert min_in_list([2, 2, 3, 3]) == 2

def test_max_in_list():
    assert max_in_list([0, 2, -2]) == 2
    assert max_in_list([0, 1, 0]) == 1
    assert max_in_list([2, 2, 3, 3]) == 3

def sum_max_and_min(lst):
   '''
   Functia retunreaza suma dintre minimul listei si maximul acesteia
   :param lst:O lista de int
   :return: Suma ceruta
   '''
   min = min_in_list(lst)
   max = max_in_list(lst)
   result = min + max
   return result

def test_sum_max_and_min():
    assert  sum_max_and_min([10, -3, 25, -1, 3, 25, 18]) == 22
    assert  sum_max_and_min([10, 25, -1, 3, 25, 18]) == 24
    assert  sum_max_and_min([-3, -5]) == -8
    assert  sum_max_and_min([0]) == 0

def sum_cif(n):
    '''
    Functia retunreaza suma cifrelor unui nr n introdus de utilizator
    :param n: Un nr nat n
    :return: Suma cifrelor acestuia
    '''
    sum_cif = 0
    cn = n
    while cn != 0:
        sum_cif += cn % 10
        cn = cn // 10
    return sum_cif

def numbers_with_sum_cif_bigger_than(lst, n):
    '''
    Functia retunreaza o lista cu numerele din lista initiala cu propr ca au suma cifrelor mai mare ca n
    :param lst:O lista de numere naturale
    :param n:Un nr nat introdus de utlizator
    :return:O lista cu numerele cerute
    '''
    result = []
    size = len(lst)
    for i in range(size):
        if sum_cif(lst[i]) >= n:
            result.append(lst[i])
    return result

def test_numbers_with_sum_cif_bigger_than():
    assert numbers_with_sum_cif_bigger_than([25, 11, 10, 24, 39], 7) == [25, 39]
    assert numbers_with_sum_cif_bigger_than([25, 11, 10, 24, 39], 0) == [25, 11, 10, 24, 39]

def all_perfect_squares_lesser_than(n):
    '''
    Functia retunreaza patratele perfecte mai mici decat un nr nat n, intr o lista
    :param n: Un nr nat n
    :return: O lista de p.p mai mici decat n
    '''
    d = 1
    lst = []
    while d * d < n:#n nu este patrat pefect
        lst.append(d * d)
        d += 1
    return lst

def swap_not_perfect_square_with_squares(lst):
    '''Functia inlocuieste fiecare nr p,p cu radcalul sau, sau numarul cu toate p.p mai mici decat el(intr o lista) din lista
    initiala
    :param lst:
    :param n:
    :return:
    '''
    n = len(lst)
    result = []
    for i in range(n):
        if lst[i] >= 0 and sqrt(lst[i]) == int(sqrt(lst[i])):#e patrat perfect
            result.append(int(sqrt(lst[i])))
        elif lst[i] >= 0:
            result.append(all_perfect_squares_lesser_than(lst[i]))
        else:
            result.append(lst[i])
    return result

def test_swap_not_perfect_square_with_squares():
    assert swap_not_perfect_square_with_squares([25, 13, 26, 9, -4, 0]) == [5, [1, 4, 9], [1, 4, 9, 16, 25], 3, -4, 0]
    assert swap_not_perfect_square_with_squares([25, 4, 1]) == [5, 2, 1]
    assert swap_not_perfect_square_with_squares([]) == []

def main():
    lst = []
    while True:
        optiune = input('Introduceti optiunea dorita aici: ')
        if optiune == '1':
            lst = read_list()
        elif optiune == '2':
            print(concatenare_lista(lst))
        elif optiune == '3':
            print(sum_max_and_min(lst))
        elif optiune == '4':
            n = int(input('Introduceti numarul aici: '))
            print(numbers_with_sum_cif_bigger_than(lst, n))
        elif optiune == '5':
            print(swap_not_perfect_square_with_squares(lst))
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')

if __name__ == '__main__':
    test_swap_not_perfect_square_with_squares()
    test_numbers_with_sum_cif_bigger_than()
    test_sum_max_and_min()
    test_min_in_list()
    test_max_in_list()
    test_concatenare_lista()
    test_number_10_power()
    main()

