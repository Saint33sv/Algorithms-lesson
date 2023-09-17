import hashlib

"""Модуль hashlib — хеширование строк в Python. Функция, которая с помощью
алгоритма SHA-1 получит хеш-сумму сообщения:"""
s = 'Привет'
hash_object = hashlib.sha1(s.encode('utf-8'))
hash_dig = hash_object.hexdigest()

print(hash_dig)
