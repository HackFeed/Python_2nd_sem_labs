""" Модуль, отвечающий за работу пирамидальной сортировки
(она же сортировка кучей, она же heapsort). В данном модуле
представлено 3 функции, которые отвечают за формирование кучи,
непосредственно сортировку и иллюстрированную сортировку. """


def heapify(in_list, n, i):
    """ Функция формирования кучи (фактически бинарное дерево).

    Передаваемые параметры:
    * in_list - исходный список
    * n - длина списка
    * i - текущий узел кучи

    Функция изменяет передаваемый массив, а не создаёт копию и
    работает с ней.

    """

    largest_node = i  # Инициализировать корень как наибольший узел
    left_s = 2 * i + 1  # Инициализация левого поддерева
    right_s = 2 * i + 2  # Инициализация правого поддерева

    """ Проверка на существование левых и правх поддеревьев
    и сравнение их с корнем. """
    if left_s < n and in_list[i] < in_list[left_s]:
        largest_node = left_s

    if right_s < n and in_list[largest_node] < in_list[right_s]:
        largest_node = right_s

    """ Смена корня. """
    if largest_node != i:
        in_list[i], in_list[largest_node] = in_list[largest_node], in_list[i]

        """ Новое формирование кучи. """
        heapify(in_list, n, largest_node)


def heapsort(in_list):
    """" Функция сортировки кучей.

    Передаваемые параметры:
    * in_list - исходный список

    Возвращаемые значения:
    * in_list - остортированный список

    """

    n = len(in_list)

    """ Формирование максимальной кучи (куча, у узлов которой
    каждый родитель больше потомков). """
    for i in range(n, -1, -1):
        heapify(in_list, n, i)

    """ Замена корня с последним элементом, "удаление"
    последнего элемента из дерева. """
    for i in range(n - 1, 0, -1):
        in_list[i], in_list[0] = in_list[0], in_list[i]
        heapify(in_list, i, 0)

    return in_list


def step_by_step_heapsort(in_list):
    """ Аналог функции heapsort, только с выводом
    каждого шага в консоль.

    Передаваемые параметры:
    * in_list - исходный список

    Возвращаемые значения:
    * res_str - ход действий для сортировки списка

    """

    res_str = ""

    try:
        n = len(in_list)
        for i in range(n, -1, -1):
            heapify(in_list, n, i)
            in_list_cp = in_list[:]
        res_str += "Формируем максимальную кучу\n" + str(in_list_cp) + "\n"

        for i in range(n - 1, 0, -1):
            in_list[i], in_list[0] = in_list[0], in_list[i]
            in_list_cp = in_list[:]
            res_str += "Меняем корень с последним узлом\n" + \
                str(in_list_cp) + "\n"
            heapify(in_list, i, 0)
            in_list_cp = in_list[:]
            res_str += "Формируем максимальную кучу\n" + str(in_list_cp) + "\n"

        return res_str

    except TypeError:
        return res_str


""" Тестовый вызов.

test_list = [-9, 2, 4, -15, 6, 15]
new_test_list = test_list[:]

print(test_list)
print("*********************")
print(step_by_step_heapsort(new_test_list))
print("*********************")
print(heapsort(new_test_list))

"""
