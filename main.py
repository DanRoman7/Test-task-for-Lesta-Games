from collections import deque
# Нет тестовых вопросов под рукой, так уже ответил на них текстом, так что заранее извините, что отвечаю по памяти
# Вопрос 1
def is_even_mod(value):

    return value % 2 == 0

# Плюсы первого метода: Очень прост к восприятию, легко читается даже новичком.

# Минусы первого метода: На больших числах может давать тормозить, из-за операции деления.

def is_even_bit(value):

    return (value & 2) == 0

# Плюсы второго метода: Работает быстрее, так как использует побитовую операцию, а так же эффективен для больших чисел

# Минусы второго метода: Читается сложнее, особенно для новичков.

# Вопрос 2

""" Реализация циклической буферизации с помощью отслеживания индексов начала и конца"""
class CircularBuffer:
    def __init__(self, size):  # Инициализируем циклический буфер
        self.size = size  # Определяем максимальный размер буфера
        self.buffer = [None] * size  # Создаем список фиксированной длинны
        self.head = 0  # Индекс начала буфера
        self.tail = 0  # Индекс конца буфера
        self.full = False  # Флаг заполненности
        self.count = 0  # Количество элементов в буфере

    def append(self, item):  # Запись элементов
        self.buffer[self.tail] = item # запись элемента
        self.count += 1
        if self.full:
            self.head = (self.head + 1) % self.size  # Перезаписываем старые данные
            self.count -= 1
        self.tail = (self.tail + 1) % self.size  # Циклический сдвиг
        self.full = self.head == self.tail  # Проверка на заполненность, обновляем флаг

    def is_empty(self):
        return not self.full and (self.head == self.tail)  # Проверка на пустоту списка

    def is_full(self):
        return self.full

    def printbuffer(self):
        if self.full:
            return self.buffer[self.head:] + self.buffer[:self.tail]
        else:
            return self.buffer[self.head:self.tail]

"""Реализация с помощью встроенного модуля collections.deque """

class CollectionsQueue:
    def __init__(self, size):
        self.buffer = deque(maxlen=size)

    def add(self, item):
        self.buffer.append(item)

    def get_all(self):
        return list(self.buffer)

    def get(self):
        if not self.buffer:
            raise RuntimeError("Buffer is empty")
        return self.buffer[0]  # Возвращаем первый элемент

"""Реализация циклической буферизации без фиксированного размера"""

class CircularQueue:
    def __init__(self):
        # Инициализация пустого списка для хранения элементов
        self.queue = []

    def enqueue(self, item):
        # Добавление элемента в конец очереди
        self.queue.append(item)

    def dequeue(self):
        # Удаление элемента из начала очереди
        # Проверка на пустую очередь
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)

    def is_empty(self):
        # Проверка, пуста ли очередь
        return len(self.queue) == 0

    def size(self):
        # Возвращает количество элементов в очереди
        return len(self.queue)

# Вопрос 3
"""Быстрая сортировка считается оптимальной и в большинстве случаев самым быстрам алгоритмом сортировки.
Однако в Python есть встроенная функция sorted(), которая использует алгоритм Timsort(гибридный алгоритм слияния 
и вставки), который чаще работает быстрее QuickSort за счет своих оптимизаций"""

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[len(array) // 2]
        left = [i for i in array[1:] if i < pivot]
        right = [i for i in array[1:] if i > pivot]
        return quicksort(left) + [pivot] + quicksort(right)