class NamesHash:
    """Пример хэш функции возвращающий значение по ключу"""

    def __init__(self):
        self.values = [None] * 8

    def get_index_by_key(self, key: str) -> int:
        return len(key)

    def get_values_by_key(self, key: str) -> int:
        index = self.get_index_by_key(key)
        return self.values[index]


names_hash = NamesHash()
names_hash.values[2] = 14  # Ия
names_hash.values[3] = 99  # Аня
names_hash.values[4] = 30  # Миш
names_hash.values[5] = 42  # Антон
names_hash.values[6] = 87  # Владик
names_hash.values[7] = 71  # Николай


class PhonesHash:
    """Тот же принцып но индекс значению присваевается методом 
    деления с остатком номера телефона на длину масива"""

    def __init__(self):
        self.values = [None] * 40

    def get_index_by_key(self, key: int) -> int:
        return key % 40

    def get_values_by_key(self, key: int) -> int:
        index = self.get_index_by_key(key)
        return self.values[index]


"""
79101002030: 900,
79101234567: 100,
79999999999: 999,
74952223344: 1
... всего 40 номеров ...
"""
phones_hash = PhonesHash()
phones_hash.values[30] = 900
phones_hash.values[7] = 100
phones_hash.values[39] = 999

phones_hash.values[24] = 1


class DynamicArray:
    """Динамический масив, изменяет свою длину в зависимости от наполнения"""

    def __init__(self):
        self.values = [None] * 8
        self.size = 8
        self.current_index = 0

    def add(self, value: int) -> None:
        self.values[self.current_index] = value
        self.current_index += 1
        if self.current_index == self.size:
            self.resize(self.size * 2)

    def resize(self, new_size: int) -> None:
        new_values = [None] * new_size
        for i in range(self.size):
            new_values[i] = self.values[i]
        self.values = new_values
        self.size = new_size


dynamic_arr = DynamicArray()
print(dynamic_arr.values)
for i in range(8):
    dynamic_arr.add(i ** 2)
print(dynamic_arr.values)


class KeyValuePair:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value


class HashMap:
    """Простейший HashMap"""

    def __init__(self):
        self.entries = [None] * 8
        self.size = 8
        self.number_of_elements = 0

    def hash_function(self, key: str) -> int:
        return 0

    def add(self, key: str, value: str) -> None:
        index = self.find_good_index(key)
        self.entries[index] = KeyValuePair(key=key, value=value)
        self.number_of_elements += 1
        if self.number_of_elements == self.size:
            self.resize(self.size * 2)

    def resize(self, new_size: int) -> None:
        new_entries = [None] * new_size
        for i in range(self.size):
            entry = self.entries[i]
            index = self.find_good_index(entry.key)
            new_entries[index] = entry

        self.entries = new_entries
        self.size = new_size

    def get(self, key: str) -> str:
        index = self.find_good_index(key)
        if index == -1:
            return None
        entry = self.entries[index]
        if entry == None:
            return None
        return entry.value

    def find_good_index(self, key: str) -> int:
        hashh = self.hash_function(key)
        index = hashh % self.size
        for i in range(self.size):
            probing_index = (index + i) % self.size
            entry = self.entries[probing_index]
            if entry == None or entry.key == key:
                return probing_index
        return -1


hash_map = HashMap()
l = ['d', 'dd', 'ddd', 'dddd', 'ddddd', 'dddddd', 'ddddddd', 'dddddddd']

for i, v in enumerate(l):
    hash_map.add(v, str(i**2))

print(hash_map.get('ddd'))
print(hash_map.entries)
