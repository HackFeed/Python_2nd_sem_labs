from tkinter import *
from tkinter import messagebox
from random import randint
from time import time
from BMSTUlab2_heapsort import *


def int_list_getter(in_entry):
    try:
        int_list = [int(x) for x in in_entry.get().strip().split()]

        if len(int_list) == 0 or len(int_list) > 5 or \
                isinstance(int_list, (str, type(None))):
            raise ValueError

        return int_list

    except ValueError:
        messagebox.showerror("Ошибка ввода данных", "Данные введены "
                                                    "некорректно, проверьте "
                                                    "правильность ввода!")


def label_writer(to_write, label_out):
    label_out["text"] = ""
    label_out["text"] += to_write


def clean_entry(*entries):
    """ Функция очистки полей ввода.

    Данная функция очищает поля ввода/вывода данных.
    Очистка может производиться как одного, так и сразу
    нескольких полей.

    Передаваемые параметры:
    * *entries - поля ввода, которые надо очистить

    """

    for entry in entries:
        entry.config(state="normal")
        entry.delete(0, END)


def clean_label(*labels):
    for label in labels:
        label["text"] = ""


def sort_visual():
    sort_visual_window = Toplevel(root)
    sort_visual_window.grab_set()
    sort_visual_window.iconbitmap("icon.ico")
    sort_visual_window.geometry("300x500+425+250")
    sort_visual_window.resizable(False, False)
    sort_visual_window.title("Визуализация сортировки кучей (heapsort)")
    sort_visual_window.config(bg="#000080")

    s_v_w_welcome_label = Label(sort_visual_window,
                                text="\nВведите массив малой размерности:\n",
                                font="consolas 10",
                                bg="#000080",
                                fg="white")
    s_v_w_welcome_label.pack()

    s_v_w_entry = Entry(sort_visual_window, width=30)
    s_v_w_entry.pack()

    s_v_w_entry.focus_set()

    s_v_w_separate_label = Label(sort_visual_window,
                                 text="",
                                 bg="#000080")
    s_v_w_separate_label.pack()

    sort_visual_button = Button(sort_visual_window, text="Отсортировать",
                                width=16,
                                height=2,
                                font="consolas 10 bold",
                                bg="white",
                                fg="#0ad325",
                                command=lambda:
                                label_writer(step_by_step_heapsort(
                                    int_list_getter(s_v_w_entry)),
                                    s_v_w_result_label))
    sort_visual_button.pack()

    s_v_w_separate_label = Label(sort_visual_window,
                                 text="",
                                 bg="#000080")
    s_v_w_separate_label.pack()

    s_v_w_result_label = Label(sort_visual_window, text="",
                               width=32,
                               height=19,
                               bg="#000080",
                               fg="white",
                               font="consolas 10 bold")
    s_v_w_result_label.pack()

    exit_visual_button = Button(sort_visual_window, text="Выйти",
                                width=16,
                                height=2,
                                font="consolas 10 bold",
                                bg="white",
                                fg="#ff0000",
                                command=lambda: exit_run(sort_visual_window))
    exit_visual_button.pack()


def sort_timingly(size, dim_list):
    if size < 1 or dim_list[0] >= dim_list[1]:
        messagebox.showerror("Ошибка ввода", "Введены некорректные данные!\n"
                             "Проверьте правильность ввода.")
    else:
        random_list = list()
        time_list = list()

        for i in range(size):
            random_list.append(randint(dim_list[0], dim_list[1]))

        ascending_sorted_list = random_list[:]
        heapsort(ascending_sorted_list)
        start_time = time()
        heapsort(ascending_sorted_list)
        end_time = time()

        time_list.append(round(end_time - start_time, 4))

        random_sorted_list = random_list[:]
        heapsort(random_sorted_list)
        start_time = time()
        heapsort(random_sorted_list)
        end_time = time()

        time_list.append(round(end_time - start_time, 4))

        descending_sorted_list = random_list[:]
        heapsort(descending_sorted_list)
        descending_sorted_list.reverse()
        start_time = time()
        heapsort(descending_sorted_list)
        end_time = time()

        time_list.append(round(end_time - start_time, 4))

        sort_sorted_list = random_list[:]
        start_time = time()
        sort_sorted_list.sort()
        end_time = time()

        time_list.append(round(end_time - start_time, 4))

        return time_list


def about():
    """" Вывод окна "О программе" """
    about_window = Toplevel(root)
    about_window.grab_set()
    about_window.iconbitmap("icon.ico")
    about_window.geometry("330x200+425+250")
    about_window.resizable(False, False)
    about_window.title("О HeapSorter")
    about_window.config(bg="#000080")

    about_label1 = Label(about_window,
                         text="\nВизуализация пирамидальной\n "
                              "сортировки и сравнение времени, отведенного\n"
                              "на сортировку массивов различного\n"
                              "типа этим способом"
                              "\n\n"
                              "Kononenko Sergey ICS7-23B",
                         font="consolas 10",
                         bg="#000080",
                         fg="white")
    about_label1.pack()

    about_label2 = Label(about_window,
                         text="@hackfeed",
                         font="consolas 10 bold",
                         bg="white",
                         fg="#000080")
    about_label2.pack()

    exit_about = Button(about_window, text="Выйти",
                        width=6,
                        height=2,
                        font="consolas 10 bold",
                        bg="#000080",
                        fg="white",
                        relief="flat",
                        command=lambda: exit_run(about_window))
    exit_about.pack()


def exit_run(root):
    """ Выход из программы. """
    root.destroy()


""" Создание каскада окна программы. """
root = Tk()
root.iconbitmap("icon.ico")
root.geometry("593x320+400+200")
root.resizable(False, False)
root.title("HeapSorter")

""" Создание меню. """
main_menu = Menu(root)
root.config(menu=main_menu, bg="#000080")

clean_menu = Menu(main_menu, tearoff=0)
clean_menu.add_command(label="Очистить поле ввода N1",
                       command=lambda: clean_entry(n1_entry, n1_count_entry))
clean_menu.add_command(label="Очистить поле вывода N1",
                       command=lambda: clean_label(label_out_n1))
clean_menu.add_separator()
clean_menu.add_command(label="Очистить поле ввода N2",
                       command=lambda: clean_entry(n2_entry, n2_count_entry))
clean_menu.add_command(label="Очистить поле вывода N2",
                       command=lambda: clean_label(label_out_n2))
clean_menu.add_separator()
clean_menu.add_command(label="Очистить поле ввода N3",
                       command=lambda: clean_entry(n3_entry, n3_count_entry))
clean_menu.add_command(label="Очистить поле вывода N3",
                       command=lambda: clean_label(label_out_n3))
clean_menu.add_separator()
clean_menu.add_command(label="Очистить все поля",
                       command=lambda: (clean_entry(n1_entry, n1_count_entry,
                                                    n2_entry, n2_count_entry,
                                                    n3_entry, n3_count_entry),
                                        clean_label(label_out_n1,
                                                    label_out_n2,
                                                    label_out_n3)))

workmode_menu = Menu(main_menu, tearoff=0)
workmode_menu.add_command(label="Режим визуализации",
                          command=lambda: sort_visual())
workmode_menu.add_command(label="Режим сравнения",
                          command=lambda: messagebox.showinfo(
                                                    "Необходимый режим",
                                                    "Вы уже в необходимом "
                                                    "режиме!"))


about_menu = Menu(main_menu, tearoff=0)
about_menu.add_command(label="О программе", command=lambda: about())

main_menu.add_cascade(label="Режим работы", menu=workmode_menu)
main_menu.add_cascade(label="Очистка", menu=clean_menu)
main_menu.add_cascade(label="Справка", menu=about_menu)

welcome_label = Label(root,
                      text="Сравнение времени, затраченного на пирамидальную "
                           "сортировку на различных массивах",
                      font="consolas 10 bold",
                      bg="white",
                      fg="#000080")
welcome_label.grid(row=1, rowspan=2, column=1, columnspan=4)

n1_label = Label(root,
                 text="Введите N1",
                 font="consolas 10",
                 bg="#000080",
                 fg="white")
n1_label.grid(row=3, column=2)

n1_count_entry = Entry(root, width=20)
n1_count_entry.grid(row=4, column=2)

n2_label = Label(root,
                 text="Введите N2",
                 font="consolas 10",
                 bg="#000080",
                 fg="white")
n2_label.grid(row=3, column=3)

n2_count_entry = Entry(root, width=20)
n2_count_entry.grid(row=4, column=3)

n3_label = Label(root,
                 text="Введите N3",
                 font="consolas 10",
                 bg="#000080",
                 fg="white")
n3_label.grid(row=3, column=4)

n3_count_entry = Entry(root, width=20)
n3_count_entry.grid(row=4, column=4)

n1_input_label = Label(root,
                       text="Введите диапазон N1",
                       font="consolas 10",
                       bg="#000080",
                       fg="white")
n1_input_label.grid(row=5, column=2)

n1_entry = Entry(root, width=20)
n1_entry.grid(row=6, column=2)

n1_asc_sorted = Entry(root, width=20)
n1_asc_sorted.grid(row=8, rowspan=2, column=2)
n1_desc_sorted = Entry(root, width=20)
n1_desc_sorted.grid(row=10, rowspan=2, column=2)
n1_rand_sorted = Entry(root, width=20)
n1_rand_sorted.grid(row=12, rowspan=2, column=2)
n1_sort_sorted = Entry(root, width=20)
n1_sort_sorted.grid(row=14, rowspan=2, column=2)
n1_out_entries = [n1_asc_sorted, n1_desc_sorted, n1_rand_sorted, n1_sort_sorted]
for entry in n1_out_entries:
    entry.config(state="readonly")

n2_input_label = Label(root,
                       text="Введите диапазон N2",
                       font="consolas 10",
                       bg="#000080",
                       fg="white")
n2_input_label.grid(row=5, column=3)

n2_entry = Entry(root, width=20)
n2_entry.grid(row=6, column=3)

n2_asc_sorted = Entry(root, width=20)
n2_asc_sorted.grid(row=8, rowspan=2, column=3)
n2_desc_sorted = Entry(root, width=20)
n2_desc_sorted.grid(row=10, rowspan=2, column=3)
n2_rand_sorted = Entry(root, width=20)
n2_rand_sorted.grid(row=12, rowspan=2, column=3)
n2_sort_sorted = Entry(root, width=20)
n2_sort_sorted.grid(row=14, rowspan=2, column=3)
n2_out_entries = [n2_asc_sorted, n2_desc_sorted, n2_rand_sorted, n2_sort_sorted]
for entry in n2_out_entries:
    entry.config(state="readonly")

n3_input_label = Label(root,
                       text="Введите диапазон N3",
                       font="consolas 10",
                       bg="#000080",
                       fg="white")
n3_input_label.grid(row=5, column=4)

n3_entry = Entry(root, width=20)
n3_entry.grid(row=6, column=4)

n3_asc_sorted = Entry(root, width=20)
n3_asc_sorted.grid(row=8, rowspan=2, column=4)
n3_desc_sorted = Entry(root, width=20)
n3_desc_sorted.grid(row=10, rowspan=2, column=4)
n3_rand_sorted = Entry(root, width=20)
n3_rand_sorted.grid(row=12, rowspan=2, column=4)
n3_sort_sorted = Entry(root, width=20)
n3_sort_sorted.grid(row=14, rowspan=2, column=4)
n3_out_entries = [n3_asc_sorted, n3_desc_sorted, n3_rand_sorted, n3_sort_sorted]
for entry in n3_out_entries:
    entry.config(state="readonly")

pass_label = Label(root, text="", bg="#000080")
pass_label.grid(row=7, columnspan=4)

sorted_ascending_label = Label(root,
                     text="Упорядоченный по\n возрастанию массив",
                     font="consolas 10",
                     bg="#000080",
                     fg="white")
sorted_ascending_label.grid(row=8, rowspan=2, column=1)

sorted_descending_label = Label(root,
                     text="Упорядоченный по\n убыванию массив",
                     font="consolas 10",
                     bg="#000080",
                     fg="white")
sorted_descending_label.grid(row=10, rowspan=2, column=1)

sorted_random_label = Label(root,
                     text="Заданный случайным\n образом массив",
                     font="consolas 10",
                     bg="#000080",
                     fg="white")
sorted_random_label.grid(row=12, rowspan=2, column=1)

sorted_sort_label = Label(root,
                     text="Отсортированный функцией\n sort массив",
                     font="consolas 10",
                     bg="#000080",
                     fg="white")
sorted_sort_label.grid(row=14, rowspan=2, column=1)



sort_all_button = Button(root, text="Отсортировать",
                         width=16,
                         height=2,
                         font="consolas 10 bold",
                         bg="white",
                         fg="#0ad325",
                         command=lambda: sort_timingly(1, [5,7]))
sort_all_button.grid(row=4, rowspan=2, column=1)

root.mainloop()
